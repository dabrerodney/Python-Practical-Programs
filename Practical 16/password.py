class PasswordIncorrectError(Exception):
    pass

def validate_password(password):
    correct_password = "password123"
    if password != correct_password:
        raise PasswordIncorrectError("Password is incorrect")

# Example usage:
try:
    user_password = input("Enter your password: ")
    validate_password(user_password)
    print("Login successful")
except PasswordIncorrectError as e:
    print(e)
