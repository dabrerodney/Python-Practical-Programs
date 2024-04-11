my_dict = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

# Sorting in ascending order by value
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sorting in descending order by value
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Sorted dictionary (ascending):", sorted_dict_asc)
print("Sorted dictionary (descending):", sorted_dict_desc)