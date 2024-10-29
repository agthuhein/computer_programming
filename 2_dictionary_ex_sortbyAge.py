collection_a = [{"name": "oliver", "age":41}, {"name": "rachel", "age":20}, {"name": "william", "age":30}]

sorted_by_age = sorted(collection_a, key=lambda x:x["age"])
#sorted_by_name = sorted(collection_a, key=lambda x:x["name"])

print(sorted_by_age)
#print(sorted_by_name)


###Lambda function example
add_two_number = lambda x,y: x+y
print(add_two_number(5, 6))
