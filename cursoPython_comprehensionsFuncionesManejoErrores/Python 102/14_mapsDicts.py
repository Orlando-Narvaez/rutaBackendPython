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

prices = list(map(lambda item: item["price"], items))
print(items)
print(prices)

def addTaxes(item):
    item["taxes"] = item["price"] * .19
    return item

newItem = list(map(addTaxes, items))
print(newItem)
print(items)