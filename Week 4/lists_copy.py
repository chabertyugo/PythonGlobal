
first_list = list(range(1,6))

second_list = first_list.copy()
third_list = first_list

print(first_list)
print(second_list)

second_list[2] = 99

print(first_list)
print(second_list)

mylist3 = []

for val in second_list:
    mylist3.append(val)

print (mylist3)

print(first_list == second_list) # FALSE
print(first_list == third_list)  # TRUE
