"""
@author: Sebastian Bednarski
"""
import pandas as pd
import matplotlib.pyplot as plt

DataFrame = pd.read_csv("vaccinations-by-manufacturer.csv")
print(DataFrame.head(5))
print('========= ZAD 1 ===========')
a = []
a = DataFrame.shape
print('DataFrame ma '+ str(a[0]) + ' wierszy i ' + str(a[1]) + ' kolumny')
print('\n Przed zamiana \n' + str(DataFrame.dtypes))
DataFrame = DataFrame.astype({'location': 'string', 'date': 'datetime64[ns]', \
    'vaccine': 'string', 'total_vaccinations': 'int64' }) #jak przypisalem do zmiennej df zamiasta DataFrame nie zmienił sie typ w zadaniach dalej i data wyskakiwała bez godziny 00:00:00
print('\n Po zamianie \n' + str(DataFrame.dtypes))

print('========= ZAD 2 ===========')
print('1. Dane gromadzone są dla ' + str(DataFrame.location.nunique()) + ' krajow')
print('2. W danych znajduja sie informacje dla ' + str(DataFrame.vaccine.nunique()) + ' producentow szczepionek')
print('3. Najwczesniejsza data dla Polski to ' + str(DataFrame[DataFrame.location == 'Poland'].date.min()))
print('4. Najbardziej aktualne dane w pliku pochodzą z ' + str(DataFrame.date.max()))
# algorytm przedstawiony na zajęciach
# grupujemy według kolumn location oraz vaccine, 
# w każdej z grupek dla kazdego kraju znajdujemy max liczby zasczepionych w ostatnich aktualizacjach, 
# sumujemy razem szczepionki w danych krajach, 
# resetujemy index- bo jest zaburzony DataFrame, 
# na koncu sortujemy nierosnąco 
country_sum = DataFrame.groupby(['location', 'vaccine']).total_vaccinations.max()\
    .groupby(['location']).sum('total_vaccinations').reset_index()\
    .sort_values('total_vaccinations', ascending = False)
country_sum.plot.bar(x = 'location', y = 'total_vaccinations')
plt.title('Wykres sumy szczpionek od danego kraju')
plt.xlabel('kraj')
plt.ylabel('ilosc szczepionek')
plt.grid(True)
plt.show()

poland = DataFrame[DataFrame['location'] == 'Poland'].groupby('date')\
    .sum('total_vaccinations').reset_index()
plt.plot(poland.date, poland.total_vaccinations, marker='d', linestyle = 'None', color = 'r')
plt.title('Wykres sumy szczpionek w Polsce danego dnia')
plt.xlabel('dzień')
plt.ylabel('ilosc szczepionek')
plt.show()

Polska = DataFrame[DataFrame['location'] == 'Poland'].groupby(['date', 'vaccine']).sum().transpose().stack(0).reset_index()
fig,a = plt.subplots(2,2)
a[0][0].plot(Polska['date'], Polska['Johnson&Johnson'])
a[0][0].set_title('Johnson&Johnson')
a[0][1].plot(Polska['date'], Polska['Oxford/AstraZeneca'])
a[0][1].set_title('Oxford/AstraZeneca')
a[1][0].plot(Polska['date'], Polska['Pfizer/BioNTech'])
a[1][0].set_title('Pfizer/BioNTech')
a[1][1].plot(Polska['date'], Polska['Moderna'])
a[1][1].set_title('Moderna')
plt.show()