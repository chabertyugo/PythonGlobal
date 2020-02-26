
# while True:
#
#     input_number = input("Enter a number >")
#
#     result = int(input_number) % 2
#
#     print("The number is ", end="")
#
#     if result == 0:
#         print("Even")
#     else:
#         print("Odd")
#
#     confirmation = input("Would you like to continue?  y/n >")
#
#     if confirmation == "n":
#         break

confirmation = "y"

while confirmation == "y":

    input_number = input("Enter a number >")

    result = int(input_number) % 2

    print("The number is ", end="")

    if result == 0:
        print("Even")
    else:
        print("Odd")

    confirmation = input("Would you like to continue?  y/n >")
