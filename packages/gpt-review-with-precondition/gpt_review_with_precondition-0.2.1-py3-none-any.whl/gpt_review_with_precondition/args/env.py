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
        self.google_application_credentials_json = os.environ.get(
            "GOOGLE_APPLICATION_CREDENTIALS_JSON", ""
        )
        self.azure_open_ai_embedding_model_name = os.environ.get(
            "AZURE_OPEN_AI_EMBEDDING_MODEL_NAME", ""
        )
        self.azure_open_ai_embedding_model_deploy_name = os.environ.get(
            "AZURE_OPEN_AI_EMBEDDING_MODEL_DEPLOY_NAME", ""
        )
        self.google_index_bucket_name = os.environ.get("GOOGLE_INDEX_BUCKET_NAME", "")
        self.google_index_file_name = os.environ.get("GOOGLE_INDEX_FILE_NAME", "index.zip")
        self.storage_context_tmp_dir = "./tmp/storage_context"
        self.storage_context_tmp_zip = "./tmp/storage_context.zip"
        shutil.rmtree("./tmp", ignore_errors=True)
        os.makedirs(self.storage_context_tmp_dir, exist_ok=True)

        assert self.azure_open_ai_key is not None
        assert self.azure_open_ai_endpoint is not None
        assert self.azure_open_ai_model_name is not None
        assert self.azure_open_ai_model_deploy_name is not None
        assert self.azure_open_ai_embedding_model_name is not None
        assert self.azure_open_ai_embedding_model_deploy_name is not None
        assert self.google_application_credentials_json is not None
        assert self.google_index_bucket_name is not None
        assert self.google_index_file_name is not None


class ReviewEnv(Env):
    def __init__(self) -> None:
        super().__init__()
        self.dummy = ""


class SaveEnv(Env):
    def __init__(self) -> None:
        super().__init__()
        self.notion_api_key = os.environ.get("NOTION_API_KEY", "")
        assert self.notion_api_key is not None
