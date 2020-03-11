import pandas as pd

# Setting panda options to format all floats from file to 2 decimal places.
pd.options.display.float_format = '{:.2f}'.format

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

# Use nrows to set rows to read. Parse_dates to prevent dates from being strings. infer_datetime_format guesses date
# type.

dataset = pd.read_csv("500000 Sales Records.csv", parse_dates=True, infer_datetime_format=True)

dataset.columns = dataset.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

# print(dataset)
# print(dataset.describe())
# print(dataset.describe(include=object))
#
# print(dataset.keys())
#
# print(dataset.columns)
#
# print(dataset.total_revenue.describe())
#
# print(dataset.unit_price.max())
# print(dataset.unit_price.min())
# print(dataset.unit_price.sum())
# print(int(dataset.unit_price.mean()))
#
# print(dataset.region.value_counts())
# print(dataset.region.unique())
#
# print(dataset.region.values)

print(dataset.groupby("region")["units_sold"].sum())
print(dataset.groupby("region")["units_sold"].sum()["Europe"])
print(dataset.groupby("region")["units_sold"].mean())
