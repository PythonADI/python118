"""

1. Register user
2. Deposit
3. Withdaw
4. Show all customers

EXAMPLE
>>> register
Enter Name
>>> Luka
Enter initial Deposit
>>> 100
Successfully saved "Luka" to database (ID: 1)

>>> list
1 | Luka | 100
2 | Nick | 700
3 | Johnny | 1000


>>> Deposit
Enter ID:
>>> 1
Enter Amount
>>> 1000
Sucessfully added 1000$ to "Luka"
New Balance: 1100$


1. Explain each function's role
2. Explain each line with comments
3. find user by id / name and show balance
4. Add transfer functionality
5. [Challenge] make user name unique
6. [Extra Challenge] optimise databaese update (udopate only the record instead of whole file)

"""
import os
import math
import csv

FILE_NAME = "database.txt"
users = []


def input_number(text, min_ = -math.inf, max_ = math.inf):
    while True:
        try:
            print(text)
            number = float(input(">>> "))
        except ValueError:
            print("Pease Enter correct number!")
            continue

        if number < min_ or max_ < number:
            print(f"Please enter number in range [{min_}, {max_}]")
            continue

        return number


def update_database():
    with open(FILE_NAME, "w", encoding="UTF-8") as f:
        f.write("id,name,balance\n")
        for user in users:
            f.write(f"{user['id']},{user['name']},{user['balance']}\n")


def load_users_from_database():
    with open(FILE_NAME) as f:
        f.readline()

        for line in csv.reader(f):
            id_, name, balance = line
            id_ = int(id_)
            balance = float(balance)

            users.append({
                "id": id_,
                "name": name,
                "balance": balance
            })


def register_user():
    print("Enter Name")
    name = input(">>> ")
    initial_deposit = input_number("Enter Initial Deposit", 0)
    users.append({
        "id": len(users) + 1,
        "name": name,
        "balance": initial_deposit
    })
    update_database()
    print(f"Successfully added {name} to data base")


def display_users():
    print("ID | NAME | BALANCE")
    for user in users:
        print(user["id"], user["name"], user["balance"], sep=" | ")

def change_balance(user, amount):
    user["balance"] += amount


def find_user(id_):
    for user in users:
        if user["id"] == id_:
            return user

    return None

def find_user_and_deposit():
    id_ = input_number("Enter ID", 1)
    user = find_user(id_)
    if user is None:
        print("Could not find user!")
        return

    amount = input_number("Enter Amount", 0)
    change_balance(user, amount)
    update_database()
    print("Successfully deposited money")


def find_user_and_withdraw():
    id_ = input_number("Enter ID", 1)
    user = find_user(id_)
    if user is None:
        print("Could not find user!")
        return

    amount = input_number("Enter Amount", 0)
    if user["balance"] < amount:
        print("Insufficient funds!")
        return
    change_balance(user, -amount)
    update_database()
    print("Successfully deposited money")



def main():
    if os.path.exists(FILE_NAME):
        load_users_from_database()
    while True:
        print("\n", "-" * 10, "\n", sep="")
        command = input(">>> ")
        if command == "add":
            register_user()
        elif command == "list":
            display_users()
        elif command == "deposit":
            find_user_and_deposit()
        elif command == "withdraw":
            find_user_and_withdraw()
        else:
            print("Inccorect command, please try again!")

main()