"""
REST API for resources
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

from app.services import resource_service, data_service


class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]


@api_rest.route('/resource/<string:resource_id>')
class SystemTime(Resource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}

    def post(self, resource_id):
        json_payload = request.json
        return {'timestamp': json_payload}, 201


@api_rest.route('/resource/get-titanic-data')
class TitanicData(Resource):

    def get(self):
        """ 
        Returns titanic dataset in JSON format 
        """
        return data_service.get_titanic_data()


@api_rest.route('/resource/get-useful-links')
class UsefulLinks(Resource):

    def get(self):
        """ 
        Returns useful links for help section 
        """
        return resource_service.get_useful_links()
