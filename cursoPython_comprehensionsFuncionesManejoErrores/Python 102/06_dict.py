import random

countries = ["Col", "Mex","Bol","Pe"]

populationV2 = {country: random.randint(1,100) for country in countries}
print(populationV2)

result = { country: population for (country, population) in populationV2.items() if population > 50 }
print(result)

text = "Hola soy Chacho"
unique = { c: c.upper() for c in text if c in "aeiou" }
print(unique)