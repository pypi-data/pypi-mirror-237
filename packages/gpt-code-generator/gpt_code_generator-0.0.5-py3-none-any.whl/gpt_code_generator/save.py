from .args.args import get_save_args
from .args.env import SaveEnv
from .llama_index_wrapper.api import Api
from .llama_index_wrapper.github import GitHub
from .storage.storage import Storage
from .zip.zip import compress


def main() -> None:
    args = get_save_args()
    env = SaveEnv()
    github = GitHub(env)
    api = Api(env)
    storage = Storage(env)

    documents = github.get_documents(
        args.commit_sha,
        args.branch,
    )
    api.save_documents(documents)
    compress(env.storage_context_tmp_dir, env.storage_context_tmp_dir)
    storage.upload_from_local(
        env.storage_context_tmp_zip,
        env.google_index_bucket_name,
        f"{env.github_owner}/{env.github_repo}/{args.output_file_name}.zip",
    )


if __name__ == "__main__":
    main()
