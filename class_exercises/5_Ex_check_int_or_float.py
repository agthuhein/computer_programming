number = float(input("Enter a value please: "))

if number.is_integer():
    print(F"{int(number)} is an integer.")
else:
    dec_component = round((number - int(number)),2)
    #print("{} is a float. And it's decimal component is {}".format(number, dec_component))
    print(F"{number} is a float. And it's decimal component is {dec_component}.")