import pandas as pd


def read_details(filename):
    data = pd.read_csv(filename)
    return data
