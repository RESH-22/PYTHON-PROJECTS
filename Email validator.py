import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return "Valid Email"
    else:
        return "Invalid Email"

# Taking input
email = input("Enter email address: ")
print(validate_email(email))
