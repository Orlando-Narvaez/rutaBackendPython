# Union
setA = {"Col","Mex","Bol"}
setB = {"Pe","Bol"}

setC = setA.union(setB)
print(setC)
print(setA | setB)

# Interseccion
setC = setA.intersection(setB)
print(setC)
print(setA & setB)

# Difference
setC = setA.difference(setB)
print(setC)
print(setA - setB)

# Symmetric Difference
setC = setA.symmetric_difference(setB)
print(setC)
print(setA ^ setB)