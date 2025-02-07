"""
ask use for number (n)
and print every number from 0 to 1000 that is divisible by n
"""

n = int(input("Enter n: "))

for i in range(1000):
    if i % n == 0:
        print(i)

