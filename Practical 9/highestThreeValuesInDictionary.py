my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}

sorted_values = sorted(my_dict.values(), reverse=True)[:3]
print("Highest 3 values:", sorted_values)
