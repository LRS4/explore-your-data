""" pytests for data API endpoints """

import pytest
from app import app
import json
import time

from app.services import file_service

FILE_NAME = 'test_data_endpoints'
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


def test_add_two_numbers(client):
    resp = client.get('api/data/add/35/20')
    assert int(resp.data) == 55


def test_unique_values(client):
    # arrange
    url = 'api/data/uniques/Survived'

    # act
    resp = client.post(url, json=dict(
        DATA), headers=HEADERS, follow_redirects=True)

    # assert
    assert json.loads(resp.json)['uniques'] == [0, 1]
    assert resp.status_code == 200


def test_data_shape(client):
    # arrange
    url = 'api/data/shape'

    # act
    resp = client.post(url, json=dict(
        DATA), headers=HEADERS, follow_redirects=True)

    # assert
    resp_json = json.loads(resp.json)
    assert resp_json['rows'] > 890
    assert resp_json['columns'] == 12
    assert resp.status_code == 200


def test_describe_numeric_data(client):
    # arrange
    url = 'api/data/describe/numeric'

    # act
    resp = client.post(url, json=dict(
        DATA), headers=HEADERS, follow_redirects=True)

    # assert
    resp_json = json.loads(resp.json)
    assert round(resp_json['Survived']['mean'], 2) == 0.38
    assert resp.status_code == 200


def test_describe_categorical_data(client):
    # arrange
    url = 'api/data/describe/categorical'

    # act
    resp = client.post(url, json=dict(
        DATA), headers=HEADERS, follow_redirects=True)

    # assert
    resp_json = json.loads(resp.json)
    assert resp_json['Sex']['unique'] == 2
    assert resp.status_code == 200


def test_column_names(client):
    # arrange
    url = 'api/data/column_names'

    # act
    resp = client.post(url, json=dict(
        DATA), headers=HEADERS, follow_redirects=True)

    # assert
    resp_json = json.loads(resp.json)
    assert 'Sex' in resp_json['categorical']
    assert 'Age' in resp_json['numeric']
    assert resp.status_code == 200

    
def test_metadata(client):
    # arrange
    url = 'api/data/metadata'

    # act
    resp = client.post(url, json=dict(
        DATA), headers=HEADERS, follow_redirects=True)

    # assert
    resp_json = json.loads(resp.json)
    assert resp_json['totalMissingValues'] == 866
    assert len(resp_json['warningMessages']) > 1
    assert resp_json['observations'] == 891
    assert resp.status_code == 200


def test_crosstab(client):
    # arrange
    url = 'api/data/crosstab/Sex/Survived/1'

    # act
    resp = client.post(url, json=dict(
        DATA), headers=HEADERS, follow_redirects=True)

    # assert
    resp_json = json.loads(resp.json['crosstab'])
    percentage_females_survived = resp_json['1']['female']
    assert percentage_females_survived == 74.2
    assert resp.status_code == 200


def test_missing_data_imputer(client):
    # arrange
    timestamp = int(time.time())
    url = 'api/data/impute-missing-data/' + str(timestamp) + '/' + FILE_NAME

    # act
    resp = client.get(url, follow_redirects=True)

    # assert
    assert resp.headers['Content-Disposition'] == 'attachment; filename=imputed_missing.csv'
    assert resp.status_code == 200
