""" pytests for data endpoints """

import pytest
from app import app


@pytest.fixture(scope="module")
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_add_two_numbers(client):
    resp = client.get('api/data/add/35/20')
    assert int(resp.data) == 55
