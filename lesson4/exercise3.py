def multiplies(first_number, second_number):
    if second_number == 0:
        return 0
    if second_number == 1:
        return first_number
    if second_number < 0:
        return -first_number + multiplies(first_number, second_number + 1)

    return first_number + multiplies(first_number, second_number - 1)


print(multiplies(3, 4))
print(multiplies(4, 0))
print(multiplies(3, -1))
print(multiplies(-3, 3))
print(multiplies(-3, -3))
