def count_case_letters(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

# Example usage:
string = "Hello World"
upper_count, lower_count = count_case_letters(string)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
