# Write a program to calculate area and perimeter of the square

def area(side):
    return side ** 2

def perimeter(side):
    return 4 * side

side = float(input("Enter the side of square: "))
a = area(side)
p = perimeter(side)

print(f"The area and perimeter of a square of whose side is {side} is {a} & {p}")