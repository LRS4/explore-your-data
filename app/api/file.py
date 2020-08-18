"""
REST API for file operations
https://flask-restx.readthedocs.io/en/latest/quickstart.html
"""

from datetime import datetime
from flask import request
from flask_restx import Resource
from werkzeug.utils import secure_filename

from .security import require_auth
from . import api_rest

import requests
import numpy as np
import pandas as pd
import json
import io
import os
import uuid

from app.services import file_service


@api_rest.route('/data/upload')
class FileUpload(Resource):
    """ Handles file upload """

    def post(self):
        f = request.files['file']
        session_id = request.form['sessionId']
        file_service.upload_file(f, session_id)
        data = file_service.read_file(session_id)
        return data.head(20).to_json()


@api_rest.route('/session/create')
class CreateUniqueSession(Resource):
    """ Creates a unique session ID """

    def post(self):
        sessionId = str(uuid.uuid4())
        return sessionId
