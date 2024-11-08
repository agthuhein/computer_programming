def reverse_string(usr_str):
    return ''.join(reversed(usr_str))

usr_input = input("Please enter a string: ")
print(reverse_string(usr_input))