"""
REST API for plots and visuals
https://flask-restx.readthedocs.io/en/latest/quickstart.html
"""

from app.services import influencers_service
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
from app.services import plot_service, file_service
import seaborn as sns

sns.set(font_scale=1.5)
matplotlib.use('Agg')


@api_rest.route('/plots/distribution/<int:datetime>/<string:file_name>/<string:variable>')
class DistributionPlot(Resource):

    def get(self, variable, file_name, datetime):
        """ 
        Returns distribution plot for numeric variables
        and a countplot for categorical variables.
        """
        data = file_service.read_file(file_name)

        f, ax = plt.subplots(figsize=(11, 9))
        plot = plot_service.get_distribution_plot(data, variable)
        plt.tight_layout()

        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        plt.close()

        return send_file(bytes_image,
                         attachment_filename=f"{variable}_distribution.png",
                         mimetype='image/png')


@api_rest.route('/plots/scatter-plot/<int:datetime>/<string:file_name>/<string:x>/<string:y>/<string:hue>/<int:reg>')
class ScatterPlot(Resource):

    def get(self, datetime, file_name, x, y, hue, reg):
        """ 
        Returns a scatter plot for the two provided x and y numeric variables and an optional
        hue for a categorical variable.

        :param datetime: the current datetime in integer format
        :param file_name: the file name represented by session_id
        :param x: the x variable
        :param y: the y variable
        :param hue: the categorical hue for the plot (optional) 
        :param reg: whether to display as a regression plot
        :return: A bytes image seaborn scatter plot
        """
        columns = [x, y] if hue == 'none' else [x, y, hue]
        data = file_service.read_file(file_name)

        if len(data.index) > 15000:
            data = data.sample(n=15000)

        plot = plot_service.get_scatter_plot(data, hue, x, y, reg)
        plt.tight_layout()

        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        plt.close()

        return send_file(bytes_image,
                         attachment_filename=f"scatter.png",
                         mimetype='image/png')


@api_rest.route('/plots/pairplot/<int:datetime>/<string:file_name>')
class PairPlot(Resource):

    def get(self, datetime, file_name):
        """ 
        Returns a standard pairplot for the dataset
        """
        data = file_service.read_file(file_name)

        f, ax = plt.subplots(figsize=(16, 9))
        pairplot = sns.pairplot(data)
        plt.tight_layout()

        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        plt.close()

        return send_file(bytes_image,
                         attachment_filename=f"pairplot.png",
                         mimetype='image/png')


@api_rest.route('/plots/missing-data-plot/<int:datetime>/<string:file_name>')
class MissingDataPlot(Resource):

    def get(self, datetime, file_name):
        """ 
        Returns a missing data visualisation for the dataset
        """
        data = file_service.read_file(file_name)

        f, ax = plt.subplots(figsize=(16, 9))
        missing_plot = sns.heatmap(
            data.isnull(), cbar=False, cmap="YlGnBu_r")
        plt.tight_layout()

        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        plt.close()

        return send_file(bytes_image,
                         attachment_filename=f"missing-data.png",
                         mimetype='image/png')


@api_rest.route('/plots/correlation/<int:datetime>/<string:file_name>/<string:columns>')
class CorrelationPlot(Resource):

    def get(self, datetime, file_name, columns):
        """ 
        Returns a correlation heatmap visualisation for the dataset
        """
        data = file_service.read_file(file_name)

        f, ax = plt.subplots(figsize=(16, 9))
        correlation_df = data[columns.split(',')].select_dtypes(
            include=[np.number]).corr(method='pearson')

        cmap = sns.diverging_palette(220, 10, as_cmap=True)
        mask = np.zeros_like(correlation_df, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True

        correlation_plot = sns.heatmap(correlation_df, mask=mask, annot=True,
                                       cmap=cmap, vmax=.3, center=0, square=True, linewidths=.5,
                                       cbar_kws={"shrink": .5})

        plt.tight_layout()
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        plt.close()

        return send_file(bytes_image,
                         attachment_filename=f"correlation-plot.png",
                         mimetype='image/png')


@api_rest.route('/plots/influencer-plot/<int:datetime>/<string:file_name>/<string:x>/<string:target_column>/<string:target_value>/<string:analysis_type>/<int:is_actuals>')
class InfluencerPlot(Resource):

    def get(self, datetime, file_name, x, target_column, target_value, analysis_type, is_actuals):
        """ 
        Returns a bar plot showing the percentages of each categorical features in the chosen column
        against the target variable.

        :param datetime: the current datetime in integer format
        :param file_name: the file name represented by session_id
        :param x: the x variable
        :param target_column: the target variable of the analysis
        :param target_value: the target value of the analysis
        :param analysis_type: a flag of 'categorical' or 'continuous' analysis type
        :param is_actuals: a flag where 1 is actual counts and 0 is percentages
        """
        data = file_service.read_file(file_name)

        data = influencers_service.bin_continuous_cols(data, target_column)
        f, ax = plt.subplots(figsize=(15, 11))

        if analysis_type != 'continuous':
            target_value = plot_service.convert_continuous_target_dtype(
                data, target_column, target_value
            )

        filtered_df = data[data[target_column] == target_value]

        plot = plot_service.get_influencers_plot(
            data, filtered_df, x, target_column, analysis_type, is_actuals)

        if (is_actuals == 1):
            base_count = len(data[data[target_column] == target_value])
        else:
            if (is_numeric_dtype(data[target_column])):
                base_mean = data[target_column].mean()
                plot.axhline(base_mean, ls='--',
                             label=f'Average {target_column}')
                plt.legend()

        plt.tight_layout()
        bytes_image = io.BytesIO()
        plt.savefig(bytes_image, format='png')
        bytes_image.seek(0)
        plt.close()

        return send_file(bytes_image,
                         attachment_filename=f"influencers.png",
                         mimetype='image/png')
