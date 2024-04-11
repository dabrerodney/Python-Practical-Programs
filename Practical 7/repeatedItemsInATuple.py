def find_repeated_items(my_tuple):
    return [item for item in my_tuple if my_tuple.count(item) > 1]

# Example usage:
my_tuple = (10, 20, 30, 10, 40, 20, 50, 10)
print("Repeated items in the tuple:", find_repeated_items(my_tuple))
