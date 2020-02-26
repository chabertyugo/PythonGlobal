mylist = [4, 5, 10, 20, 10, 54, 22, 1, 20]
#Find min value.
#Find max value.
#Find duplicates.

min = mylist[0]
max = mylist[0]

for i in mylist:
    if i < min:
        min = i
print("The minimum value of the set is " + str(min) + ".")

for i in mylist:
    if i > max:
        max = i
print("The maximum value of the set is " + str(max) + ".")
print(min(mylist))