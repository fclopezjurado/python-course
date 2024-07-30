def print_string(string):
    print(string)


print_string("Hello, World!")


# ######################

def first_procedure():
    def print_numbers(first_number, second_number):
        print(first_number, second_number)

    print_numbers(2, 3)
    print_numbers(4, 5)


first_procedure()


# ######################

def add_one_to_integer(integer):
    print(integer)
    integer += 1


number = 5

add_one_to_integer(number)
print(number)

# ######################

numeric_list = [1, 2, 3, 4, 5]


def add_one_to_list_elements(list_with_numbers):
    for key in range(0, len(list_with_numbers)):
        list_with_numbers[key] += 1


add_one_to_list_elements(numeric_list)
print(numeric_list)

# ######################

alphabetical_list = ["a", "b", "c", "d", "e"]


def search_char(searchable_list, char):
    for element in searchable_list:
        if element == char:
            return True
    return False


print(search_char(alphabetical_list, "c"))

# ######################

dictionary = {"first_key": 1, "second_key": 2, "third_key": 3}


def search_key_in_dictionary(searchable_dictionary, key):
    for element_key in searchable_dictionary:
        if element_key == key:
            return True
    return False


def search_value_in_dictionary(searchable_dictionary, value):
    for element_value in searchable_dictionary.values():
        if element_value == value:
            return True
    return False


print(search_key_in_dictionary(dictionary, "second_key"))
print(search_key_in_dictionary(dictionary, "fourth_key"))
print(search_value_in_dictionary(dictionary, 3))
print(search_value_in_dictionary(dictionary, 7))

# ######################

result = 5


def add_two_numbers(first_number, second_number):
    global result
    result = first_number + second_number


add_two_numbers(3, 4)
print(result)


# ######################

def chained_functions(first_number, second_number):
    first_number -= 1
    second_number += 2
    print(first_number, second_number)

    def decrement_numbers(third_number, fourth_number):
        third_number -= 1
        fourth_number -= 1
        print(third_number, fourth_number)

        def increment_numbers(fifth_number, sixth_number):
            fifth_number += 1
            sixth_number += 1
            print(fifth_number, sixth_number)

        increment_numbers(third_number, fourth_number)

    decrement_numbers(first_number, second_number)


number_four = 4
number_eight = 8

chained_functions(number_four, number_eight)
print(number_four, number_eight)

# ######################

seed = 3.89


def random_number(first_number, second_number, operation_seed):
    quotient = first_number // second_number
    remainder = second_number % first_number
    random_quotient = first_number * (operation_seed % quotient) - remainder * (operation_seed // quotient)

    if random_quotient < 0:
        operation_seed = random_quotient
    else:
        operation_seed = random_quotient + second_number

    return operation_seed / second_number


print(random_number(8, 4, seed))


# ######################

def factorial(integer):
    if integer < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if integer < 2:
        return 1

    return integer * factorial(integer - 1)


print(factorial(3))

try:
    print(factorial(-5))
except ValueError as error:
    print(error)

# ######################

try:
    print(5 / 0)
except ZeroDivisionError:
    print("Division by zero is not allowed")
else:
    print("Division was successful")

# ArithmeticError when there is an error in arithmetic operation
# FloatingPointError when there is an error in floating point operation
# OverflowError when the result of an arithmetic operation is too large to be represented
# ZeroDivisionError when the second argument of a division or modulo operation is zero
# IndexError when a sequence subscript is out of range
# KeyError when a key is not found in a dictionary
# NameError when a local or global name is not found

# ######################
