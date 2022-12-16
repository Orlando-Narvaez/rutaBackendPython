myDict = {}
print(type(myDict))

myDict = {
    "Avion" : "Bla bla bla",
    "Nombre" : "Orlando",
    "Apellido": "Narvaez",
    "Años" : 23
}
print(myDict)
print(len(myDict))

print(myDict["Años"])
print(myDict.get("Años"))

print("Avion" in myDict)
print("xd" in myDict)