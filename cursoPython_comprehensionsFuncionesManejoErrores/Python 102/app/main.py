import utils 
keys,values = utils.getPopulation()
print(keys,values)

data = [
    {
        "Country": "Colombia",
        "Population": 300
    },
    {
        "Country": "Bolivia",
        "Population": 100
    }
]

country = input("Escribe el pais que desea buscar: ")

result = utils.populationByCountry(data, country)
print(result)