# Write a program to find the square root of a number
import math

def squareRoot(no):
    if(no < 0) :
        print ("Invalid number ")
    else :
        return math.sqrt(no)
    
no = int(input("Enter the number: "))
sq = squareRoot(no)
print(f"Square Root of {no} is {sq:.2f}")