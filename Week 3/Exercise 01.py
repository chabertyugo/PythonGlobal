value = ""
while True:
    value = input("Please enter a number.")
    if value.upper() == "Q":
        print("Goodbye!")
        break
    if int(value) % 10 != 0:
        print("This number is not a multiple of 10.")
    if int(value) % 10 == 0:
        print("This number is indeed a multiple of 10.")
