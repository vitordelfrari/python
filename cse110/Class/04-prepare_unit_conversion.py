fah_temp = float(input("What is the temperature in Fahrenheit?" ))
celcius_temp = (fah_temp - 32) * (5 / 9)

print(f"The temperature in Celsius is {celcius_temp:.1f} degrees.")

#"--------------------------"

#degrees_f = float(input("What is the temperature in Fahrenheit? "))
#degrees_c = (degrees_f - 32) * 5 / 9

#print(f"The temperature in Celsius is {degrees_c:.1f} degrees.")

# Note: I chose to abbreviate degrees_fahrenheit to degrees_f, because I decided
# that _f and _c were common, known abbreviations, and less likely to introduce
# bugs than if I tried to spell out "fahrenheit" in my code each time. But even
# in that case, I thought "degrees_f" seemed more obvious than the single
# letter variable name of "f".

# "--------------------------"

cars = 3
people = 8

people_per_car = people / cars

# Round to 1 decimal
print(f"There are {people_per_car:.1f} people in each car.")
# Output: There are 2.7 people in each car.

# Round to 2 decimals
print(f"There are {people_per_car:.2f} people in each car.")
# Output: There are 2.67 people in each car.

# Round to 3 decimals
print(f"There are {people_per_car:.3f} people in each car.")
# Output: There are 2.667 people in each car.

distance = 9 * 1205 * 18

# Scientific notation with 3 digits of precision
print(f"The distance is: {distance:.3e} meters.")
# Output: The distance is: 1.952e+05 meters.

# Scientific notation with 6 digits of precision
print(f"The distance is: {distance:.6e} meters.")
# Output: The distance is: 1.952100e+05 meters.

big_number = 123456789

# Display without formatting:
print(f"The number is: {big_number}")
# Output: The number is: 123456789

# Display with "," formatting:
print(f"The number is: {big_number:,}")
# Output: The number is: 123,456,789

# Display with "_" formatting:
print(f"The number is: {big_number:_}")
# Output: The number is: 123_456_789

import math

radius = 5
area = math.pi * (radius ** 2)
print(f"The area is: {area}")
# Output: The area is: 78.53981633974483

import math

weight = 1.65

lower = math.floor(weight)
print(lower)
# Output: 1

higher = math.ceil(weight)
print(higher)
# Output: 2

# Proper style
area = length * width