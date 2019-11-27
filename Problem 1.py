import pandas as pd
car=pd.read_csv('cars.csv')
cars=pd.concat([car.head(),car.tail()])
