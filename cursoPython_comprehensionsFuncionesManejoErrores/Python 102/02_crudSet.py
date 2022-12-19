setCountries = {"Col", "Mex", "Bol"}

size = len(setCountries)
print(size)

print("Col" in setCountries)
print("Pe" in setCountries)

# add
setCountries.add("Pe")
print(setCountries)
setCountries.add("Pe")
print(setCountries)

# update
setCountries.update({"Ar","Ecua","Pe"})
setCountries.add("Pe")
print(setCountries)

# remove
setCountries.remove("Col")
print(setCountries)
setCountries.remove("Ar")
print(setCountries)
#setCountries.remove("Colo")
setCountries.discard("Colo")
print(setCountries)

setCountries.add("Arg")
print(setCountries)

setCountries.clear()
print(setCountries)
print(len(setCountries))