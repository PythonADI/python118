import math
limit = 100000
def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


for n in range(limit + 1):
    if is_prime(n):
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")


# print(is_prime(25))
