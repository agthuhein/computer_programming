nameList = ["William", "Priyamkumar", "Saloni", "Kirtesh", "Aung Thu Hein", "Su Mon", "Bond"]
counter = 0

while counter < len(nameList):
    if nameList.__contains__("Bond"):
        print("We've been expecting you, Mr. Bond")
        break
    counter += 1


"""
while counter < len(nameList):
    if "Bond" in nameList:
        print("We've been expecting you, Mr. Bond")
        break
    counter += 1
"""