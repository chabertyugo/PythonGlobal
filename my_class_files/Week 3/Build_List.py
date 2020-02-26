inp = ""
my_list = []

while True:
    inp = input("Please enter a number. When done, press q.")
    if inp.upper() == "Q":
        print("Goodbye!")
        break
    my_list.append(int(inp))
sum = 0
for a in my_list:
    sum += a
print("The sum of your list is " + str(sum)+ ".")
print (int(sum)/len(my_list))