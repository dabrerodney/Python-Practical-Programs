# Write a program to find out absolute value of an input number

def absolute_value(number):
  return abs(number)

number = float(input("Enter a number: "))

absolute_value = absolute_value(number)
print(f"The absolute value of {number} is {absolute_value:.2f}")
