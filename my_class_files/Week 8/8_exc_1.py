value = input("Please enter an integer.")
try:
    num = int(value)
    print(num)
except Exception as e:
    print("An exception has occurred." + str(e))