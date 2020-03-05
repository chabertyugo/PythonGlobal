def deposit(amount: float):
    assert(amount > 0), "Sorry, the amount deposited must be greater than 0!"


value = input("Please, enter an amount to deposit.")
try:
    deposit(float(value))
except AssertionError as error_text:
    print(error_text)
except Exception as error_text:
    print("An unhandled error has occurred!")
else:
    print("If no error has occurred, run these lines!")
    # Send email of confirmation of deposit here.

# Exception command is the "catch-all" of errors. All 'try' commands should end with an 'except Exception', the user
# should never encounter an error message! (as in, from the console).
