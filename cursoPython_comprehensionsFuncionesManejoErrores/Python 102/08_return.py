def sumWitchRanger(min,max):
    print(min,max)
    sum = 0
    for x in range(min,max):
        sum += x
    return sum

result = sumWitchRanger(1,10)
print(result)
result2 = sumWitchRanger(result,result + 10)
print(result2)