def print_squares(first_side, second_side, character):
    for first_index in range(first_side):
        print(character * second_side)


print_squares(2, 3, "&")
print_squares(4, 7, "#")


def sort_list_ascending(numeric_list):
    sorted_list = []

    while len(numeric_list) > 0:
        min_value_index = 0

        if len(numeric_list) > 1:
            for index in range(1, len(numeric_list)):
                if numeric_list[index] < numeric_list[min_value_index]:
                    min_value_index = index

        sorted_list.append(numeric_list[min_value_index])
        numeric_list.pop(min_value_index)

    return sorted_list


def sort_list_ascending_mutable(numeric_list):
    for first_index in range(len(numeric_list)):
        if len(numeric_list) > 1:
            min_value_index = first_index

            for second_index in range(first_index, len(numeric_list)):
                if numeric_list[second_index] < numeric_list[min_value_index]:
                    min_value_index = second_index

            if min_value_index != first_index:
                exchange_number(numeric_list, min_value_index, first_index)


def exchange_number(numeric_list, first_index, second_index):
    number = numeric_list[second_index]
    numeric_list[second_index] = numeric_list[first_index]
    numeric_list[first_index] = number


first_numbers_list = [1, 5, 3, 7]
second_numbers_list = [1, 5, 3, 7, 56, 78, 23, 45, 1290, 2, 6]

print(sort_list_ascending(first_numbers_list))
print(sort_list_ascending(second_numbers_list))

first_numbers_list = [1, 5, 3, 7]
second_numbers_list = [1, 5, 3, 7, 56, 78, 23, 45, 1290, 2, 6]

sort_list_ascending_mutable(first_numbers_list)
sort_list_ascending_mutable(second_numbers_list)

print(first_numbers_list)
print(second_numbers_list)
