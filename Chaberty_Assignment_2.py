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



