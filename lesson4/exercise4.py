def generates_multiplier_grid():
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid number")
        return None

    return [value * number for value in range(1, 11)]


print(generates_multiplier_grid())
