# Write a program to calculate surface volume and area of a cylinder

import math

def surfaceArea(radius, height):
    return 2 * math.pi * radius * (radius + height)

def volume(radius, height):
    return math.pi * (radius ** 2) * height

radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))

a = surfaceArea(radius, height)
v = volume(radius, height)

print(f"The surface area and volume of radius {radius} and height {height} is {a:.2f} & {v:.2f}")