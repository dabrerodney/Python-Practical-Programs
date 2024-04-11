# Write a program to check the largest number among the three numbers

def largest_number(num1, num2, num3):
  largest = max(num1, num2, num3)
  return largest

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest = largest_number(num1, num2, num3)
print(f"The largest number between {num1}, {num2} & {num3} is {largest}")