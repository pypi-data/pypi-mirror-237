import os
import shutil


class Env:
    def __init__(self) -> None:
        self.azure_open_ai_key = os.environ.get("AZURE_OPEN_AI_KEY", "")
        self.azure_open_ai_endpoint = os.environ.get("AZURE_OPEN_AI_ENDPOINT", "")
        # example: "2023-05-15"
        # ref https://learn.microsoft.com/en-us/azure/ai-services/openai/reference
        self.azure_open_ai_version = os.environ.get("AZURE_OPEN_AI_VERSION", "")
        self.azure_open_ai_model_name = os.environ.get("AZURE_OPEN_AI_MODEL_NAME", "")
        self.azure_open_ai_model_deploy_name = os.environ.get("AZURE_OPEN_AI_MODEL_DEPLOY_NAME", "")
        self.azure_open_ai_embedding_model_name = os.environ.get(
            "AZURE_OPEN_AI_EMBEDDING_MODEL_NAME", ""
        )
        self.azure_open_ai_embedding_model_deploy_name = os.environ.get(
            "AZURE_OPEN_AI_EMBEDDING_MODEL_DEPLOY_NAME", ""
        )
        self.google_application_credentials_json = os.environ.get(
            "GOOGLE_APPLICATION_CREDENTIALS_JSON", ""
        )
        self.google_index_bucket_name = os.environ.get("GOOGLE_INDEX_BUCKET_NAME", "")
        self.github_owner = os.environ.get("GITHUB_OWNER", "")
        self.github_repo = os.environ.get("GITHUB_REPO", "")

        self.storage_context_tmp_dir = "./tmp/storage_context"
        self.storage_context_tmp_zip = "./tmp/storage_context.zip"
        shutil.rmtree("./tmp", ignore_errors=True)
        os.makedirs(self.storage_context_tmp_dir, exist_ok=True)

        assert self.azure_open_ai_key
        assert self.azure_open_ai_endpoint
        assert self.azure_open_ai_model_name
        assert self.azure_open_ai_model_deploy_name
        assert self.azure_open_ai_embedding_model_name
        assert self.azure_open_ai_embedding_model_deploy_name
        assert self.google_application_credentials_json
        assert self.google_index_bucket_name
        assert self.github_owner
        assert self.github_repo


class GeneratorEnv(Env):
    def __init__(self) -> None:
        super().__init__()
        self.dummy = ""


class SaveEnv(Env):
    def __init__(self) -> None:
        super().__init__()
        self.github_token = os.environ.get("GITHUB_TOKEN", "")
        self.ignore_file_extensions = os.environ.get("IGNORE_FILE_EXTENSIONS", "").split(",")
        self.ignore_directories = os.environ.get("IGNORE_DIRECTORIES", "").split(",")
        assert self.github_token
