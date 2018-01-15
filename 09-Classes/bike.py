class Bike():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("This bike has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back odometer reading")

    def increment_odometer(self, miles):
        if miles >= 0:  # reject negative values
            self.odometer_reading += miles
        else:
            print("You cannot roll back odometer reading")

my_new_bike = Bike("honda", "125", 2014)
print(my_new_bike.get_descriptive_name())
my_new_bike.read_odometer()
my_new_bike.odometer_reading = 23
my_new_bike.read_odometer()
my_new_bike.update_odometer(35)
my_new_bike.read_odometer()
my_new_bike.increment_odometer(8)
my_new_bike.read_odometer()
