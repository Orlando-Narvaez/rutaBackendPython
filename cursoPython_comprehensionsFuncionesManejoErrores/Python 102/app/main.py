import utils
import readCSS
import charts

def run():
  data = readCSS.read_csv('./data.csv')
  """data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generateBarChart(countries, percentages)
  """
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generateBarChart(labels, values)

if __name__ == '__main__':
  run()