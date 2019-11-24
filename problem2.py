import pandas as pd

cars = pd.read_csv('cars.csv')

cars.iloc[[0,5]]

cars.loc[cars['Model']=='Mazda RX4']

cars.loc[cars['Model']=='Camaro Z28']['cyl']

cars.loc[((cars.Model == 'Mazda RX4 Wag') | (cars.Model == 'Ford Pantera L') | (cars.Model == 'Honda Civic')),['Model','cyl','gear']]
