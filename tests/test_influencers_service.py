""" pytests for influencers service methods """

import pytest
import pandas as pd
import json
from app import app

from app.services import influencers_service


@pytest.fixture(scope="module")
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_get_categorical_description(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')

    # act
    survived_frequency = influencers_service.get_target_base_frequency(
        df, 'Survived', 1)
    first_class_frequency = influencers_service.get_target_base_frequency(
        df, 'Pclass', 1)

    # assert
    assert round(survived_frequency, 2) == 0.38
    assert round(first_class_frequency, 2) == 0.24


def test_drop_columns_with_missing_over(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')

    # act
    drop_cabin = influencers_service.drop_columns_with_missing_over(0.5, df)
    drop_age = influencers_service.drop_columns_with_missing_over(0.95, df)

    # assert
    assert 'Cabin' not in drop_cabin.columns
    assert 'Age' in drop_cabin.columns
    assert 'Age' not in drop_age.columns


def test_bin_continuous_cols(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')

    # act
    binned_df = influencers_service.bin_continuous_cols(df, 'Fare', bins=10)
    target_is_skipped = binned_df['Fare'].nunique(dropna=True) > 10
    age_is_binned = binned_df['Age'].nunique(dropna=True) == 10
    passengerid_is_binned = binned_df['PassengerId'].nunique(dropna=True) == 10

    # assert
    assert target_is_skipped
    assert age_is_binned
    assert passengerid_is_binned


def test_populate_crosstab(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')

    # act
    crosstab = influencers_service.populate_crosstab(
        df, 'Sex', 'Survived', 1, show_as_percentages=True)

    # assert
    assert round(crosstab[1]['female'], 2) == 0.74


def test_populate_crosstab_json(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')
    crosstab = influencers_service.populate_crosstab(
        df, 'Sex', 'Survived', 1, show_as_percentages=True)

    # act
    jsonified = influencers_service.populate_crosstab_json(
        crosstab, 'Sex', 'Survived', 1)

    # assert
    assert jsonified[0] == {
        'parent_column_name': 'Sex',
        'index': 'female',
        'value': 74.2,
        'target_column': 'Survived',
        'target_value': 1
    }


def test_flatten_list(client):
    # arrange
    test_list = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

    # act
    flattened_list = influencers_service.flatten_list(test_list)

    # assert
    assert flattened_list == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']


def test_get_classification_influencers(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')

    # act
    influencers = influencers_service.get_classification_influencers(
        'Survived', 1, df)

    # assert
    assert len(influencers) > 7
    assert influencers[0] == {
        'parent_column_name': 'Sex',
        'index': 'female',
        'value': 74.2,
        'target_column': 'Survived',
        'target_value': 1
    }


def test_populate_regression_json(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')
    target_column = 'Fare'
    inc_or_dec = 'increase'
    column = 'Pclass'

    target_mean = df[target_column].mean()
    grouped = df[[column, target_column]].groupby(column).mean()
    grouped = grouped.sort_values(target_column,
                                  ascending=False)

    # act
    jsonified = influencers_service.populate_regression_json(
        grouped, column, target_column, target_mean, inc_or_dec)

    # assert
    assert jsonified[0] == {
        'parent_column_name': 'Pclass',
        'index': '1',
        'value': 84.15,
        'target_column': 'Fare',
        'target_value': 'increase',
        'difference_from_baseline_avg': 51.95
    }


def test_get_regression_influencers(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')

    # act
    influencers = influencers_service.get_regression_influencers(
        target_column='Fare', inc_or_dec='increase', df=df)

    # assert
    assert influencers != None
    assert influencers[11] == {
        'parent_column_name': 'Pclass',
        'index': '1',
        'value': 84.15,
        'target_column': 'Fare',
        'target_value': 'increase',
        'difference_from_baseline_avg': 51.95
    }


def test_find_key_influencers_for_categorical_inputs(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')

    # act
    survived_influencers = influencers_service.find_key_influencers(
        target_column='Survived', target_value=1, df=df, method='classification')

    # assert
    assert {
        'parent_column_name': 'Sex',
        'index': 'female',
        'value': 74.2,
        'target_column':
        'Survived',
        'target_value': 1
    } in survived_influencers


def test_find_key_influencers_for_continuous_inputs(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')

    # act
    fare_increase_influencers = influencers_service.find_key_influencers(
        target_column='Fare', target_value='increase', df=df, method='regression')

    fare_decrease_influencers = influencers_service.find_key_influencers(
        target_column='Fare', target_value='decrease', df=df, method='regression')

    # assert
    assert {
        'parent_column_name': 'Pclass', 
        'index': '1', 'value': 84.15,
        'target_column': 'Fare', 
        'target_value': 'increase', 
        'difference_from_baseline_avg': 51.95
    } in fare_increase_influencers

    assert {
        'parent_column_name': 'Embarked', 
        'index': 'Q', 
        'value': 13.28,
        'target_column': 'Fare', 
        'target_value': 'decrease', 
        'difference_from_baseline_avg': -18.93
    } in fare_decrease_influencers


