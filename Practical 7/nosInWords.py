def number_to_words(number):
    num_dict = {'0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
    return ' '.join(num_dict[digit] for digit in str(number))

# Example usage:
number = 1234
print("Number in words:", number_to_words(number))
