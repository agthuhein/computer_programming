collection_a = [{"name": "oliver", "age":41}, {"name": "rachel", "age":20}, {"name": "william", "age":30}]

#get_age = lambda a : a["age"]
#print(get_age)

sorted_by_age = sorted(collection_a, key=lambda x:x["age"], reverse=False)
#sorted_by_name = sorted(collection_a, key=lambda x:x["name"])

print(sorted_by_age)
#print(sorted_by_name)


###Lambda function example
#add_two_number = lambda x,y: x+y
#print(add_two_number(5, 6))

test = (3, 2, 1, 5, 6, 2, 3, 90)
sorted_item = sorted(test, reverse=True)
print(sorted_item)