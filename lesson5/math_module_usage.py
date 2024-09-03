import math
import cmath

from lesson5.a_module import square_root

float_number = 2. / 3.

print("Two divided by three: ", float_number)
print("Ceil: ", math.ceil(float_number))
print("Floor: ", math.floor(float_number))
print("Truncate: ", math.trunc(float_number))
print("Square root: ", math.sqrt(float_number))
print("Square: ", math.pow(float_number, 2))
print("Cube: ", math.pow(float_number, 3))

pi = math.pi
e = math.e
napierian_logarithm = math.log(e)
log_base_ten = math.log(10, 10)
exponential = math.exp(-0.5)
function = exponential * math.cos(2 * math.pi * 100 * 5)
infinite = math.inf
complex_square_root = cmath.sqrt(-1)

print("PI: ", pi)
print("E: ", e)
print("log(e): ", napierian_logarithm)
print("log base 10 of 10: ", log_base_ten)
print(infinite)
print(infinite + 100)
print(complex_square_root)

print(dir(math))  # List of functions and constants
