import csv
d_region_units = {}
d_region_revenue = {}
l_regions = []

current_region = ""
current_units = 0
current_revenue = 0

f = open("region_input.csv", 'rt')
reader = csv.reader(f)
next(reader)
#read the input file
for row in reader:
    print(row) #checking purposes
    # Get the current value
    current_region = row[0]
    current_units = row[1]
    current_revenue = row[2]
    if not current_region in d_region_units:
        d_region_units[current_region] = current_units
    else:
        d_region_units[current_region] =  int(d_region_units[current_region]) + int(current_units)

print(d_region_units)

l_regions = d_region_units.keys()
print(l_regions)
#as opposed to
l_regions = list(d_region_units.keys())
print(l_regions)

print("All the regions found are: ", end="")
for r in l_regions:
    print(r, end="")
print()

print("TOTALS PER REGION")
for r in l_regions:
    print(r)
    print("Total units for region: " + str(d_region_units[r]))
    print()