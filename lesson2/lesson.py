value = 20
first, second, third = 3, 3, 5
float1 = 2.0 / 3.0
float2 = 2.000000000000000000001 / 3.0
valid = True
invalid = False
char = u'A'
a_char = chr(65)
charNumber = ord(char)
fourth = 7.2
fifth = 3.4
seven = 7
three = 3
real_number = 4.78945646
complex_number = 5.3 + 2.6j
large_string = """This is a large string
that spans multiple lines
and contains a lot of text"""
filepath = 'C:\\Users\\user\\Desktop\\file.txt'
small_string = u'La Pe\xf1a'
medium_string = 'This is a medium string'
numeric_tuple = (7, 78, 45)
first_int, second_int, third_int = numeric_tuple
week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
furniture_set = {'chair', 'table', 'closet', 'bed'}
first_range = range(0, 10)
second_range = range(0, 10, 2)
first_list = [element ** 2 for element in first_range]
mixed_list = ['Anthony', 1, 54, 'Rudolf', 3, 23]
numeric_list = list(first_range)

print(type(value))  # data type of "value" variable
print(first == second)
print(first == third)
print(first != third)
print(float1)
print(float2)
print(float1 == float2)
print(valid)
print(invalid)

print(bool(1))
print(bool())
print(bool(-1))
print(bool('test'))
print(bool(15))

print(char)
print(a_char)
print(charNumber)
print('a' < 'b')

print(fourth // fifth)
print(seven // three)
print(type(fourth // fifth))
print(type(seven // three))
print(1 / 3 == 0.33333333)
print(round(real_number, 2))  # round a number

print(complex_number, complex_number.imag, complex_number.real, type(complex_number))
print(float(2))  # converts to a float
print(int(2.5))  # converts to an int
print(str(4789))  # converts to a string
print(bin(34123421))  # converts to a binary number
print(oct(567))  # converts to an octal number
print(hex(1234))  # converts to a hexadecimal number
print(complex(2.7894))  # converts to a complex number

print(large_string)
print("""This is a large string \
that spans multiple lines \
and contains a lot of text""")  # string template with multiple lines
print("string with 'single quotes' inside")
print("string with \"double quotes\" inside")
print('string with \'single quotes\' inside')
print('string with "double quotes" inside')
print(filepath)
print(small_string)
print(small_string.encode('latin-1'))  # encodes a string
print('this string contains a double backslash \\.')
print(r'this string contains a single backslash \.')
print(large_string[-1])
print(large_string[:4])  # takes the first 5 elements of the string
print(large_string[3:7])  # takes all string chars from third to seventh position
print(large_string[7:])  # takes all string chars from seventh position to the last one
print(small_string + medium_string)
print(small_string * 2)
print('My first name is %s and my weight is %d' % ('John', 56))  # string template
print('Bank' > 'bank')  # string comparison
print(len(medium_string))  # string length
print('A\nB\nC\nD')
print('E\tF\tG\tH')
print('WX\bYZ')
print('1\a2\a3\a4\a5\a6')
print('I am {0} years old and I received {1} messages'.format(25, 5))  # string template

print(numeric_tuple)
print(first_int)
print(second_int)
print(third_int)
print(numeric_tuple.index(78))  # gets the index of "78" number in the tuple
print(numeric_tuple.count(45))
print('sofa' in furniture_set)  # evaluates if "sofa" string is in set
print('chair' in furniture_set)  # evaluates if "chair" string is in set
print(first_range)
print(second_range)
print(list(first_range))  # converts a range to a list

for index in first_range:  # prints range elements one by one
    print(index)

print(first_list)
print(mixed_list)
print(mixed_list[2])  # gives the third element in the list
print(len(mixed_list))  # gives the length of the list
print(mixed_list[2:4])  # gives all list elements from third place to fifth place
print(mixed_list[:4])  # gives the first four elements of the list
print(mixed_list[2:])  # gives all list elements except the first three

mixed_list.append('element')  # appends elements to a list
del mixed_list[1]  # deletes the second element of a list

print(mixed_list)
print(numeric_list)
print(sum(numeric_list))  # adds all elements of a list
print(mixed_list)
print(any(mixed_list))  # some of them are true
print(all(mixed_list))  # all of them are true
print(numeric_list.count(5))  # number of times 5 is in the list

numeric_list.extend([14, 15, 16])  # add a list of elements at the end of another list

print(numeric_list)
print(numeric_list.index(4))  # gives the element in fifth position

numeric_list.insert(2, 300)  # inserts 300 value in the third list position
numeric_list_element = numeric_list.pop(3)  # deletes a list element by index and returns it

print(numeric_list)
print(numeric_list_element)

numeric_list.sort()  # sorts the list in a degressive order
print(numeric_list)
numeric_list.reverse()  # sorts the list in reversed order

first_numeric_list = [2, 4, 5, 7]
second_numeric_list = [5, 8, 9, 12]
concatenaded_numeric_list = first_numeric_list + second_numeric_list

print(concatenaded_numeric_list)

first_dictionary = {"first_key": 345, "second_key": True, "third_key": [1, 2, 3], "fourth_key": 340}
print(first_dictionary, type(first_dictionary))

first_dictionary["fifth_key"] = 4 * 8  # adds a new key in a dictionary
print(first_dictionary)

del (first_dictionary["second_key"])
first_dictionary.update({"sixth_key": 67})  # updates the dictionary adding more key-value pairs
first_dictionary["seventh_key"] = "Pepe"  # adds a new key-value pair

print(first_dictionary)
print(first_dictionary.get("first_key"))  # gets the first dictionary element
print(first_dictionary.keys())  # gets all dictionary keys
print(first_dictionary.values())  # get all dictionary values
print(first_dictionary.items())  # gets all dictionary items

random_set = {34, "John", 57, True}
first_numeric_set = {1, 2, 1, 3, 4, 4, 5, 6, 3}
second_numeric_set = {1, 3, 3, 5, 7, 1}
set_intersection = first_numeric_set & second_numeric_set  # gives set intersection
set_unification = first_numeric_set | second_numeric_set  # gives set unification
set_difference = first_numeric_set - second_numeric_set  # gives set difference
set_symmetric_difference = first_numeric_set ^ second_numeric_set  # gives set symmetric difference

print(random_set)
print(set_intersection)
print(set_unification)
print(set_difference)
print(set_symmetric_difference)

name = input("Type your name: ")  # gives the standard input
integer = int(input("Type your favourite name (0, 10): "))  # converts the standard input to an integer
float_number = float(input("Type your favourite float (0, 10): "))  # converts the standard input to a float
boolean = bool(input("Type something to be converted to a boolean: "))  # converts the standard input to a boolean

print(name)
print(integer)
print(float_number)
print(boolean)
