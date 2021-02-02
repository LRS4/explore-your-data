import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import ScalarFormatter
import json


def get_distribution_plot(df, variable):
    """
    Returns distribution plot for numeric variables
    and a countplot for categorical variables
    """
    if (is_numeric_dtype(df[variable])):
        plot = sns.distplot(df[variable], kde=False)
        plt.ticklabel_format(style='plain', axis='x')

        return plot
    else:
        plot = sns.countplot(x=variable, data=df, palette="Blues")
        plot.set_xticklabels(plot.get_xticklabels(),
                             rotation=45, horizontalalignment='right')

        return plot


def get_scatter_plot(df, hue, x, y, reg: bool):
    """
    Returns regplot or scatter plot with optional hue
    """
    f, ax = plt.subplots(figsize=(15, 11))
    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_major_formatter(ScalarFormatter())

    if reg == 1:
        plot = sns.regplot(
            data=df, x=x, y=y)
        plt.ticklabel_format(style='plain', axis='y')
        plt.ticklabel_format(style='plain', axis='x')

        return plot
    elif hue == "none":
        plot = sns.scatterplot(
            data=df, x=x, y=y, legend='brief')
        plt.ticklabel_format(style='plain', axis='y')
        plt.ticklabel_format(style='plain', axis='x')

        return plot
    else:
        plot = sns.scatterplot(
            data=df, x=x, y=y, hue=hue, legend='brief')
        plt.ticklabel_format(style='plain', axis='y')
        plt.ticklabel_format(style='plain', axis='x')

        return plot


def convert_continuous_target_dtype(df, target_column, target_value):
    """
    Returns target value converted to target column dtype
    """
    target_dtype = df[target_column].dtypes
    if target_dtype == 'float64':
        return float(target_value)
    elif target_dtype == 'int64':
        return int(target_value)
    else:
        return str(target_value)


def get_influencers_plot(data, filtered_df, x, target_column, analysis_type, is_actuals):
    """
    Returns count plot or barplot depending on whether is actuals (counts) or percentages
    and whether categorical or continuous variable passed in
    """
    if (is_actuals == 1):
        plot = sns.countplot(x=target_column,
                             hue=x,
                             data=filtered_df,
                             palette="colorblind")
        plt.ticklabel_format(style='plain', axis='y')

        return plot
    else:
        if (is_numeric_dtype(data[target_column]) and analysis_type == 'categorical'):
            plot = sns.barplot(data=data,
                               x=x,
                               y=target_column,
                               palette="Blues")
            plt.ticklabel_format(style='plain', axis='y')

            return plot
        elif analysis_type == 'categorical':
            ct = pd.crosstab(data[x], data[target_column],
                             normalize="index").round(4) * 100
            stacked = ct.stack().reset_index().rename(columns={0: 'percent %'})

            plot = sns.barplot(x=stacked[x],
                               y=stacked['percent %'],
                               hue=stacked[target_column],
                               palette="colorblind")
            plt.ticklabel_format(style='plain', axis='y')
            plot.set_xticklabels(plot.get_xticklabels(),
                                 rotation=45, horizontalalignment='right')

            return plot
        else:
            plot = sns.barplot(data=data,
                               x=x,
                               y=target_column,
                               palette="Blues")
            plt.ticklabel_format(style='plain', axis='y')
            plot.set_xticklabels(plot.get_xticklabels(),
                                 rotation=45, horizontalalignment='right')

            return plot
