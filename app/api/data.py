"""
REST API for data operations
https://flask-restx.readthedocs.io/en/latest/quickstart.html
"""

from datetime import datetime
from flask import request
from flask_restx import Resource

from .security import require_auth
from . import api_rest

import requests
import numpy as np
import pandas as pd
import json
import io

from app.services import file_service


@api_rest.route('/data/add/<int:number_one>/<int:number_two>')
class AddTwoNumbers(Resource):
    """ Adds two numbers """

    def get(self, number_one, number_two):
        return number_one + number_two


@api_rest.route('/data/shape')
class DataShape(Resource):
    """ Returns shape of the data """

    def post(self):
        file_name = request.get_json()['sessionId']
        data = file_service.read_file(file_name)
        shape = data.shape
        return json.dumps({'rows': shape[0], 'columns': shape[1]})


@api_rest.route('/data/describe/numeric')
class DescribeNumericData(Resource):
    """ 
    Returns summary description of the numeric variables in the dataset 
    """

    def post(self):
        file_name = request.get_json()['sessionId']
        data = file_service.read_file(file_name)
        return data.describe().to_json()


@api_rest.route('/data/describe/categorical')
class DescribeCategoricalData(Resource):
    """ 
    Returns summary description of the categorical variables in the dataset 
    """

    def post(self):
        file_name = request.get_json()['sessionId']
        data = file_service.read_file(file_name)
        categorical_df = data.select_dtypes(
            include=['object', 'bool'])

        return categorical_df.describe().to_json()


@api_rest.route('/data/column_names')
class ColumnNames(Resource):
    """ Returns the labels of the columns for both numeric
    and categorical variables """

    def post(self):
        file_name = request.get_json()['sessionId']
        data = file_service.read_file(file_name)
        numeric_df = data.select_dtypes(include=[np.number])
        categorical_df = data.select_dtypes(include=['object', 'bool'])
        return json.dumps({
            'categorical': list(categorical_df.columns.values),
            'numeric': list(numeric_df.columns.values)
        })
