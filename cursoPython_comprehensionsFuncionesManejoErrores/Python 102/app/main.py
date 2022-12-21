import utils 

def run():
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

if __name__ == '__main__':
    run()