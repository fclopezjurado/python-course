import numpy
import matplotlib.pyplot
from sympy.physics.quantum.circuitplot import pyplot

array = numpy.array([10, 20, 30, 40, 50]) # create array with 5 integers
matrix1 = numpy.matrix('10, 20, 40; 40, 50, 60; 70, 80, 90') # creates matrix with 3 rows and 3 columns
matrix2 = numpy.matrix(([1, 2, 3], [4, 5, 6], [7, 8, 9])) # creates matrix with 3 rows and 3 columns
matrix3 = numpy.matrix([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).reshape(4, 3) # creates matrix with 4 rows and 3 columns

print(array)
print()
print(matrix1)
print()
print(matrix2)
print()
print(matrix1 + matrix2)
print()
print(matrix3)
print()
print(matrix3 * 2)
print()

lineal_array_1 = numpy.arange(0, 10, 0.5) # Array with values from 0 to 9 with step 0.5
lineal_array_2 = numpy.linspace(0, 10, 25) # Array with 25 equidistant points from 0 to 10

print(lineal_array_1)
print()
print(lineal_array_2)

lineal_array_3 = numpy.linspace(-4, 8, 50)
y1_function = lineal_array_3 ** 3 - 6 * lineal_array_3 ** 2 - 5 * lineal_array_3 + 6
y2_function = 0 * lineal_array_3

pyplot.plot(lineal_array_3, y1_function, 'b-', lineal_array_3, y2_function, 'g-')
pyplot.title('Third grade polynomial')
pyplot.xlabel('x-axis')
pyplot.ylabel('y-axis')
pyplot.show()
