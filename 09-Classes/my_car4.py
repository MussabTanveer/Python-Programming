# Importing a Module into a Module

from car import Car
from electric_car import ElectricCar

my_civic = Car("honda", "civic", 2017)
print(my_civic.get_descriptive_name())

my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
