numeric_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(min(numeric_list))


def get_max_and_min_values(numbers):
    if len(numbers) == 0:
        return None

    max_value = numbers[0]
    min_value = max_value

    del numbers[0]

    for number in numbers:
        if number > max_value:
            max_value = number
        if number < min_value:
            min_value = number

    return [min_value, max_value]


print(get_max_and_min_values([1, 2, 3, 5, 6, 23, 7, 8]))
