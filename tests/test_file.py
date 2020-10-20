""" pytests for file API endpoints """

import pytest
from app import app
import json
import time
import uuid

from app.services import file_service

FILE_NAME = 'test_file_endpoints'
APPLICATION_TYPE = 'application/json'
HEADERS = {
    'Content-Type': APPLICATION_TYPE,
    'Accept': APPLICATION_TYPE
}
DATA = {
    'sessionId': str(FILE_NAME)
}


@pytest.fixture(scope="module")
def client():
    app.config['TESTING'] = True
    return app.test_client()


def setup_module(client):
    f = open('tests/titanic.csv', 'r')
    f.filename = FILE_NAME
    f.content_type = 'application/CSV'
    file_service.upload_file(f, FILE_NAME)
    f.close()


def test_file_upload(client):
    # arrange
    file_location = 'tests/titanic.csv'
    data = {
        'sessionId': str(FILE_NAME),
        'file': (open(file_location, 'rb'), FILE_NAME)
    }
    url = 'api/data/upload'

    # act
    resp = client.post(url, data=data, headers=HEADERS,
                       follow_redirects=True, content_type='multipart/form-data')

    # assert
    resp_json = json.loads(resp.json)
    nunique = resp_json['nunique']
    assert nunique is not None
    assert resp.status_code == 200


def test_create_unique_session(client):
    # arrange
    url = 'api/session/create'

    # act
    resp = client.post(url, headers=HEADERS, follow_redirects=True)
    uuid_response = resp.json
    
    # assert
    try:
        uuid_obj = uuid.UUID(uuid_response, version=4)
    except ValueError:
        return False

    is_uuid_valid = str(uuid_obj) == uuid_response

    assert is_uuid_valid
    assert resp.status_code == 200
