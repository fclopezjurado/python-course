option = "a"

if option == "a":
    print("You chose 'a'")
elif option == "b":
    print("You chose 'b'")
elif option == "c":
    print("You chose 'c'")

# ######################

numeric_set = set()

for value in range(0, 10):
    input_number = int(input("Enter a number: "))
    numeric_set.add(input_number)

print(list(numeric_set))

# ######################

numeric_set = set()

for value in range(0, 10):
    input_number = int(input("Enter a number: "))
    numeric_set.add(input_number)

numeric_list = list(numeric_set)

numeric_list.sort(reverse=True)
print(numeric_list)
