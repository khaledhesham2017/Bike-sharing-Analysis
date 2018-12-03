import pandas as pd


filename = "Data/bike-sharing.csv"
data = pd.read_csv(filename)

print(data.info())
