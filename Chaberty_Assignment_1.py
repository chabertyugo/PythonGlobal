# Import commands for csv reading and time reading.
import csv
import datetime
# Define now variable to show current time upon call.
now = datetime.datetime.now()
# Define empty dictionaries first.
d_regions = {}
d_region_units = {}
d_region_revenue = {}
# Define empty lists next.
regions_from_keys = []
# Define 'iteration' variables.
current_region = ""
current_units = 0
current_revenue = 0
# Setting up the first interface lines.
# Tried using the os.get_terminal_size but failed as this is not running in terminal.
# Ended up assigning variables to phrases and using Python 3.6 alignment formatting. This isn't truly centered but
# proves to be definitely cleaner.
report = "Sales Report"
print(f"{report:^80}")
dash = "------------"
print(f"{dash:^80}")
# Aligning and calling time function.
log = "Produced on: " + now.strftime("%Y-%m-%d")
print(f"{log:^80}")
# We are now ready to actually start iterating through the csv file. Original name retained.
f = open("my_class_files/Week 9/500000 Sales Records.csv", 'rt')
reader = csv.reader(f)
# Skip the header line right away.
next(reader)
# Reading csv file row by row.
for row in reader:
    # Using 'iterating' variables.
    current_region = row[0]
    current_units = row[8]
    current_revenue = row[11]
    # We add the current units to a newly created region key in unit dictionary.
    if not current_region in d_region_units:
        d_region_units[current_region] = current_units
    # Otherwise we add the new unit value to the value currently assigned to region key.
    else:
        d_region_units[current_region] = int(d_region_units[current_region]) + int(current_units)
    # We add the current revenue to a newly created region key in revenue dictionary.
    if not current_region in d_region_revenue:
        d_region_revenue[current_region] = current_revenue
    # Otherwise we add the new revenue value to the value currently assigned to region key.
    else:
        # Every time we add 2 float values, we round to 2 decimal places.
        # This ensures we never end up with a round up when it should actually round down and vice versa due to float.
        d_region_revenue[current_region] = round(float(d_region_revenue[current_region]) + float(current_revenue), 2)

# Begin by printing every region analyzed and total.
regions_from_keys = d_region_units.keys()
print("Regions analyzed: ", end="")
# Use for loop with index limit to print all regions on same line that ends with full stop.
for i in list(regions_from_keys):
    if list(regions_from_keys).index(i)<6:
        print(i, end=", ")
    else:
        print(i, end=".")
print()
# Print total by using length function.
print("Total, "+str(len(regions_from_keys))+" regions.")
print()
# Once again using Python 3.6 formatting for alignment purposes.
left_1 = "Total units sold:"
left_2 = "Average revenue per unit:"
left_3 = "Total revenue:"
for i in list(regions_from_keys):
    # Defining variables which constitute our results. Each is technically a function of the index called.
    center_1 = d_region_units[i]
    # Making sure to round the floats again.
    center_2 = "$" + str(round(d_region_revenue[i] / d_region_units[i], 2))
    center_3 = "$" + str(d_region_revenue[i])
    # Using cheeky if statement to format units sold in N.A. They are the only ones described with 8 digits.
    if list(regions_from_keys).index(i) < 6:
        print(i)
        print()
        print(f"{left_1:<14}{center_1:^50}")
        print(f"{left_2:<15}{center_2:^32}")
        print(f"{left_3:<15}{center_3:^60}")
        print()
    else:
        print(i)
        print()
        print(f"{left_1:<14}{center_1:^49}")
        print(f"{left_2:<15}{center_2:^32}")
        print(f"{left_3:<15}{center_3:^60}")
        print()

# Defining new variables for our grand totals.
total_units = sum(d_region_units.values())
total_revenue = sum(d_region_revenue.values())
total_revenue_per_unit = round((total_revenue/total_units), 2)

print("Grand Totals")
print()
# Using alignment.
center_5 = "$" + str(total_revenue_per_unit)
center_6 = "$" + str(total_revenue)
print(f"{left_1:<14}{total_units:^50}")
print(f"{left_2:<15}{center_5:^32}")
print(f"{left_3:<15}{center_6:^60}")


#print(list(regions_from_keys))
#print(d_region_units)
#print(d_region_revenue)