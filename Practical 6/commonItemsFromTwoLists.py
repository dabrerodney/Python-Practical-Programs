def find_common_items(list1, list2):
    return list(set(list1) & set(list2))

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print("Common items from two lists:", find_common_items(list1, list2))
