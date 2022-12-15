name = "Orlando"
lastName = "Narvaez Baracaldo"
print(name)
print(lastName)

fullName = name + " " + lastName
print(fullName)

quote = "I'm Orlando"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

#Formato
print("V1")
template = "Hola, mi nombre es: " + name + " y mis apellidos son: " + lastName
print(template)
print("V2")
template = "Hola, mi nombre es: {} y mis apellidos son: {}".format(name,lastName)
print(template)
print("V3")
template = f"Hola, mi nombre es: {name} y mis apellidos son: {lastName}"
print(template)