import json

from google.cloud.storage import Client  # type: ignore
from google.oauth2 import service_account  # type: ignore

from ..args.env import Env


class Storage:
    def __init__(self, env: Env) -> None:
        self.env = env
        info = json.loads(env.google_application_credentials_json)
        credentials = service_account.Credentials.from_service_account_info(info)
        self.client = Client(credentials=credentials)

    def upload_from_local(self, local_path: str, bucket_name: str, blob_name: str) -> None:
        bucket = self.client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(local_path)

    def download_to_local(self, local_path: str, bucket_name: str, blob_name: str) -> None:
        bucket = self.client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.download_to_filename(local_path)
