import re

def check_password_strength(password):
    strength = 0

    # Length check
    if len(password) >= 8:
        strength += 1

    # Contains uppercase
    if re.search(r"[A-Z]", password):
        strength += 1

    # Contains lowercase
    if re.search(r"[a-z]", password):
        strength += 1

    # Contains digit
    if re.search(r"[0-9]", password):
        strength += 1

    # Contains special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Strength result
    if strength <= 2:
        return "Weak Password"
    elif strength == 3 or strength == 4:
        return "Medium Password"
    else:
        return "Strong Password"


password = input("Enter your password: ")
print("Password Strength:", check_password_strength(password))
