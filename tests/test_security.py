""" pytests for security method """

import pytest
from app import app
import json
import time

from app.api.security import require_auth

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


def test_secure_decorator_with_valid_request(client):
    # arrange
    url = 'api/data/influencers/categorical/Survived/1'

    # act
    valid_response = client.post(url, json=dict(
        DATA), headers=HEADERS, follow_redirects=True)

    # assert
    assert valid_response.status_code == 200


def test_secure_decorator_with_invalid_request(client):
    # arrange
    url = 'api/data/influencers/categorical/Survived/1'
    invalid_data = {
      'sessionIdNotPresentHere': '123'
    }

    # act
    valid_response = client.post(url, json=dict(
        invalid_data), headers=HEADERS, follow_redirects=True)

    # assert
    assert valid_response.status_code == 401
