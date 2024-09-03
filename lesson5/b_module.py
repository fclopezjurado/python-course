import a_module

document = a_module.__doc__
print(document)
print(a_module.__author__)
print(a_module.__version__)

first_number, second_number = a_module.square_root(2, 4, 6)
print(first_number, second_number)
