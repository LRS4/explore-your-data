""" pytests for plot service methods """

import pytest
import pandas as pd
import matplotlib.pyplot as plt
import json
from app import app

from app.services import plot_service


@pytest.fixture(scope="module")
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_get_distribution_plot(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')

    # act
    distribution_plot = plot_service.get_distribution_plot(df, 'Age')

    # assert
    assert str(distribution_plot) == 'AxesSubplot(0.125,0.11;0.775x0.77)'


def test_get_scatter_plot(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')

    # act
    scatter_plot = plot_service.get_scatter_plot(df, 'Sex', 'Age', 'Fare', False)

    # assert
    assert str(scatter_plot) == 'AxesSubplot(0.125,0.11;0.775x0.77)'


def test_convert_continuous_target_dtype(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')

    # act
    target_dtype_int = plot_service.convert_continuous_target_dtype(
      df, 'Survived', 1
    )

    target_dtype_str = plot_service.convert_continuous_target_dtype(
        df, 'Sex', 'male'
    )

    # assert
    assert type(target_dtype_int) == int
    assert type(target_dtype_str) == str


def test_get_influencers_plot(client):
    # arrange
    df = pd.read_csv('tests/titanic.csv')
    target_column = 'Survived'
    target_value = 1
    filtered_df = df[df[target_column] == target_value]
    x = 'Sex'

    # act 
    influencers_plot = plot = plot_service.get_influencers_plot(
        df, filtered_df, x, target_column, analysis_type='categorical', is_actuals=0
    )

    # assert
    assert str(influencers_plot) == 'AxesSubplot(0.125,0.11;0.775x0.77)'
