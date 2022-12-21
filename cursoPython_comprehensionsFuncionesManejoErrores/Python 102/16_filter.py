numbers = [1,2,3,4,5]
newNumbers = list(filter(lambda x: x % 2 == 0, numbers))
print(newNumbers)
print(numbers)