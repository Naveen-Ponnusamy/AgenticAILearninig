import re

def validate_password(password):
    errors = []

    if len(password) < 8:
        errors.append("Password should be at least 8 characters long.")

    if not any(char.isupper() for char in password):
        errors.append("Password should include at least one uppercase letter.")

    if not any(char.islower() for char in password):
        errors.append("Password should include at least one lowercase letter.")

    if not any(char.isdigit() for char in password):
        errors.append("Password should include at least one number.")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("Password should include at least one special character.")

    return errors

# Prompt for user input
username = input("Enter your username: ")
password = input(f"Hello {username},Please enter your password for registration: ".format(username))

# Validate the password
validation_errors = validate_password(password)

# Output result
if not validation_errors:
    print(f"Thank you, {username}. Your password has been successfully set.")
else:
    print(f"Hi {username}, your password doesn't meet the following requirement(s):")
    for error in validation_errors:
        print(f"- {error}")
