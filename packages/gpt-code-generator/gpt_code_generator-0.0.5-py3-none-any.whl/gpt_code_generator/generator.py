from .args.args import get_generator_args
from .args.env import GeneratorEnv
from .llama_index_wrapper.api import Api
from .storage.storage import Storage
from .zip.zip import decompress


def main() -> None:
    args = get_generator_args()
    env = GeneratorEnv()
    storage = Storage(env)
    storage.download_to_local(
        env.storage_context_tmp_zip,
        env.google_index_bucket_name,
        f"{env.github_owner}/{env.github_repo}/{args.output_file_name}.zip",
    )
    decompress(env.storage_context_tmp_zip, env.storage_context_tmp_dir)
    api = Api(env)
    api.ask(args.get_prompt())


if __name__ == "__main__":
    main()
