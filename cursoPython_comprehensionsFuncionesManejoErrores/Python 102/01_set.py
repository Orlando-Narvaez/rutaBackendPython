#Conjuntos
set_countries = {"Col", "Mex", "Bol"}
print(set_countries)
print(type(set_countries))

setNumbers = {1,2,3,4,2,444}
print(setNumbers)

setTypes = {1, "Hola", False, 12.12}
print(setTypes)

setFromString = set("Hoola")
print(setFromString)

setFromTulples = set(("abc","cbd","aeio", "as","abc"))
print(setFromTulples)

numbers = [1,2,3,4,5,1,2,3,4]
setNumbers = set(numbers)
print(setNumbers)
uniqueNumbers = list(setNumbers)
print(uniqueNumbers)