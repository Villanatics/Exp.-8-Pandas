import pandas as pd
car=pd.read_csv("cars.csv")
a=car.iloc[:5,1:11:2]
b=car[car["Model"]== "Mazda RX4"]
c=car.loc[car["Model"]== "Camaro Z28" , ["cyl"]]
e=car.loc[car["Model"] == "Honda Civic",["cyl","gear"]]
f=car.loc[car["Model"] == "Ford Pantera L",["cyl","gear"]]
g=car.loc[car["Model"] == "Mazda RX4 Wag",["cyl","gear"]]
d=pd.concat([e,f,g])
print(a,b,c,d)
