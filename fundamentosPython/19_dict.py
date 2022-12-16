person = {
    "name" : "Orlando",
    "lastName" : "Narvaez Baracaldo",
    "langs" : ["python","javascript"],
    "age" : 23
}

print(person)

person["name"] = "Santi"
print(person)
person["age"] -= 10
person["langs"].append("rust")
print(person)

del person["lastName"]
person.pop("age")
print(person)

print("items")
print(person.items())

print("keys")
print(person.keys())

print("values")
print(person.values())