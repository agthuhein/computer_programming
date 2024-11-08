def calculate_tax(salary):
    if salary > 0 and salary <= 20000:
        return salary * 0.0
    elif salary > 20001 and salary <= 50000:
        return round((salary * 0.10),2)
    elif salary > 500001 and salary <= 100000:
        return round((salary * 0.20),2)
    else:
        return round((salary * 0.30),2)

salary = int(input("Enter your salary: "))
print(F"You have to pay {calculate_tax(salary)} as your income tax")