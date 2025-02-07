"""
Ask user for temperature (ensure it's a number but also it should be from [-100, 100])
if everything is correct put that number inside temps list

then calculate average of temperatures
if user enters q (stop recording)

also show user which day is he wiritng for
"""
temps = []
day = 1

while True:
    user_input = input(f"Enter number {day}: ")
    if user_input == 'q':
        break

    if not (user_input.isdigit() or user_input[0] == '-' and user_input[1:].isdigit()):
        print("Please enter only numbers")
        continue

    user_input = int(user_input)

    if user_input < -100 or 100 < user_input:
        print("Enter correct temperature")
        continue

    temps.append(user_input)
    day += 1



print(temps)
total_temp = 0

for temp in temps:
    total_temp += temp

print(f"Average temperatures is: {total_temp / len(temps)}")
    