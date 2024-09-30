import numpy

integers = numpy.array([1, 2, 3, 4, 5])
reals = numpy.array([1.2, 2.3, 3.5, 4.7, 5.9])
booleans = numpy.array([True, False, True, False, True])
strings = numpy.array(['Anne', 'Peter', 'John'])
zeros = numpy.zeros((3, 5)) # Matrix with 3 rows and 5 columns of zeros
ones = numpy.ones((3, 5), dtype=numpy.int16) # Matrix with 3 rows and 5 columns of ones

print(integers)
print(integers.dtype)
print(reals)
print(reals.dtype)
print(booleans)
print(booleans.dtype)
print(strings)
print(strings.dtype)
print(zeros)
print(ones)

first_array = numpy.array([1, 2, 3, 4, 5])
second_array = numpy.array([5, 4, 3, 2, 1])
array_range = numpy.arange(10, 16, 2) # Array with values from 10 to 16 with step 2
random_matrix = numpy.arange(15).reshape(3, 5) # Matrix with 3 rows and 5 columns with values from 0 to 14

print(first_array + second_array)
print(first_array - second_array)
print(first_array * second_array)
print(first_array / second_array)
print(array_range)

print(random_matrix)
print(random_matrix.shape)
print(random_matrix.ndim)
print(random_matrix.dtype.name)
print(random_matrix.itemsize)
print(random_matrix.size)
print(type(random_matrix))
print(type(first_array))

lineal_space_array = numpy.linspace(0, 2, 9) # Array with 9 equidistant points from 0 to 2
numpy.random.seed(123) # Seed for random numbers
random_numbers_uniform_distribution = numpy.random.rand(10) # Array with 10 random numbers with uniform distribution
random_numbers_normal_distribution = numpy.random.randn(10) # Array with 10 random numbers with normal distribution
random_integers = numpy.random.randint(1, 100, 10) # Array with 10 random integers from 1 to 100

print(lineal_space_array)
print(random_numbers_uniform_distribution)
print(random_numbers_normal_distribution)
print(random_integers)

random_integers[random_integers % 2 == 0] = -1
first_matrix = numpy.array([[1, 2, 3], [4, 5, 6]])

print(random_integers)
print(first_matrix)
print(first_matrix.ndim)
print(first_matrix.shape)
print(len(first_matrix))

third_array = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sub_array = third_array[2:7] # Sub-array from index 2 to 6

print(third_array)
print(sub_array)
