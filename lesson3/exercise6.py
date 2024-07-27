dictionary = []

for first_side in range(1, 101):
    for second_side in range(1, 101):
        for hypotenuse in range(1, 101):
            if first_side**2 + second_side**2 == hypotenuse**2:
                dictionary.append({(first_side, second_side): hypotenuse})

print(dictionary)
