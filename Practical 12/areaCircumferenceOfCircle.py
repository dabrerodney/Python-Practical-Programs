import math

def calculate_circle_area(radius):
    # Calculate area of circle: A = π * r^2
    area = math.pi * radius ** 2
    return area

def calculate_circle_circumference(radius):
    # Calculate circumference of circle: C = 2 * π * r
    circumference = 2 * math.pi * radius
    return circumference

# Test the functions
radius = 5
area = calculate_circle_area(radius)
circumference = calculate_circle_circumference(radius)

print("Radius of the circle:", radius)
print("Area of the circle:", area)
print("Circumference of the circle:", circumference)
