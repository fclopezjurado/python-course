first_boolean = not (False or True)  # False
second_boolean = not ((False or True) and (False and False))  # True
third_boolean = (False or True) and (not (False and False))  # True

print(first_boolean)
print(second_boolean)
print(third_boolean)
