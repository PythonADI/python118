import random

def give_me_number_or_nothing():
    number = random.randint(0, 10)
    if number > 5:
        return None

    return number


for i in range(10):
    print(give_me_number_or_nothing())
