# and
print("AND")
print("True and True = ", True and True)
print("True and False = ", True and False)
print("False and False = ", False and False)
print("False and True = ", False and True)

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

age = int(input("Ingresa tu edad: "))
print("Eres mayor de edad y menor de 30? ", age >= 18 and age <= 30)

# or 
print("OR")
print("True or True = ", True or True)
print("True or False = ", True or False)
print("False or False = ", False or False)
print("False or True = ", False or True)

age = int(input("Ingresa tu edad: "))
print("Eres menor de edad y mayor de 30? ", age <= 18 or age >= 30)
