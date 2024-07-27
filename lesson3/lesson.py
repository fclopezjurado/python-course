number = 3

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# ######################

number = 4

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# ######################

input_number = int(input("Enter a number: "))

if input_number > 0:
    print("Positive")
    if input_number % 2 == 0:
        print("Even")
        if input_number > 100:
            print("Bigger than 100")
        else:
            print("Smaller than 100")
    else:
        print("Odd")
        if input_number > 100:
            print("Bigger than 100")
        else:
            print("Smaller than 100")

# ######################

index = 0

while index < 10:
    index += 1
    print(index, index ** 2, index ** 3)

# ######################

multiplying = 3
multiplier = 4
product = 0
index = 0

while index < multiplier:
    product += multiplying
    index += 1

print(product)

# ######################

input_number = int(input("Enter a number: "))
factorial = 1
index = 1

if input_number > 0:
    while index <= input_number:
        factorial *= index
        index += 1

print(factorial)

# ######################

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

for number in numbers:
    if number % 2 == 0:
        break
    print(number)

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)
else:
    print("Iteration finished")

# ######################

fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("Apple is in the list")

more_fruits = ["date", "elderberry"]

for fruit in more_fruits:
    fruits.append(fruit)

print(fruits)

# ######################

number = 5
dictionary = {}

for index in range(1, number + 1):
    dictionary[index] = index ** 2

dictionary.update({10: 100})

print(dictionary)

# ######################

keys = ["a", "b", "c"]
values = [1, 2, 3]
dictionary = dict(zip(keys, values))

print(dictionary)

# ######################

dictionary = {"first": {"a": "first", "b": "second"}, "second": {"c": "first", "d": "second"}}

for key in dictionary:
    print(key)
    for sub_key in dictionary[key]:
        print(sub_key, ":", dictionary[key][sub_key])

# ######################

currencies = ["€", "$", "£"]
input_currency = str(input("Enter an input currency (€, $, £): "))
amount = float(input("Enter an amount: "))
output_currency = str(input("Enter an output currency (€, $, £): "))
exchange_index = {"€$": 1.2, "€£": 0.9, "$€": 0.8, "$£": 0.7, "£€": 1.1, "£$": 1.4}
exchange = exchange_index[input_currency + output_currency] * amount

print(str(exchange) + output_currency)
