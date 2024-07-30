import sys
import exercise1

perfect_numbers = []

for number in range(1, sys.maxsize):
    if exercise1.is_perfect_number(number):
        perfect_numbers.append(number)
    if len(perfect_numbers) == 4:
        break

print(perfect_numbers)
