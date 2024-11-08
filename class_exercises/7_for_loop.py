customer_list = ["customer1", "customer2", "customer3", "customer4", "customer5"]

for cust in customer_list:
    if cust == "customer2":
        continue
    print(cust)

"""
for cust in customer_list:
    if cust != "customer2":
        print(cust)
"""

"""
for cust in customer_list:
    print(cust)

    if cust == "customer2":
        print("Found customer two")
        break
"""