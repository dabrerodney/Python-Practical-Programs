# Write a program to check if a Number is Positive, Negative or Zero

def check_number(number):
  if number > 0:
    return "positive"
  elif number < 0:
    return "negative"
  else:
    return "zero"

number = float(input("Enter a number: "))

number_type = check_number(number)
print(f"{number} is {number_type}")
