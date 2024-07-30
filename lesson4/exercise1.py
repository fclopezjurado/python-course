import sys


def is_perfect_number(number):
    if number > sys.maxsize or number < 2:
        return False

    accumulator = 0

    for integer in range(1, number):
        if number % integer == 0:
            accumulator += integer

    if accumulator == number:
        return True

    return False
