
n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a)
        nth = a + b
        a, b = b, nth
        count += 1
