"""
REST API for plots and visuals
https://flask-restx.readthedocs.io/en/latest/quickstart.html
"""

import matplotlib
import pandas as pd
from pandas.api.types import is_numeric_dtype
import numpy as np
import base64
import io
import json
from . import api_rest
from flask_restx import Resource
from flask import request, send_file
from datetime import datetime
import matplotlib.pyplot as plt
from app.services import plot_service
from app.services import file_service
import seaborn as sns
sns.set(font_scale=1.5)

matplotlib.use('Agg')


@api_rest.route('/plots/distribution/<int:datetime>/<string:file_name>/<string:variable>')
class DistributionPlot(Resource):
    """ 
    Returns a distribution plot if the given variable is numeric.
    Returns a count plot if the given variable is categorical.
    """

    def get(self, variable, file_name, datetime):
        data = file_service.read_file(file_name)
        f, ax = plt.subplots(figsize=(11, 9))
        if (is_numeric_dtype(data[variable])):
            plot = sns.distplot(data[variable], kde=False)
        else:
            plot = sns.countplot(x=variable, data=data, palette="Blues")

        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)

        return send_file(bytes_image,
                         attachment_filename=f"{variable}_distribution.png",
                         mimetype='image/png')


@api_rest.route('/plots/scatter-plot/<int:datetime>/<string:file_name>/<string:x>/<string:y>')
class ScatterPlot(Resource):
    """ 
    Returns a scatter plot for the two provided x and y numeric variables and an optional
    hue for a categorical variable.

    :param datetime: the current datetime in integer format
    :param file_name: the file name represented by session_id
    :param x: the x variable
    :param y: the y variable
    :param hue: the categorical hue for the plot (optional) 
    :return: A bytes image seaborn scatter plot
    """

    def get(self, datetime, file_name, x, y):
        bytes_image = io.BytesIO()
        data = file_service.read_file(file_name)
        f, ax = plt.subplots(figsize=(11, 9))
        scatter = sns.scatterplot(data=data, x=x, y=y)
        plt.tight_layout()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)

        return send_file(bytes_image,
                         attachment_filename=f"scatter.png",
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


@api_rest.route('/plots/correlation/<int:datetime>/<string:file_name>')
class CorrelationPlot(Resource):
    """ Returns a correlation heatmap visualisation for the dataset"""

    def get(self, datetime, file_name):
        bytes_image = io.BytesIO()
        data = file_service.read_file(file_name)
        f, ax = plt.subplots(figsize=(11, 9))
        correlation_df = data.select_dtypes(
            include=[np.number]).corr(method='pearson')

        cmap = sns.diverging_palette(220, 10, as_cmap=True)
        mask = np.zeros_like(correlation_df, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True

        correlation_plot = sns.heatmap(correlation_df, mask=mask, annot=True,
                                       cmap=cmap, vmax=.3, center=0, square=True, linewidths=.5,
                                       cbar_kws={"shrink": .5})

        plt.tight_layout()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)

        return send_file(bytes_image,
                         attachment_filename=f"correlation-plot.png",
                         mimetype='image/png')
