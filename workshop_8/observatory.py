"""

>>> Full Name: Josh Doe
>>> Start Date: 01/02/2025
Enter Temperatures (Type END to stop recording)
>>> 7
Successfully recorded (01/02/2025, 7)
>>> 9
Successfully recorded (02/02/2025, 9)
>>> 6
Successfully recorded (03/02/2025, 6)
>>> ads
Please use correct number format!
>>> -101
Temperature should be in range of [-100, 100]
>>> END

[01/02/2025] Josh Doe - 7
[02/02/2025] Josh Doe - 9
[03/02/2025] Josh Doe - 6 
"""
from datetime import datetime, timedelta

full_name = input("Full Name: ")
date_format = "%d/%m/%Y"
start_date = datetime.strptime(input(f"Start Date ({date_format}): "), date_format)
current_date = start_date
temperatures = []
print("Enter Temperatures (Type END to stop recording)")
while True:
    user_input = input(">>> ")
    if user_input == "END":
        break

    try:
        temperature = float(user_input)
    except ValueError:
        print("Please use correct number format!")
        continue

    if temperature < -100 or 100 < temperature:
        print("Temperature should be in range of [-100, 100]")
        continue

    print(f"Successfully recorded ({current_date}, {user_input})")
    temperatures.append({
        "temperature": temperature,
        "scientist": full_name,
        "date": current_date
    })
    current_date += timedelta(days=1)

# print(temperatures)


with open(f"./workshop_8/{full_name}_{start_date.date()}.csv", "w") as f:
    for record in temperatures:
        f.write(f"{record['date'].date()},{record['scientist']},{record['temperature']}\n")

with open(f"./workshop_8/{full_name}_{start_date.date()}.txt", "w") as f:
    for record in temperatures:
        f.write(f"[{record['date'].date()}] {record['scientist']} | {record['temperature']}\n")
        