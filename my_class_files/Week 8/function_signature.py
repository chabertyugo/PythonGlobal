# Implicit signature.
def addintegers(n: int, m: int):
    return n + m


# Explicit signature.
def sayhello(first: str,last:str="-name unknown-"):
    return "Hello, " + first + ", " + last + "."

print(sayhello("Ugo",))