import pandas as pd
import sys
import logging
import matplotlib.pyplot as plt

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

# Formatting to remove spaces and parentheses and set all headers to lower case.
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

# Here we define our 4 functions. To call functions from other file would require 2 .py submissions to moodle (not
# possible) and for the functions to include reading the csv file independently (unacceptable).


def country_profit(country: str):
    # Simple function that returns a rounded value for the total profit of requested country.
    return print("The total profit is: $" + '{:.2f}'.format(df.groupby("country")["total_profit"].sum()[country]))


def region_profit(region: str):
    # Simple function that returns a rounded value for the total profit of requested region.
    return print("The total profit is: $" + '{:.2f}'.format(df.groupby("region")["total_profit"].sum()[region]))


def bar_chart():
    # Use groupby to select data in question.
    a = df.groupby("region").sum()["total_profit"]
    # Plotting bar chart with appropriate x and y labels.
    a.plot(kind="bar", x="region", y="total_profit")
    # Set title and specify x and y labels.
    plt.title("Total profits per region.", fontsize = 16)
    plt.xlabel("Region name", fontsize = 12)
    plt.ylabel("Total profits ($)", fontsize = 12)
    # Ultimately the function returns the plot itself.
    return plt.show()


def pie_chart():
    # Use groupby to select data in question.
    a = df.groupby("region").sum()["total_profit"]
    # Plotting pie chart, remove labels to show in legend and show wedge proportion to 2 decimal places.
    a.plot(kind="pie", labels=['','','','','','',''], autopct = '%.2f')
    # Set title.
    plt.title("Percentage of total profits by regions.", fontsize = 14)
    # Plot the legend in another subplot and format to the side.
    plt.legend(loc = "center right", labels = sorted(df.region.unique()), bbox_to_anchor=(1,0.5), fontsize=10,
               bbox_transform=plt.gcf().transFigure)
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.45)
    # Ultimately the function returns the plot itself.
    return plt.show()


# Defining our menu as a function with refining criteria.
def menu():
    # Start with interface dialogue.
    print("Welcome to Data analysis tools. \nSelect from one of the following options: \n1) Total profit based on a "
          "country. \n2) Total profit based on a region. \n3) Bar chart for total profit per region. \n4) Pie chart "
          "for total profit in each region. \n5) Exit. ")
    choice = input()
    try:
        # Using try command to set appropriate response to matching choice.
        if choice == "1":
            # Call function 1.
            print(country_profit(input("Please enter a country.")))
            return menu()
        if choice == "2":
            # Call function 2.
            print(region_profit(input("Please enter a region.")))
            return menu()
        if choice == "3":
            # Call function 3.
            print(bar_chart())
            return menu()
        if choice == "4":
            # Call function 4.
            print(pie_chart())
            return menu()
        if choice == "5":
            # Set input choice of 5 as exit.
            print("Thank you for your time.")
            return sys.exit("Shutting down.")
        if choice < 1 or choice > 5:
            # Too small or large a value will prompt a re-entry of value.
            print("A numerical value between 1 and 5 is required. Please try again.")
            return menu()
    except TypeError:
        # Separate error catch if user has entered a string.
        print("The value entered must be an integer value!")
        return menu()
    except Exception as e:
        # Catch all errors.
        logging.exception(e)
        print("An unhandled error has occurred, logging and returning to menu.")
        return menu()


# Once all is set, we must simply call the menu function.
menu()


