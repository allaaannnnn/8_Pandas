import pandas as pd

cars = pd.read_csv('cars.csv')

print(cars.head(5))
print(cars.tail(5))