fibonacci = [0, 1]

for index in range(2, 20):
    fibonacci.append(fibonacci[index - 1] + fibonacci[index - 2])

print(fibonacci)
