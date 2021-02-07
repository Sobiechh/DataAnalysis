import pandas as pd
import matplotlib.pyplot as plt

price_data = pd.read_csv('price.csv')

#print(price_data.head())

price_data = price_data.fillna(0)
#fill nan with 0 

#print(price_data.head())

def get_price():
    for index, row in price_data.iterrows():

        total_price = row['Total_Price']
        quantity = row['Quantity']

        price_of_unit = total_price/quantity
        print(price_of_unit)

get_price()

plt.bar(price_data.Item_Name, height=price_data.Total_Price)
plt.title('Barplot of things')
plt.show()