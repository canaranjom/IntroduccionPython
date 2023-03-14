import utils
import read_csv
import charts

def run():
  
  continente = input('Type Continent => ')
  
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == continente ,data))
  
  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(continente, countries, percentages)
  
  country = input('Type Country => ')
  print(country)
  result = utils.population_by_country(data, country)
  print(result)
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)
    charts.generate_plot_chart(country['Country'], labels, values)
    
  

if __name__ == '__main__':
  run()