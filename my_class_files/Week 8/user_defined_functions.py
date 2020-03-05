# Define python user-defined exceptions.
class Error(Exception):
    pass


class ValueTooSmallError(Error):
    pass


num = int(input("Enter a number here."))
try:
    if num < 0:
        raise ValueTooSmallError
except ValueTooSmallError:
    print("You reached this because the value was too small!")
except Exception as e:
    print("An unhandled error has occurred.") + str(e)
else:
    print("Large enough...")
