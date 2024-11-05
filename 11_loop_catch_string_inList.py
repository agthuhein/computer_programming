list_1 = [3, 7, 6, 8, 9, 11, "Hello", 15, 25, "World"]
list_2 = []

for l in list_1:
    if isinstance(l, str):
        print(F"Index {list_1.index(l)} was a sting, not an integer.")
        continue
    list_2.append(l * l)

for l in list_2:
    print(l)