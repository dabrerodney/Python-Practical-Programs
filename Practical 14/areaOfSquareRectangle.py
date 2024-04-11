class ShapeArea:
  def calculate_area(self, side):
    area = side * side
    print(f"Area of the square: {area}")

  def calculate_area(self, length, breadth):
    area = length * breadth
    print(f"Area of the rectangle: {area}")

# Create an object of the ShapeArea class
obj = ShapeArea()

# Call the calculate_area methods with different parameters
obj.calculate_area(5)  # Square with side 5
obj.calculate_area(3, 4)  # Rectangle with length 3 and breadth 4
