import pandas as pd

cars = pd.read_csv('cars.csv')

print(cars.iloc[0:5,::2],'\n')

print(cars.loc[cars['Model']=='Mazda RX4'],'\n')

print(cars.loc[(cars['Model']=='Camaro Z28'),['cyl']],'\n')

print(cars.loc[((cars['Model'] == 'Mazda RX4 Wag') | (cars['Model'] == 'Ford Pantera L') | (cars['Model'] == 'Honda Civic')),['Model','cyl','gear']])

##For sub problem d, the column 'Model' is also printed to determine which models the data cylinders and gear type corresponds to. 
