""" pytests for influencers API endpoints """

import pytest
from app import app
import json
import time

from app.services import file_service

FILE_NAME = 'test_influencers_endpoints'
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


def test_key_influencers(client):
    # arrange
    url = 'api/data/influencers/categorical/Survived/1'

    # act
    resp = client.post(url, json=dict(
        DATA), headers=HEADERS, follow_redirects=True)

    # assertn
    json_resp = json.loads(resp.json)
    assert json_resp['influencers'][0]['target_column'] == 'Survived'
    assert resp.status_code == 200
