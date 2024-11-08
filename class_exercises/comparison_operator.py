#print(2 < 1)
#print(5 > 2.5)

#Traditional for-loop
output = []
for x in [10, 5, 6]:
    if x % 2 == 0:
        output.append(x)


#list conprehension (More "Pythonic")
output_list = [x for x in [10, 5, 6] if x % 2 == 0]

#############
x = 10
y = 15

print(x == y)
print(x > y)
print(y > x)

#############
A = "Gisma"
B = "Yale"

print(A == B)
print(A != B)

############
a = (1.1 + 2.2)
b = (1.1 + 2.2) * 10 / 10
print(a)
print(b)
print(a == 3.3)
print(b == 3.3)