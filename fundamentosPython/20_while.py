"""
while True:
    print("Se ejecuto")
    

counter = 0

while counter < 10:
    counter += 1
    print("contador va en: ", counter)
    

counter = 0

while counter < 20:
    counter += 1
    if counter == 15:
        break
    print("contador va en: ", counter)
"""

counter = 0

while counter < 20:
    counter += 1
    if counter < 15:
        continue
    print("contador va en: ", counter)