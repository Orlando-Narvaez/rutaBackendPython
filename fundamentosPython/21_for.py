"""
for elemmet in range(1,21):
    print(elemmet)
"""

myList = [23,55,12,10]
for elemment in myList:
    print(elemment)

myTuple = ("Hola","soy","Chacho")
for elemmet in myTuple:
    print(elemmet)

myProducts = {
    "name" : "Camisa",
    "price" : 100,
    "stock" : 89
}
for elemmet in myProducts:
    print(elemmet, "=>", myProducts[elemmet])

for key, value in myProducts.items():
    print(key, "=>", value)

people = [
{
    "name": "Nicolas",
    "age" :34
},
{
    "name": "Orlando",
    "age" :23
},
{
    "name": "Santi",
    "age" :10
}
]
for person in people:
    print(person["name"])