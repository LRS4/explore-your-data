""" pytests for data service methods """

import pytest
import pandas as pd
import json
from app import app

from app.services import data_service


@pytest.fixture(scope="module")
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_get_categorical_description(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')

    # act
    cat_description = data_service.get_categorical_description(df)
    json_data = json.loads(cat_description)

    # assert
    assert json_data['Name']['count'] == 891
    assert json_data['Cabin']['unique'] < 500


def test_get_numeric_description(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')

    # act
    num_description = data_service.get_numeric_description(df)
    json_data = json.loads(num_description)

    # assert
    assert json_data['PassengerId']['count'] == 891
    assert round(json_data['SibSp']['mean'], 2) == 0.52


def test_get_missing_values_info(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')

    # act
    total_missing_values, total_percentage_missing = data_service.get_missing_values_info(
        df)

    # assert
    assert total_missing_values == 866
    assert total_percentage_missing == 8.81


def test_get_total_kilobytes_in_memory(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')

    # act
    total_kilobytes_in_memory = data_service.get_total_kilobytes_in_memory(df)

    # assert
    assert total_kilobytes_in_memory > 80
    assert total_kilobytes_in_memory < 90


def test_get_duplicates_info(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')

    # act
    duplicate_row_count, duplicate_row_percent = data_service.get_duplicates_info(
        df)

    # assert
    assert duplicate_row_count == 0
    assert duplicate_row_percent < 0.01


def test_get_column_type_counts(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')

    # act
    column_type_counts = data_service.get_column_type_counts(df)

    # assert
    assert column_type_counts['num_col_count'] == 7
    assert column_type_counts['cat_col_count'] == 5


def test_populate_warning_messages(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')

    # act
    warning_messages = data_service.populate_warning_messages(df)

    # assert
    assert warning_messages[0]['type'] == 'High cardinality'
    assert warning_messages[1]['column'] == 'Name'
    assert warning_messages[7]['type'] == 'Missing values'
