img = "#"
while True:
    square = input("How big a square would you like?")
    if square.upper() == "Q":
        print("Goodbye!")
        break
    if square == "":
        print("I do not understand, please repeat query.")
        continue
    for a in range(int(square)):
        line = img * int(square)
        print(line)
    for a in range(int(square)):
        line2 = img * (int(a)+1)
        print(line2)


