string = "Hello, World!"
numeric_tuple = (1, 2, 3, 4, 5)
mixed_list = [1, 2, "3", 4, 5]
dictionary = {"first_key": 345, "second_key": True, "third_key": [1, 2, 3], "fourth_key": 340}
numeric_set = {2, 2, 4, 5, 7, 7, 8, 9, 12}

[print(char) for char in string]
[print(number) for number in numeric_tuple]
[print(element) for element in mixed_list]
[print(key, value) for key, value in dictionary.items()]
[print(key) for key in dictionary.keys()]
[print(value) for value in dictionary.values()]

print(mixed_list[:3])
print(mixed_list[3:])
print(mixed_list[1:4])
print(numeric_set)
print(str(2.24))

age = int(input("Enter your age: "))
year = int(input("Enter the current year: "))

# numeric_tuple[2] = 34
# string[1] = "r"
