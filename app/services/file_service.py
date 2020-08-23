import io
import os
import time
from werkzeug.utils import secure_filename
from .config import bucket

import numpy as np
import pandas as pd


def upload_file(file, session_id):
    """ Uploads a file to blob storage bucket """
    filename = secure_filename(str(session_id) + '.csv')
    file.save(filename)


def list_files_in_bucket():
    for blob in bucket.list_blobs():
        print(blob)


def read_file(filename) -> pd.DataFrame:
    """ Reads a file from blob storage bucket """
    return pd.read_csv(filename + ".csv")


def remove_file(filename):
    """ Removes a file from blob storage bucket """
    time.sleep(3)
    os.remove(filename + ".csv")
