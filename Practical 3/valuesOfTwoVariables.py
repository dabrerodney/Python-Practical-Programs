# Write a program to swap the value of two variables

def swap(a, b):
    t = a
    a = b
    b = t
    return a, b

a = int(input("Enter value: "))
b = int(input("Enter value: "))

print(f"Before Swapping a = {a} b = {b}")
c, d = swap(a, b)
print(f"After Swapping a = {c} b = {d}")