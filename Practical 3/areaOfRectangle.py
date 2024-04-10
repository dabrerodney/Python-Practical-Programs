# Write a program to find the area of Rectangle

def area(length, width):
    if length < 0 or width < 0:
        print ("Enter vaild values")
    else:
        return length * width
    
length = float(input("Enter the Length: "))
width = float(input("Enter the Width: "))
result = area(length, width)
print(f"the area of length {length} and width {width} is {result}")