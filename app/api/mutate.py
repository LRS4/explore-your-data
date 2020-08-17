"""
REST API for Data Operations
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

@api_rest.route('/mutate/add/<int:number_one>/<int:number_two>')
class AddTwoNumbers(Resource):
    """ Adds two numbers """

    def get(self, number_one, number_two):
        return number_one + number_two


@api_rest.route('/mutate/describe')
class DescribeData(Resource):
    """ Returns summary description of a dataset """

    def post(self):
        file_name = request.get_json()['sessionId']
        data = pd.read_csv(file_name + '.csv')
        return data.describe().to_json()
