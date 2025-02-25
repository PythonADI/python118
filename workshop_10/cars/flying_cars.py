from cars.base_car import Car
from cars.electric_cars import ElectricCar

class FlyingCar(Car):
    # this is called inhertance / Polymorphism
    # Flying car is a child class to Car
    def __init__(self, make, model, price, flight_range = 600):
        super().__init__(make, model, price)
        self.flight_range = flight_range

    def move(self):
        # move method is now overriden (Car method)
        print(f"{self.make} - {self.model} is Flying is skies")


class SpaceCar(FlyingCar):
    def launch_to_space(self):
        print("Going to space!")

    def move(self):
        # move method is now overriden (FlyingCar method)
        print(f"{self.make} - {self.model} is Flying is space")

    def charge(self):
        print(f"Fueling {self.make} - {self.model}")


class ElectricSpaceCar(ElectricCar, SpaceCar):
    def __init__(self, make, model, price, flight_range):
        super().__init__(make, model, price)
        SpaceCar.__init__(self, make, model, price, flight_range)
