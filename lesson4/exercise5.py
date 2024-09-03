numeric_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(max(numeric_list))


def get_max_value(numbers):
    if len(numbers) == 0:
        return None

    max_value = numbers[0]
    del numbers[0]

    for number in numbers:
        if number > max_value:
            max_value = number

    return max_value


print(get_max_value([1, 2, 3, 5, 6, 23, 7, 8]))
