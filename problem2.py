import pandas as pd

cars = pd.read_csv('cars.csv')

##Solutions to subproblems are not printed, instead enter to console window.

cars.iloc[0:5,::2]

cars.loc[cars['Model']=='Mazda RX4']

cars.loc[cars['Model']=='Camaro Z28']['cyl']

cars.loc[((cars.Model == 'Mazda RX4 Wag') | (cars.Model == 'Ford Pantera L') | (cars.Model == 'Honda Civic')),['Model','cyl','gear']]
