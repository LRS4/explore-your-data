"""
REST API for file operations
https://flask-restx.readthedocs.io/en/latest/quickstart.html
"""

from datetime import datetime
from flask import request
from flask_restx import Resource
from werkzeug.utils import secure_filename
import json

from .security import require_auth
from . import api_rest
import uuid

from app.services import file_service, data_service


@api_rest.route('/data/upload')
class FileUpload(Resource):

    def post(self):
        """ Handles file upload """
        f = request.files['file']
        session_id = request.form['sessionId']
        file_service.upload_file(f, session_id)
        data = file_service.read_file(session_id)
        
        return data_service.get_metadata_information(data)


@api_rest.route('/session/create')
class CreateUniqueSession(Resource):

    def post(self):
        """ Creates a unique session ID """
        sessionId = str(uuid.uuid4())
        return sessionId
