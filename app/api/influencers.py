"""
REST API for key influencers
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

from app.services import file_service, influencers_service


@api_rest.route('/data/influencers/<string:analysis_type>/<string:target_column>/<string:target_value>')
class KeyInfluencers(Resource):

    @require_auth
    def post(self, analysis_type, target_column, target_value):
        """ Returns key influencers json """
        file_name = request.get_json()['sessionId']
        data = file_service.read_file(file_name)

        target_dtype = data[target_column].dtypes

        if analysis_type != 'continuous':
            if target_dtype == 'float64':
                target_value = float(target_value)
            elif target_dtype == 'int64':
                target_value = int(target_value)
            else:
                target_value = str(target_value)

        method = 'classification' if analysis_type == 'categorical' else 'regression'

        influencers = influencers_service.find_key_influencers(target_column, target_value, df=data, method=method)

        return json.dumps({
            'influencers': influencers
        })
