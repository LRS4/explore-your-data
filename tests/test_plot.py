""" pytests for plot API endpoints """

import pytest
from app import app
import json
import time

from app.services import file_service

FILE_NAME = 'test_plot_endpoints'


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


def test_distribution_plot(client):
    # arrange
    timestamp = int(time.time())
    url = 'api/plots/distribution/' + \
        str(timestamp) + '/' + FILE_NAME + '/' + 'Age'

    # act
    resp = client.get(url, follow_redirects=True)

    # assert
    assert resp.status_code == 200


def test_scatter_plot(client):
    # arrange
    timestamp = int(time.time())
    url = 'api/plots/scatter-plot/' + \
        str(timestamp) + '/' + FILE_NAME + '/Age/Fare/Sex/0'

    # act
    resp = client.get(url, follow_redirects=True)

    # assert
    assert resp.status_code == 200


def test_pair_plot(client):
    # arrange
    timestamp = int(time.time())
    url = 'api/plots/pairplot/' + str(timestamp) + '/' + FILE_NAME

    # act
    resp = client.get(url, follow_redirects=True)

    # assert
    assert resp.status_code == 200


def test_missing_data_plot(client):
    # arrange
    timestamp = int(time.time())
    url = 'api/plots/missing-data-plot/' + str(timestamp) + '/' + FILE_NAME

    # act
    resp = client.get(url, follow_redirects=True)

    # assert
    assert resp.status_code == 200


def test_correlation_plot(client):
    # arrange
    timestamp = int(time.time())
    columns = 'Age,Fare,Pclass'
    url = 'api/plots/correlation/' + \
        str(timestamp) + '/' + FILE_NAME + '/' + columns

    # act
    resp = client.get(url, follow_redirects=True)

    # assert
    assert resp.status_code == 200


def test_influencer_plot(client):
    # arrange
    timestamp = int(time.time())
    x, target_column, target_value = 'Sex', 'Survived', 1
    analysis_type = 'categorical'
    is_actuals = 0

    url = 'api/plots/influencer-plot/' + \
        str(timestamp) + \
        '/' + FILE_NAME + \
        '/' + x + \
        '/' + target_column + \
        '/' + str(target_value) + \
        '/' + analysis_type + \
        '/' + str(is_actuals)

    # act
    resp = client.get(url, follow_redirects=True)

    # assert
    assert resp.status_code == 200
