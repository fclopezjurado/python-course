def printSquare(number):
    print("The square of number {} is: {}".format(number, number ** 2))


def printCube(number):
    print("The cube of number {} is: {}".format(number, number ** 3))


def printFourthPower(number):
    print("The fourth power of number {} is: {}".format(number, number ** 4))


try:
    float_number = float(input("Enter a float number: "))
except ValueError:
    print("Please enter a valid float number")
    exit()

print("1. Calculate square")
print("2. Calculate cube")
print("3. Calculate fourth power")

try:
    operation = int(input("Enter an operation number: "))
except ValueError:
    print("Please enter a valid number (1-4)")
    exit()

if operation < 1 or operation > 3:
    print("Please enter a valid operation number (1-3)")
    exit()

switch = {2: printSquare, 3: printCube, 4: printFourthPower}

switch.get(operation)(float_number)
