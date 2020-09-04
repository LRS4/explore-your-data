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


@api_rest.route('/data/describe')
class DescribeData(Resource):
    """ Returns summary description of a dataset """

    def post(self):
        file_name = request.get_json()['sessionId']
        data = file_service.read_file(file_name)
        return data.describe().to_json()


@api_rest.route('/data/numeric_columns')
class ContinuousColumnLabels(Resource):
    """ Returns the labels of the columns which are numeric """

    def post(self):
        file_name = request.get_json()['sessionId']
        data = file_service.read_file(file_name)
        numeric_variables = data.select_dtypes(include=[np.number])
        return numeric_variables.columns.to_json()


@api_rest.route('/data/categorical_columns')
class CategoricalColumnLabels(Resource):
    """ Returns the labels of the columns which are categorical """

    def post(self):
        file_name = request.get_json()['sessionId']
        data = file_service.read_file(file_name)
        numeric_variables = data.select_dtypes(include=['object', 'bool'])
        return numeric_variables.columns.to_json()
