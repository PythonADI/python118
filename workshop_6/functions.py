# function definition
def f(x):
    print(x ** 2)


# function with multiple parameters
def turn_on_heating(house, percentage = 50):
    print(f"Accessing {house} central heating system")
    print("Successfully accessed")
    print(f"Increasing by {percentage}%")
    print(f"Turned on heaing in {house} {percentage}%")


# function call
f(7)
f(9)
f(3)

turn_on_heating("House 1", 90)
turn_on_heating("House 7", 20)
turn_on_heating("House 3", 0)
turn_on_heating("House 5")
# turn_on_heating(80, "House 5")


