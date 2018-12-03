import pandas as pd


def get_data(filename="Data/bike-sharing.csv"):
    data = pd.read_csv(filename)
    return data
