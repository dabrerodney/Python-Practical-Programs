def multiply_list(lst):
    result = 1
    for item in lst:
        result *= item
    return result

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Product of all items in the list:", multiply_list(my_list))
