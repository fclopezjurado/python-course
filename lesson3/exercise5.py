evens = []

[evens.append(value) for value in range(2, 101, 2)]

print(evens)

evens = []

[evens.append(value) for value in range(2, 101) if value % 2 == 0]

print(evens)
