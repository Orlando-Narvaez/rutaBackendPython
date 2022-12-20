def findVolume(leng=1, width=1, depth=1):
    return leng * width * depth, width, "Hola"

result, width, text = findVolume(width=10)

print(result)
print(width)
print(text)