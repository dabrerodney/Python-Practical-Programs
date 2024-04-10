# Write a program to convert U.S. dollars to Indian rupees

def convertCurrency(usAmount):
    rate = 83.37
    indAmount = usAmount * rate
    print(f"{usAmount} Dollars to indian rupees is {indAmount}")

usAmount = int(input("Enter the Amount in dollars: "))

if(usAmount<0):
    print("Please Enter Correct Amount")
    exit() 
else:
    convertCurrency(usAmount)