"""
REST API for plots and visuals
https://flask-restx.readthedocs.io/en/latest/quickstart.html
"""

from app.services import plot_service
from app.services import file_service
import seaborn as sns
sns.set(font_scale=1.5)
import matplotlib.pyplot as plt
from datetime import datetime
from flask import request, send_file
from flask_restx import Resource
from . import api_rest
import json

import io
import base64
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')


@api_rest.route('/plots/distribution/<string:file_name>/<string:variable>')
class DistributionPlot(Resource):
    """ Returns a distribution plot for the given variable """

    def get(self, variable, file_name):
        data = file_service.read_file(file_name)
        f, ax = plt.subplots(figsize=(11, 9))
        dist_plot = sns.distplot(data[variable])
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)

        return send_file(bytes_image,
                         attachment_filename=f"{variable}_distribution.png",
                         mimetype='image/png')


@api_rest.route('/plots/pairplot/<int:datetime>/<string:file_name>')
class PairPlot(Resource):
    """ Returns a standard pairplot for the dataset"""

    def get(self, datetime, file_name):
        bytes_image = io.BytesIO()
        data = file_service.read_file(file_name)
        f, ax = plt.subplots(figsize=(11, 9))
        pairplot = sns.pairplot(data)
        plt.tight_layout()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)

        return send_file(bytes_image,
                         attachment_filename=f"pairplot.png",
                         mimetype='image/png')


@api_rest.route('/plots/missing-data-plot/<int:datetime>/<string:file_name>')
class MissingDataPlot(Resource):
    """ Returns a missing data visualisation for the dataset"""

    def get(self, datetime, file_name):
        bytes_image = io.BytesIO()
        data = file_service.read_file(file_name)
        f, ax = plt.subplots(figsize=(11, 9))
        missing_plot = sns.heatmap(
            data.isnull(), cbar=False, cmap="YlGnBu_r")
        plt.tight_layout()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)

        return send_file(bytes_image,
                         attachment_filename=f"missing-data.png",
                         mimetype='image/png')
