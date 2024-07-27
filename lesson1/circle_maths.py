import math

CIRCLE_RADIUS_QUESTION = "Enter the circle radius: "

# circle radius
circle_radius = float(input(CIRCLE_RADIUS_QUESTION))
circumference_length = math.pi * 2 * circle_radius
circle_area = math.pi * circle_radius ** 2

print(circumference_length)
print(circle_area)
