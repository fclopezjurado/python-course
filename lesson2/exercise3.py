numeric_list = [16, 28, 5, 37, 22, 33]

print(len(numeric_list))
print(type(numeric_list))

numeric_list.append(30)
print(numeric_list)

numeric_list.sort()
print(numeric_list)

numeric_list.reverse()
print(numeric_list)

print(numeric_list.index(28))
print(numeric_list[3:5])
print(numeric_list[:3])
print(numeric_list[3:])
print(numeric_list[-2:])
