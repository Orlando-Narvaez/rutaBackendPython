numbers = [1,2,3,4]
numbersV2 = []
for i in numbers:
    numbersV2.append(i*2)

numbersV3 = list(map(lambda i: i * 2, numbers))

print(numbers)
print(numbersV2)
print(numbersV3)

numbers2 = [1,2,3,4]
numbers3 = [5,6,7]

print(numbers2)
print(numbers3)
result = list(map(lambda x,y: x + y, numbers2,numbers3))
print(result)