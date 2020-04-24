#!/usr/bin/env python
# coding: utf-8

# Zadanie 2 (15 pkt) 
# W zadaniu wykorzystaj zbiór danych zawierajacy cechy samochodów, gdzie zmienna objasniajaca znajduje sie w pierwszej kolumnie
#  (mpg- miles per gallon, czyli spalanie). Braki danych w zbiorze oznaczone sa znakiem „?”. 
# Kolejne zmienne oddzielone sa spacja. Zbiór danych znajduje sie pod adresem:
# 
# https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data
# 
# Kolejne kolumny w zbiorze danych to:
# 1. mpg: continuous  2. cylinders: multi-valued discrete 3. displacement: 
# continuous 4. horsepower: continuous 5. weight: continuous 6. acceleration: continuous 7. model_year: multi-valued discrete  
#  8. origin: multi-valued discrete 9. car_name: string (unique for each instance)
# 
# Wykonaj nastepujace polecenia:
# 
# 	1.Wgraj dane bezposrednio z internetu. (2 pkt). 
# 	2.Nazwij kolumny jak w liscie powyzej (mozna skrócic nazwy). (2 pkt)
# 	3.Usun ostatnia kolumne danych. Usun braki danych. (2 pkt)
# 	4.Jakie jest srednie spalanie samochodów o liczbie cylindrów równej 8 i mocy (horsepower) wiekszej niz mediana mocy? (3pkt) 
# 	5.Wyswietl na wykresie slupkowym srednie spalanie dla kolejnych dwuletnich grup roku produkcji samochodu. (3 pkt)
# 	6.Na jednym rysunku narysuj 4 wykresy rozrzutu zmiennej objasnianej i zmiennych displacement, horsepower, weight, acceleration. Dla kazdego wykresu nanies linie regresji. (3 pkt)
# 

# # Pudpunkt 1, 2

# In[1]:


import numpy as np
import pandas as pd
import statistics #do mediany


# In[2]:


data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data', 
                    sep='\s+', 
                    header = None,
                    names=["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "car_name"])


# In[3]:


data.head(100)


# # Podpunkt 3

# In[4]:


data.tail(3)


# In[5]:


data.drop(data.tail(1).index,inplace=True)


# In[6]:


data.tail(3)


# # Podpunkt 4

# In[7]:


#kolumna horsepower do lsity
horsepower_median = data['horsepower'].tolist()
#pominiecie ?
horsepower_median = [elem for elem in horsepower_median if elem != '?']
#zamiana do numeric
horsepower_median = pd.to_numeric(horsepower_median)
#wykorzystanie median
horsepower_median = statistics.median(horsepower_median)
#print(horsepower_median)

cons =  [] #tablica ze spalaniami kazdego z aut
for index, row in data.iterrows(): 
    if row['horsepower'] != '?': #pominiecie '?'
        if (float(row['horsepower']) > horsepower_median) and (int(row['cylinders']) == 8): #wytyczne do podpunktu
            cons.append(float(row['mpg'])) #dodanie do listy

#print(cons) 
#uzycie numpy do znalezienia sredniej wartosci spalania samochodow
avg = np.mean(cons)

#odpowiedz
print(avg)


# # Podpunkt 5

# In[8]:


years = [] #wszystkie lata produkcji
years_pair = [] #kazda z par dwuletnich grup produkcji
x_val = [] #tablica do danych w wykressie (poziom)
y_val = []

for index, row in data.iterrows():  #dodawanie do listy kazdey rok
    years.append(row['model_year'])
    

years = list(set(years))
#print(years) #lsita wszystkich rocznikow

for i in range(0, len(years)-1): #wypisujemy pary kolejnych rocznikow
    x_val.append(f"{years[i]}, {years[i+1]}")
    temp = []
    temp.append(years[i])
    temp.append(years[i+1])
    years_pair.append(temp)
    
#print(years_pair)

y_val = []
            
for years in years_pair:
    temp = data[(data['model_year'] == years[0]) | (data['model_year'] == years[1])] #robimy nowe dataframe tylko z rocznikami sasiadujacymi po kolei
    y_val.append(round(temp['mpg'].mean(),2)) #dodajemy srednia wartosc z kolumny mpg (spalanie) z zaokrągleniem do dwóch
        

#print(y_val) #srednie spalanie z kazdej pary lat
#print(x_val)

    
#wynik
wynik = pd.DataFrame({'lata':x_val, 'średnie spalanie':y_val})
ax = wynik.plot.bar(x='lata', y='średnie spalanie', legend=False, title='Srednie spalanie dla kazdej z par lat produkcji')


# # Podpunkt 6

# In[25]:


import seaborn
import matplotlib.pyplot as plt

data1 = data.replace({'?': '10.0'})


fig, (ax1, ax2, ax3, ax4) = plt.subplots(ncols=4, sharey=True, figsize=(40,10))



seaborn.regplot(x ='displacement', y='mpg', data=data1, truncate=False, color='green', ax=ax1, ci = None)

seaborn.regplot(x ='displacement', y='mpg', data=data1, truncate=False, color='blue', ax=ax2, ci = None)

seaborn.regplot(x = 'weight',       y='mpg', data=data, truncate=False, color='red', ax=ax3, ci = None)

seaborn.regplot(x = 'acceleration', y='mpg', data=data, truncate=False, color='pink', ax=ax4, ci = None)


# In[27]:


#for index, row in data1.iterrows():  #moze wystapic maly problem z horsepower, robione na Jupyterze dziala, natomiast nie w przypadku VSCode
#    print(row['horsepower'])