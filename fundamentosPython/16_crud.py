# Crud = crear, leer, actaulizar y eliminar

numbers = [1,2,3,4,5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

numbers.append(700)
print(numbers)

numbers.insert(0, "Hola")
print(numbers)

numbers.insert(3, "Hice un cambio")
print(numbers)

takss = ["Todo 1", "Todo 2"]
newList = numbers + takss
print(newList)

index = newList.index("Todo 1")
newList[index] = "Se actaulizo"
print(newList)

newList.remove("Todo 2")
print(newList)

newList.pop()
print(newList)

newList.pop(0)
print(newList)

newList.reverse()
print(newList)

numbers2 = [1,10,4,22,11,77]
numbers2.sort()
print(numbers2)

strings = ["re", "ab", "ed"]
strings.sort()
print(strings)