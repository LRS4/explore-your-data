from io import StringIO, BytesIO
import os
import time
from werkzeug.utils import secure_filename
from .config import bucket, BUCKET_NAME
import numpy as np
import pandas as pd


def upload_file(file, session_id):
    """ Uploads a file to blob storage bucket """
    file.filename = secure_filename(str(session_id) + '.csv')

    blob = bucket.blob(blob_name=file.filename)

    blob.upload_from_string(
        file.read(),
        content_type=file.content_type
    )


def read_file(filename) -> pd.DataFrame:
    """ Reads a file from blob storage bucket """
    file_object = get_byte_fileobj(filename + '.csv')
    return pd.read_csv(file_object)


def remove_file(filename):
    """ Removes a file from blob storage bucket """
    time.sleep(3)
    os.remove(filename + ".csv")


def list_files_in_bucket():
    files = bucket.list_blobs()
    fileList = [file.name for file in files if '.' in file.name]
    return fileList


def get_byte_fileobj(blob_name: str) -> BytesIO:
    """
    Retrieve data from a given blob on Google Storage and pass it as a file object.
    :param path: path within the bucket
    :param project: name of the project
    :param bucket_name: name of the bucket
    :param service_account_credentials_path: path to credentials.
           TIP: can be stored as env variable, e.g. os.getenv('GOOGLE_APPLICATION_CREDENTIALS_DSPLATFORM')
    :return: file object (BytesIO)
    """
    blob = bucket.blob(blob_name)
    byte_stream = BytesIO()
    blob.download_to_file(byte_stream)
    byte_stream.seek(0)
    return byte_stream


def get_bytestring(blob_name: str) -> bytes:
    """
    Retrieve data from a given blob on Google Storage and pass it as a byte-string.
    :param path: path within the bucket
    :param project: name of the project
    :param bucket_name: name of the bucket
    :param service_account_credentials_path: path to credentials.
           TIP: can be stored as env variable, e.g. os.getenv('GOOGLE_APPLICATION_CREDENTIALS_DSPLATFORM')
    :return: byte-string (needs to be decoded)
    """
    blob = bucket.blob(blob_name + '.csv')
    return blob.download_as_bytes()


def get_blob_URI(blob_name):
    """Prints out a blob's URI."""
    blob = bucket.blob(blob_name + '.csv')
    link = blob.path_helper(BUCKET_NAME, blob_name + '.csv')
    return f"gs://{link}"
