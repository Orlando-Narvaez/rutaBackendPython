numbers = (1,2,3,4,5)
strings = ("Orlando" , "Maritza","Jose","Orlando")
print(numbers)
print(type(numbers))
print(numbers[0])
print(numbers[-1])

print(strings)
print(type(strings))

print(strings.index("Maritza"))
print(strings.count("Orlando"))

myList = list(strings)
print(myList)
print(type(myList))

myList[0] = "Juli"
print(myList) 

myTuple = tuple(myList)
print(myTuple)
print(type(myTuple))