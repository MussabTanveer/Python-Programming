# Importing an Entire Module

import car

my_civic = car.Car("honda", "civic", 2017)
print(my_civic.get_descriptive_name())

my_tesla = car.ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
