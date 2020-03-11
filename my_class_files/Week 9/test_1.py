import pandas as pd

dataset = pd.read_csv("500000 Sales Records.csv", parse_dates=True, infer_datetime_format=True)

print(dataset)