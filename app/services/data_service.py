import numpy as np
import pandas as pd 
import json

def get_titanic_data() -> list:
    url = "https://gist.githubusercontent.com/michhar/2dfd2de0d4f8727f873422c5d959fff5/raw/fa71405126017e6a37bea592440b4bee94bf7b9e/titanic.csv"
    df = pd.read_csv(url)
    return df.to_json()
