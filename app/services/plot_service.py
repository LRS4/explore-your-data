import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
import matplotlib.pyplot as plt
import seaborn as sns
import json


def get_distribution_plot(df, variable):
    """
    Returns distribution plot for numeric variables
    and a countplot for categorical variables
    """
    if (is_numeric_dtype(df[variable])):
        return sns.distplot(df[variable], kde=False)
    else:
        plot = sns.countplot(x=variable, data=df, palette="Blues")
        plot.set_xticklabels(plot.get_xticklabels(),
                             rotation=45, horizontalalignment='right')

        return plot


def get_scatter_plot(df, hue, x, y, reg: bool):
    """
    Returns regplot or scatter plot with optional hue
    """
    if reg == 1:
        return sns.regplot(
            data=df, x=x, y=y)
    elif hue == "none":
        return sns.scatterplot(
            data=df, x=x, y=y, legend='brief')
    else:
        return sns.scatterplot(
            data=df, x=x, y=y, hue=hue, legend='brief')


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
        return sns.countplot(x=filtered_df[target_column],
                             hue=x,
                             data=filtered_df,
                             palette="colorblind")
    else:
        if (is_numeric_dtype(data[target_column]) and analysis_type == 'categorical'):
            return sns.barplot(data=data,
                               x=x,
                               y=target_column,
                               palette="Blues")
        elif analysis_type == 'categorical':
            return sns.countplot(x=filtered_df[target_column],
                                 hue=x,
                                 data=filtered_df,
                                 palette="colorblind")
        else:
            return sns.barplot(data=data,
                               x=x,
                               y=data[target_column],
                               palette="Blues")
    
