import string

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (use at least 8-12 characters).")

    # Uppercase check
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Lowercase check
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Numbers check
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Special characters
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add special characters (!,@,#,$, etc).")

    # Strength result
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, feedback


# Main program
password = input("Enter a password: ")

strength, feedback = check_password_strength(password)

print("\n🔐 Password Strength:", strength)

if feedback:
    print("\nSuggestions to improve:")
    for f in feedback:
        print("-", f)
else:
    print("Your password is very strong!")
