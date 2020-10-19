""" pytests for influencers service methods """

import pytest
import pandas as pd
import json
from app import app
import csv
from datetime import date
from io import StringIO, BytesIO

from app.services import file_service

TODAY = date.today().strftime("%d%m%Y")
FILE_NAME = 'test_csv_upload_' + str(TODAY)


@pytest.fixture(scope="module")
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_upload_file(client):

    # arrange
    f = open('tests/titanic.csv', 'r')
    f.filename = FILE_NAME
    f.content_type = 'application/CSV'

    # act
    file_service.upload_file(f, FILE_NAME)
    f.close()

    # assert
    filenames_in_bucket = file_service.list_files_in_bucket()
    file_name = FILE_NAME + '.csv'
    assert file_name in filenames_in_bucket


def test_get_bytestring(client):
    # act
    bytestring = file_service.get_bytestring(FILE_NAME)

    # assert
    assert type(bytestring) == bytes


def test_get_byte_fileobj(client):
    # act
    byte_stream = file_service.get_byte_fileobj(FILE_NAME + '.csv')

    # assert
    assert type(byte_stream) == BytesIO


def test_get_blob_URI(client):
    # arrange
    uri = 'test'

    # act
    blob_URI = file_service.get_blob_URI(FILE_NAME)

    # assert
    assert "gs://" in blob_URI
    assert FILE_NAME in blob_URI
