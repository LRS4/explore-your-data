"""
REST API for data operations
https://flask-restx.readthedocs.io/en/latest/quickstart.html
"""

from datetime import datetime
from flask import request, make_response
from flask_restx import Resource

from .security import require_auth
from . import api_rest

import json
import io
import requests
import numpy as np
import pandas as pd

from app.services import file_service, data_service


@api_rest.route('/data/add/<int:number_one>/<int:number_two>')
class AddTwoNumbers(Resource):
    """ Adds two numbers """

    def get(self, number_one, number_two):
        return number_one + number_two


@api_rest.route('/data/uniques/<string:column_name>')
class UniqueValues(Resource):

    def post(self, column_name):
        """ Returns the unique values for the given column """
        file_name = request.get_json()['sessionId']
        data = file_service.read_file(file_name)
        data[column_name].fillna('Missing', inplace=True)
        uniques = pd.unique(data[column_name])
        uniques_json = json.dumps({
            'uniques': np.sort(uniques).tolist()
        })
        return uniques_json


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


@api_rest.route('/data/metadata')
class MetaData(Resource):
    """ Returns a json object with information (metadata) on the
    dataset """

    def post(self):
        file_name = request.get_json()['sessionId']
        data = file_service.read_file(file_name)
        total_missing_values, total_missing_percent = data_service.get_missing_values_info(
            data)
        total_duplicate_rows, total_duplicates_percent = data_service.get_duplicates_info(
            data)

        return json.dumps({
            'totalMissingValues': int(total_missing_values),
            'totalMissingPercent': total_missing_percent,
            'totalKbInMemory': data_service.get_total_kilobytes_in_memory(data),
            'variables': int(data.shape[1]),
            'observations': int(data.shape[0]),
            'totalDuplicatedRows': int(total_duplicate_rows),
            'totalDuplicatedPercent': total_duplicates_percent,
            'columnsInfo': data_service.get_column_type_counts(data),
            'warningMessages': data_service.populate_warning_messages(data)
        })


@api_rest.route('/data/crosstab/<string:x>/<string:y>/<int:show_as_percentages>')
class CrossTab(Resource):
    """ Returns a json object containing a cross tabulation (pivot table)
    data structure for x and y variables """

    def post(self, x, y, show_as_percentages=False):
        file_name = request.get_json()['sessionId']
        data = file_service.read_file(file_name)
        if (show_as_percentages):
            crosstab = pd.crosstab(
                data[x], data[y], normalize='index').round(4) * 100
        else:
            crosstab = pd.crosstab(data[x], data[y])

        return {
            'crosstab': crosstab.to_json(),
            'transposed': crosstab.transpose().to_json()
        }


@api_rest.route('/data/impute-missing-data/<int:datetime>/<string:file_name>')
class MissingDataImputer(Resource):
    """ Returns a CSV with all missing data imputed """

    def get(self, datetime, file_name):
        data = file_service.read_file(file_name)
        data.fillna(data.median(), inplace=True)
        data.fillna(value='missing', inplace=True)

        resp = make_response(data.to_csv(index=False))
        resp.headers["Content-Disposition"] = "attachment; filename=imputed_missing.csv"
        resp.headers["Content-Type"] = "text/csv"
        return resp
