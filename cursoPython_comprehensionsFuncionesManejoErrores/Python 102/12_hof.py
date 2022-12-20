def increment(x):
    return x + 1
incrementV2 = lambda x: x + 1

def highOrdFunc(x, func):
    return x + func(x)

highOrdFuncV2 = lambda x, func: x + func(x)

result = highOrdFunc(2, increment)

print(result)

result = highOrdFuncV2(2,incrementV2)
print(result)