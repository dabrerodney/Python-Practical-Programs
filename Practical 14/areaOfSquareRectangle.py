class Shape:
    def area(self, length, breadth=None):
        if breadth is None:
            print("Area of square:", length ** 2)
        else:
            print("Area of rectangle:", length * breadth)

# Example usage:
shape = Shape()
shape.area(5)               # Calls the first method
shape.area(4, 6)            # Calls the second method
