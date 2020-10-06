import numpy as np
import pandas as pd
import json
from operator import add
from functools import reduce


def get_titanic_data() -> list:
    url = "https://gist.githubusercontent.com/michhar/2dfd2de0d4f8727f873422c5d959fff5/raw/fa71405126017e6a37bea592440b4bee94bf7b9e/titanic.csv"
    df = pd.read_csv(url)
    return df.to_json()


def get_categorical_description(df):
    """ 
    Returns the Pandas describe method for the categorical
    variables in the dataset

    :param df: the pandas DataFrame
    :return: A DataFrame description in json format
    """
    categorical_df = df.select_dtypes(
        include=['object', 'bool'])

    return categorical_df.describe().to_json()


def get_numeric_description(df):
    """ 
    Returns the Pandas describe method for the numeric
    variables in the dataset

    :param df: the pandas DataFrame
    :return: A DataFrame description in json format
    """
    return df.describe().to_json()


def get_missing_values_info(df):
    """ 
    Returns the total missing value counts and total percentage 
    of data missing from the provided DataFrame

    :param df: the pandas DataFrame
    :return total_missing_values: A sum of missing values
    :return total_percentage_missing: A decimal representing the total percentage 
    of data missing
    """
    total_missing_values = reduce(add, df.isnull().sum())
    total_row_counts = reduce(add, df.count())
    total_percentage_missing = round(
        (total_missing_values / total_row_counts) * 100, 2)

    return total_missing_values, total_percentage_missing


def get_total_kilobytes_in_memory(df):
    """ 
    Returns the total bytes in memory that the DataFrame consumes

    :param df: the pandas DataFrame
    :return: A sum of the total bytes in memory the DataFrame consumes
    """
    bytes_in_memory = reduce(add, df.memory_usage())
    total_kilobytes_in_memory = round(bytes_in_memory / 1000, 2)
    return total_kilobytes_in_memory


def get_duplicates_info(df):
    """ 
    Returns the total duplicate rows and the percentage of the DataFrame 
    that contains missing values

    :param df: the pandas DataFrame
    :return duplicate_row_count: The total duplicate rows sum
    :return duplicate_row_percent: The percentage of the DataFrame 
    that contains missing values
    """
    total_row_count = df.shape[0]
    duplicate_row_count = df.duplicated().sum()
    duplicate_row_percent = duplicate_row_count / total_row_count
    return duplicate_row_count, duplicate_row_percent


def get_column_type_counts(df):
    """ 
    Returns the count of categorical and numeric columns in the DataFrame

    :param df: the pandas DataFrame
    :return: A dictionary of how many categorical and numeric columns are in the
    DataFrame
    """
    num_col_names = df.select_dtypes(include=[np.number]).columns
    cat_col_names = df.select_dtypes(include=['object', 'bool']).columns
    return {
        'num_col_names': list(num_col_names),
        'cat_col_names': list(cat_col_names),
        'num_col_count': len(num_col_names),
        'cat_col_count': len(cat_col_names)
    }


def populate_warning_messages(df):
    """ 
    Returns an array of warning objects about the DataFrame. These consist of 
    high cardinality, high missing values, and high zero count warnings.

    :param df: the pandas DataFrame
    :return: A list of warning messages
    """
    warning_messages = []
    total_row_count = df.shape[0]

    unique_values = df.nunique().to_frame().transpose()
    for column in unique_values:
        value = unique_values[column][0]
        if value > 20:
            warning_messages.append({
                'column': str(column),
                'message': 'has high cardinality: ' + str(value) + ' distinct values',
                'type': 'High cardinality'
            })

    missing_values = df.isnull().sum().to_frame().transpose()
    for column in missing_values:
        value = int(missing_values[column][0])
        percentage = round((value / total_row_count) * 100, 2)
        if percentage > 10:
            warning_messages.append({
                'column': str(column),
                'message': 'has ' + str(value) + ' (' + str(percentage) + '%) missing values',
                'type': 'Missing values'
            })

    df_where_not_zero_count = df.astype(bool).sum().to_frame().transpose()
    for column in df_where_not_zero_count:
        zeros = total_row_count - df_where_not_zero_count[column][0]
        percentage = round((zeros / total_row_count) * 100, 2)
        if zeros > 0:
            warning_messages.append({
                'column': str(column),
                'message': 'has ' + str(zeros) + ' (' + str(percentage) + '%) zeros',
                'type': 'Zeros'
            })

    return warning_messages
