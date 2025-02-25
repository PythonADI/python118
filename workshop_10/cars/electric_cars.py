from cars.base_car import Car

class ElectricCar(Car):
    def __init__(self, make, model, price):
        super().__init__(make, model, price)
        self.battery_size = 1000

    def charge(self):
        print(f"Charging {self.make} - {self.model}")
