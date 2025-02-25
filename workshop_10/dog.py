import random

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


names = [
    "Milo", "Doggo", "Strawberry", "Cookie"
]
dogs = []

for _ in range(10):
    dogs.append(
        Dog(
            random.choice(names),
            random.randint(0, 7)
        )
    )



# my_dog = Dog("Milo", 7)
# my_dog.sit()
# my_dog.roll_over()
for dog in dogs:
    print(dog.name)
    dog.sit()
