'''
Author: Kevin Ligan

Purpose: Calculate areas of shapes
'''
print()
#Calculate the area of square
side_length = float(input('What is the length of a side of the square? '))
square_area = side_length ** 2
print(f'The area of the square is: {square_area} ')

print()
#Calcaulate the area of the rectangle
length = float(input('What is the lenght of the rectangle? '))
width = float(input('What is the width of the rectangle? '))
rectangle_area = length * width
print(f'The area of the rectangle is: {rectangle_area}')

print()
#Calculate the area of the circle
radius= float(input('what is the radius of the circle? '))
circle_area = 3.14 * radius ** 2
print(f'The area of the circle is {circle_area}')

print()
#Stretch 1: Using the math library
import math
radius= float(input('what is the radius of the circle? '))
circle_area = math.pi * radius ** 2
print(f'The are of the circle is: {circle_area}')

print()
#Stretch 2: 
length = float(input("Enter a length value: "))

print()
# Compute the areas
square_area = length ** 2
circle_area = math.pi * length ** 2
cube_volume = length ** 3
sphere_volume = 4 / 3 * math.pi * length ** 3

print()
# Display the results
print(f'Area of the square with side length {length} is {square_area}')
print(f'Area of the circle with radius {length} is {circle_area}')
print(f'Volume of the cube with side length {length} is {cube_volume}')
print(f'Volume of the sphere with radius {length} is {sphere_volume}')

print()
#Stretch 3: Conversion cm to m
# Prompt user for length value in centimeters
length_cm = float(input("Enter a length value in centimeters: "))

# Compute area of square in square centimeters and square meters
area_square_cm = length_cm ** 2
area_square_m = area_square_cm / 10000

# Compute area of circle in square centimeters and square meters
radius_cm = length_cm / 2
area_circle_cm = math.pi * radius_cm ** 2
area_circle_m = area_circle_cm / 10000

# Compute volume of cube in cubic centimeters and cubic meters
volume_cube_cm = length_cm ** 3
volume_cube_m = volume_cube_cm / 1000000

# Compute volume of sphere in cubic centimeters and cubic meters
radius_m = radius_cm / 100
volume_sphere_cm = 4/3 * math.pi * radius_cm ** 3
volume_sphere_m = volume_sphere_cm / 1000000

# Display the results
print(f'The area of the square is {area_square_cm} square centimeters or {area_square_m} square meters.')
print(f'The area of the circle is {area_circle_cm} square centimeters or {area_circle_m} square meters.')
print(f'The volume of the cube is {volume_cube_cm} cubic centimeters or {volume_cube_m} cubic meters.')
print(f'The volume of the sphere is {volume_sphere_cm} cubic centimeters or {volume_sphere_m} cubic meters.')