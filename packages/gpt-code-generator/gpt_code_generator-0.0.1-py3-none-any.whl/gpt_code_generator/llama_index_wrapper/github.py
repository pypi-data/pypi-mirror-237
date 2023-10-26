from typing import List

from llama_index import Document, GithubRepositoryReader

from ..args.env import SaveEnv


class GitHub:
    def __init__(self, env: SaveEnv) -> None:
        self.env = env
        self.reader = GithubRepositoryReader(
            owner=env.github_owner,
            repo=env.github_repo,
            github_token=env.github_token,
            verbose=True,
            ignore_file_extensions=env.ignore_file_extensions,
            ignore_directories=env.ignore_directories,
        )

    def get_documents(
        self,
        commit_sha: str,
        branch: str,
    ) -> List[Document]:
        if commit_sha:
            return self.reader.load_data(commit_sha=commit_sha)
        return self.reader.load_data(branch=branch)
