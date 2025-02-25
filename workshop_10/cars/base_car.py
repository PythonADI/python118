class Car:
    # Car is a parent class
    def __init__(self, make, model, price):
        # __init__ method is call initialize and it is called when object is instatiated
        # init is sometimes refered as constructor

        # these are called attributes
        self.make = make
        self.model = model
        self.price = price
        self.odometer = 0

    def move(self):
        print(f"{self.make} - {self.model} is moving on ground")

    def print_odometer(self):
        print(f"Reading on odometer for {self.make} - {self.model}: {self.odometer} ")

    def update_odometer(self, milage):
        if milage < 0:
            print("Milage should be positive!")
        self.odometer += milage
