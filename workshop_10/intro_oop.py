from cars.base_car import Car
from cars.flying_cars import FlyingCar, SpaceCar, ElectricSpaceCar

# coupling
my_car = Car("Tesla", "Model 3", 40_000)
my_car.update_odometer(-500)
my_car.print_odometer()
my_car.move()
my_car.start_engine()
print(my_car.make)
print(my_car.model)
print(my_car.price)

other_car = Car("BMW", "X5", 80_000)
print(other_car.model, other_car.make, other_car.price)
# other_car.odometer += 500
other_car.update_odometer(500)
other_car.print_odometer()

my_new_car = FlyingCar("Space Industries", "1", 7_000_000, 1700)
my_new_car.move()
print(my_new_car.flight_range)

space_car = SpaceCar("Space Industries", "Dragon 1", 70_000_000, 1_000_000)
space_car.print_odometer()
space_car.launch_to_space()
space_car.move()

esv = ElectricSpaceCar("Space Industries", "Electric Dragon 1", 70_000_000, 1_000_000)
print(esv.battery_size)
esv.launch_to_space()
esv.charge()
