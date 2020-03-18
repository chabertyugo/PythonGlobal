import pandas as pd
import sys
import logging


# Setting panda options to format all floats from file to 2 decimal places.
pd.options.display.float_format = '{:.2f}'.format

try:
    # Reading csv and thus creating dataframe using panda.
    df = pd.read_csv("500000 Sales Records.csv", parse_dates=True, infer_datetime_format=True)
except FileNotFoundError:
    # Exiting and feeding error text if triggered.
    sys.exit("Sorry, an error has occurred: file not found. Exiting.")
except IOError:
    # Exiting and feeding error text if triggered.
    sys.exit("Sorry, an error has occurred; input/output error. Exiting.")
except Exception as e:
    # Logging, exiting and feeding error text if triggered.
    logging.exception(e)
    sys.exit("An unhandled error has occurred. Logging and exiting.")

# Formatting to remove spaces and parentheses and set all to lower case.
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

d_country_profits = {}
for index, row in df.iterrows():
    current_country = row[1]
    current_profits = row[12]
    if not current_country in d_country_profits:
        d_country_profits[current_country] = current_profits
    # Otherwise we add the new revenue value to the value currently assigned to region key.
    else:
        # Every time we add 2 float values, we round to 2 decimal places.
        # This ensures we never end up with a round up when it should actually round down and vice versa due to float.
        d_region_revenue[current_region] = round(float(d_region_revenue[current_region]) + float(current_revenue), 2)



# def profit_by_country(n: str):
#     return print(df.groupby("country")["total_profits"]



