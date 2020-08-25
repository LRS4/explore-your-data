import os
import json
from google.cloud import storage
from google.oauth2 import service_account

BUCKET_NAME = os.getenv('BUCKET_NAME')

GOOGLE_CREDENTIALS = json.loads(
    str(os.getenv('GCLOUD_SERVICE_ACCOUNT_CREDENTIALS')))

credentials = service_account.Credentials.from_service_account_info(
    GOOGLE_CREDENTIALS)

storage_client = storage.Client(project=BUCKET_NAME, credentials=credentials)

bucket = storage_client.get_bucket(BUCKET_NAME)
