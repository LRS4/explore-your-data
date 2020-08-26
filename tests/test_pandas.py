""" testing for pandas data manipulations """

import os
import pytest
import numpy as np
import pandas as pd

# Basics
df = pd.read_csv('tests/titanic.csv')
describe_numeric = df.describe()
describe_non_numeric = df.describe(include=['object', 'bool'])
shape = df.shape
information = df.info()
columns = df.columns
value_counts = df.value_counts('Pclass')
unique_values = df.nunique()
null_values = df.isnull()
fill_age_missing_values = df['Age'].fillna(df['Age'].median())
sort_by_fare = df.sort_values(by='Fare', ascending=False)
replace_values = df['Sex'].replace(
    to_replace=['male', 'female'], value=['Male', 'Female'])
transpose_df = df.transpose()

# Aggregations
survivors_by_class = df.groupby(by='Pclass')['Survived']
survivor_statistics = df.groupby(by='Survived')[['Pclass', 'Fare', 'Age']].agg([
    np.mean, np.std, np.min, np.max])
young_passengers = df[df['Age'] < 10]
lower_class_passengers = df[df['Pclass'].isin([2, 3])]
adult_names = df.loc[df['Age'] > 35, ['Name', 'Age']]
pivot_by_sex = df.pivot_table(
    values=['Survived', 'Age', 'Fare'], index=['Sex'], aggfunc='mean')
crosstab_by_class = pd.crosstab(index=df['Survived'], columns=df['Pclass'])


def join_two_dataframes(df):
    town_df = pd.DataFrame(df[['PassengerId']])
    town_df['EmbarkedTown'] = df['Embarked'].fillna('S').map(
        {'S': 'Southampton', 'C': 'Cherbourg', 'Q': 'Queenstown'}
    )
    return df.merge(town_df, on=['PassengerId'])


def vertical_concat_two_dataframes(df):
    return pd.concat([df, df], axis=0)


def get_survivors_by_age(df):
    df['AgeBins'] = pd.cut(
        x=df['Age'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80])
    return df.groupby('AgeBins')['Survived']


def map_new_values(df):
    keys = {3: 'Lower class', 2: 'Middle class', 1: 'Upper class'}
    df['ClassName'] = df['Pclass'].map(keys)
    return df


def loop_over_row_get_names(df):
    dictionary = {}
    for i, row in df.iterrows():
        print(f"{i} : {row['Name']}")
