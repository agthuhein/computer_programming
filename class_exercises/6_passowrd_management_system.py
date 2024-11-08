def check_password_strength(password):
    if len(password) < 8:
        print("Weak password: too short")
        return False

    for c in password:
        if c.isupper():
            upper = True
        elif c.islower():
            lower = True
        elif c.isdigit():
            digit = True
        else:
            break
    
    if upper and lower and digit:
        print("Strong password!")
        return True

    print("Moderate password: missing character types")
    return False    

# Main program
def main_function():
    while True:
        # Prompt the user to enter a list of passwords
        passwords = input("Enter you password: ").split(',')

        for password in passwords:
            password = password.strip()  # Remove leading/trailing whitespace
            if check_password_strength(password):
                break  # Exit the loop if a strong password is found

main_function()
