import sys


class Args:
    def __init__(self, args: list[str], help_message: str) -> None:
        super().__init__()
        self.args = args

        args_count = len(args)
        self.commit_sha = ""
        self.branch = ""
        for i in range(1, args_count):
            arg = args[i]
            if arg in {"-h", "--help", "-?"} and i + 1 < args_count:
                print_help(help_message)
            elif arg in {"-c", "--commit-sha"} and i + 1 < args_count:
                self.commit_sha = args[i + 1]
            elif arg in {"-b", "--branch"} and i + 1 < args_count:
                self.branch = args[i + 1]

        if not self.commit_sha and not self.branch:
            print("Error: commit_sha or branch must be specified.", sys.stderr)
            print_help(help_message)

        if self.commit_sha and self.branch:
            print("Error: commit_sha and branch cannot be specified at the same time.", sys.stderr)
            print_help(help_message)

        self.output_file_name = self.commit_sha or self.branch


class GeneratorArgs(Args):
    def __init__(self, args: list[str]) -> None:
        help_message = """
Usage: gpt-code-generator [options]
Generate code from the prompt with precondition.

[options]
-p, --prompt-file-path <prompt-file-path> [required] Path to the prompt file.
-c, --commit-sha <commit_sha>             Commit SHA of the repository to save.
-b, --branch <branch>                     Branch of the repository to save.
-?, -h, --help                            Print this message.
            """
        super().__init__(
            args,
            help_message,
        )

        args_count = len(args)
        self.prompt_path = ""
        for i in range(1, args_count):
            arg = args[i]
            if arg in {"-p", "--prompt-file-path"} and i + 1 < args_count:
                self.prompt_path = args[i + 1]

        if not self.prompt_path:
            print("Error: prompt-file-path must be specified.", sys.stderr)
            print_help(help_message)

    def get_prompt(self) -> str:
        with open(self.prompt_path, encoding="utf-8") as f:
            s = f.read()
            return s


class SaveArgs(Args):
    def __init__(self, args: list[str]) -> None:
        super().__init__(
            args,
            """
Usage: save-code-generating-precondition [options]
Save the code generating precondition to Google Cloud Storage.

[options]
-c, --commit-sha <commit_sha>  Commit SHA of the repository to save.
-b, --branch <branch>          Branch of the repository to save.
-?, -h, --help                 Print this message.
            """,
        )


def get_generator_args() -> GeneratorArgs:
    a = GeneratorArgs(sys.argv)
    return a


def get_save_args() -> SaveArgs:
    a = SaveArgs(sys.argv)
    return a


def print_help(help_message: str) -> None:
    print(
        help_message,
        sys.stderr,
    )
    sys.exit(1)
