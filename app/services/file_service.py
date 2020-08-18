import io
import os
import requests
import numpy as np
import pandas as pd
import time
from werkzeug.utils import secure_filename


def upload_file(file, session_id):
    """ Uploads a file to blob storage """
    filename = secure_filename(str(session_id) + '.csv')
    file.save(filename)


def read_file(filename) -> pd.DataFrame:
    """ Reads a file to blob storage """
    return pd.read_csv(filename + ".csv")


def remove_file(filename):
    """ Removes a file to blob storage """
    time.sleep(3)
    os.remove(filename + ".csv")
