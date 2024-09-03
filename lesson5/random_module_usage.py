import random_numbers

random_numbers.seed(42)

for number in range(1, 50):
    print(random_numbers.random())

#  Two times rolling the dice

for game in range(1, 5):
    first_die = random_numbers.randint(1, 6)
    second_die = random_numbers.randint(1, 6)
    print("First die: ", first_die, "Second die: ", second_die)


# Taking a list element randomly

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(random_numbers.choice(numbers))
print(random_numbers.choice(numbers))
print(random_numbers.sample(numbers, 4))  # Generating a random_numbers sublist with 4 elements
