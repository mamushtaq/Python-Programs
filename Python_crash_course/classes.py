class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    def fill_gas_tank (self):
        """We can fill the gas tank of normal cars"""
        print("Gas tank filled")

class Battery():

    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has " + str(self.battery_size) + "kwh battery life.")

    def get_range(self):
        """Prints out the range of the car"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "The range of battery is " + str(range)
        message += " miles on a full charge"
        print(message)

class ElectricCar(Car):
    """A class initializes attributes of Car
    Creates new attributes for Electric Car"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        #We can send instances as attributes
        self.battery = Battery()


    def describe_battery(self):
        print("This car has " + str(self.battery.battery_size) + "kwh battery life.")

    #We can override function if there is an attribute in parent class which is not needed in child class. EG

    def fill_gas_tank(self):
        """Ekectric cars do not need a gas tank"""
        print("Electric car does not need a gas tank.")

    

my_car = Car("ada", "2esdw",2021)
print(my_car.get_descriptive_name())

my_tesla = ElectricCar("tesla", "model s", 2021)
print (my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_car.fill_gas_tank()
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()