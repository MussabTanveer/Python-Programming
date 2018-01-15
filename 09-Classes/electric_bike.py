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

    def fill_gas_tank(self):
        print("The bike's gas tank has been filled")


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This bike has a " + str(self.battery_size) + "-kWh battery")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This bike can go approximately " + str(range) + " miles on a full charge"
        print(message)


class ElectricBike(Bike):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This bike doesn't need a gas tank")

my_e_bike = ElectricBike("honda", "125", 2017)
print(my_e_bike.get_descriptive_name())
my_e_bike.battery.describe_battery()
my_e_bike.fill_gas_tank()
my_e_bike.battery.get_range()
