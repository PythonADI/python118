"""
Ask user for number, ensure that you get the number correctly
(ask user until you get the number)
"""

print("23A".isdigit())
num = input("Enter number: ")
while not num.isdigit():
    print("Please use correct number format!")
    num = input("Enter number: ")

"""
while True:
    isdigit = True
    for character in num:
        "234A647435"
        if ord(character) < 45 or 57 < ord(character):
            isdigit = False
            break

    if isdigit:
        break

    print("Please use correct number format!")
    num = input("Enter number: ")
"""


num = int(num)

print(num / 2)
