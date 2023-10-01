from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore, Back, Style, init

data = pd.read_csv('avocado.csv')

# 1. Obtener Cuantas filas y cuantas columnas tiene el conjunto de datos
print(Fore.CYAN + '--1. Obtener Cuantas filas y cuantas columnas tiene el conjunto de datos--')
print(Fore.YELLOW, data.shape)

# 2. Mostrar los primeros 100 registros
print(Fore.CYAN + '--2. Mostrar los primeros 100 registros--')
print(Fore.YELLOW, data.head(100).to_string())

# 3. Mostrar los últimos 20 registros
print(Fore.CYAN + '--3. Mostrar los últimos 20 registros--')
print(Fore.YELLOW, data.tail(20).to_string())

# 4. Cual es el precio mínimo, máximo y promedio del aguacate en ese conjunto de datos
print(Fore.CYAN + '--4. Cual es el precio mínimo, máximo y promedio del aguacate en ese conjunto de datos--')
print(Fore.YELLOW, data.describe())

# 5.Generar un gráfico de tipo scatter usando  para la x la variable 'year' y  para y la variable 'AveragePrice' para 3 regiones (las que usted elija),
print(Fore.CYAN + '5.Generar un gráfico de tipo scatter usando  para la x la variable ''year'' y  para y la variable ''AveragePrice'' para 3 regiones (las que usted elija),')

x1 = plt.subplot()
albany = data[data['region'] == 'Albany']
atlanta = data[data['region'] == 'Atlanta']
westTexNewMexico = data[data['region'] == 'WestTexNewMexico']

g_albany = albany.plot(x ='year',y ='AveragePrice', kind = 'scatter', color='red', ax = x1)
g_atlanta = atlanta.plot(x ='year',y ='AveragePrice', kind = 'scatter', color='blue', ax = x1)
g_westTexNewMexico = westTexNewMexico.plot(x ='year',y ='AveragePrice', kind = 'scatter',color='yellow', ax = x1)

plt.show()

