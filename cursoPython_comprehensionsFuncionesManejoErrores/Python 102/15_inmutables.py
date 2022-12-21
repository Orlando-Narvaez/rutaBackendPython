items = [
    {
        "product": "Camisa",
        "price": 100,
    },
    {
        "product": "Pantalon",
        "price": 300,
    },
    {
        "product": "Camisa rayada",
        "price": 200,
    }
]

def addTaxes(item):
    newItem = item.copy()
    newItem["taxes"] = newItem["price"] * .19
    return newItem

newItem = list(map(addTaxes, items))
print("New list")
print(newItem)
print("Old list")
print(items)