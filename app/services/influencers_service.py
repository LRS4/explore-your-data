import numpy as np
import pandas as pd
from operator import itemgetter
from pandas.api.types import is_numeric_dtype
import matplotlib.pyplot as plt
import seaborn as sns
import json


def get_target_base_frequency(df, target_column, target_value, debug=False):
    base_frequencies = df[target_column].value_counts(normalize=True)
    target_base_frequency = base_frequencies[target_value]
    
    if debug:
        print(f'Baseline {target_column} ({target_value}) frequency: ', end="")
        print(str(round(target_base_frequency, 2)))

    return target_base_frequency


def drop_columns_with_missing_over(percent, df):
    """
    Removes columns where the percent of missing rows is over the given value.
    """

    limit = len(df) * percent

    return df.dropna(thresh=limit, axis=1)


def bin_continuous_cols(df, target_column, bins=10, debug=False):
    """ 
    Splits the continuous variables into bins of the given size. 
    Has a check to exclude columns with high cardinality (nunique).
    """

    for column in df:
        if debug:
            print(column)
            print(df[column].nunique())
            print(is_numeric_dtype(df[column]), end="\n---\n\n")

        if column != target_column:
            if df[column].nunique() > 15 and is_numeric_dtype(df[column]):
                df[column] = pd.cut(
                    df[column].copy(),
                    bins=bins,
                    precision=0)

                if debug:
                    print(df[column].value_counts())

    return df


def populate_crosstab(df, column, target_column, target_value, show_as_percentages=False):
    """ 
    Creates a pandas crosstab using two given column names, one being the target.
    """

    crosstab = pd.crosstab(
        index=df[column],
        columns=df[target_column],
        normalize='index' if show_as_percentages else False)

    crosstab = crosstab.sort_values(target_value, ascending=False)
    target_base_frequency = get_target_base_frequency(
        df, target_column, target_value)

    return crosstab[crosstab[target_value] > target_base_frequency + 0.05]


def populate_crosstab_json(crosstab, parent_column_name, target_column, target_value, debug=False):
    """
    Returns influencers in json format given a crosstab dataframe.

    Limits the returned list by slicing the first two each time called. 
    This can be adjusted to return more influencers per crosstab passed.
    """

    response = []

    for column_name in crosstab:
        if column_name == target_value:
            series = crosstab[column_name]
            for index, value in series.items():

                if debug == True:
                    print(f'Where {parent_column_name} was {index}', end="\n")
                    print(f"{round(value * 100, 2)}% had '{target_column}' value of {column_name}",
                          end="\n---\n\n")

                response.append({
                    'parent_column_name': parent_column_name,
                    'index': str(index),
                    'value': round(value * 100, 2),
                    'target_column': target_column,
                    'target_value': column_name
                })

    return response[:3]


def flatten_list(two_d_list: list):
    return [item for sublist in two_d_list for item in sublist]


def get_classification_influencers(target_column, target_value, df, debug=False):
    """
    Finds influencers for classification target 
    """

    influencers = []

    for column in df:
        if column != target_column and df[column].nunique() < 20:
            xy = df[[column, target_column]]

            crosstab = populate_crosstab(
                xy,
                column,
                target_column,
                target_value,
                show_as_percentages=True)

            if debug == True:
                print(f"{column} length: {len(df[column])}", end="\n")
                print(crosstab, end='\n---\n\n')

            influencers.append(populate_crosstab_json(crosstab,
                                                      column,
                                                      target_column,
                                                      target_value,
                                                      debug=False))

    influencers = flatten_list(influencers)

    return sorted(influencers, key=lambda k: k['value'], reverse=True)


def populate_regression_json(df, column, target_column, target_mean, inc_or_dec, debug=False):
    """
    Returns influencers in json format given a grouped by dataframe.

    Limits the returned list by slicing the first three each time called. 
    This can be adjusted to return more influencers per features passed.
    """

    response = []
    for column_name in df:
        for index, value in df[column_name].items():

            if debug == True:
                print(f'Where {column} was {index}', end="\n")
                print(f"'{target_column}' had an average value of {round(value, 2)}",
                      end="\n")
                print(f"This was a {round(value - target_mean, 2)} {inc_or_dec} from the baseline average.",
                      end="\n---\n\n")

            response.append({
                'parent_column_name': column,
                'index': str(index),
                'value': round(value, 2),
                'target_column': target_column,
                'target_value': inc_or_dec,
                'difference_from_baseline_avg': round(value - target_mean, 2)
            })

    return response[:2]


def get_regression_influencers(target_column, inc_or_dec, df):
    """
    Finds influencers for regression target. Uses the target mean +/- 20%
    as a starting point at which to benchmark segment comparisons.

    Passing 'increase' or 'decrease' determines whether the algorithm is 
    looking for what makes the target increase or what makes the target 
    decrease against the base average.
    """

    influencers = []
    target_mean = df[target_column].mean()
    ascending = False if inc_or_dec == 'increase' else True

    for column in df:
        if column != target_column:
            grouped = df[[column, target_column]].groupby(column).mean()
            grouped = grouped.sort_values(target_column,
                                          ascending=ascending)

            if inc_or_dec == 'increase':
                grouped = grouped[grouped > target_mean +
                                  (target_mean * 0.2)].dropna()
            else:
                grouped = grouped[grouped < target_mean -
                                  (target_mean * 0.2)].dropna()

            influencers.append(populate_regression_json(grouped,
                                                        column,
                                                        target_column,
                                                        target_mean,
                                                        inc_or_dec,
                                                        debug=False))
    influencers = flatten_list(influencers)

    return sorted(influencers, key=lambda k: k['value'], reverse=not ascending)


def find_key_influencers(target_column, target_value, df, method):
    """
    Calculates and finds key influencers for the target column (variable).
    Returns influencers in json format.

    For regression problems, either 'increase' or 'decrease' must be passed 
    as the target value, to find either influencers which make the target 
    increase or decrease.

    Example usage:
        find_key_influencers(target_column='Survived', 1,  df=data, method='classification')
        find_key_influencers(target_column='Survived', 'increase', df=data, method='regression')
    """

    print('Finding key influencers...', end="\n\n")

    df = drop_columns_with_missing_over(0.5, df)
    df = bin_continuous_cols(df, target_column, debug=False)

    if method == 'classification':
        return get_classification_influencers(target_column, target_value, df, debug=False)
    elif method == 'regression':
        return get_regression_influencers(target_column, target_value, df)
    else:
        return print("Must provide either 'classification' or 'regression' for method.")


def generate_influencer_plot(df, feature, target_column, base_mean, actuals=False):
    """ 
    Returns a plot of the relationship between a feature and the target from the 
    given DataFrame. This is generally a count plot of absolute values or percentages
    for the individual 'segments' of the feature. 

    The base mean will be added to an horizontal line to visualise which segments 
    were above average for the current feature segment. 

    Example usage:
        generate_influencer_plot(df, 'Sex', 'Survived', base_mean=0.38, actuals=False)
    """
    plot = sns.barplot(data=df,
                       x=feature,
                       y=target_column,
                       palette="Blues")

    plot.axhline(base_mean, ls='--', label='Average')
    plt.legend()

    return plot
