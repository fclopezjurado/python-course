import math

__doc__ = """Custom math module"""
__author__ = "Fran López"
__version__ = "1.0"


def square_root(first_number, second_number, third_number):
    root = second_number ** 2 - 4 * first_number * third_number

    if root < 0:
        print("Complex square roots")
        first_root = complex(-second_number, math.sqrt(-root) / 2)
        second_root = complex(-second_number, - math.sqrt(-root) / 2)

        if second_number == 0:
            print("Pure imaginary square roots")
            first_root = complex(0, first_root)
            second_root = complex(0, second_root)
    elif root > 0:
        print("Real negative square roots and imaginary parts")
        first_root = (-second_number + math.sqrt(root)) / 2
        second_root = (-second_number - math.sqrt(root)) / 2
    else:  # root == 0
        print("Double negative real square roots")
        first_root, second_root = -second_number / 2, -second_number / 2

    return first_root, second_root


if __name__ == "__main__":
    first_integer = int(input("Enter the first number: "))
    second_integer = int(input("Enter the second number: "))
    third_integer = int(input("Enter the third number: "))
    first_square_root, second_square_root = square_root(first_integer, second_integer, third_integer)
    print("( {} , {} )".format(first_square_root, second_square_root))
