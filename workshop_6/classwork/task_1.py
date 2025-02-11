"""
1. Smart heating
2. ask user for comfortable temperature (min, max)
3. keep temperature in this range

program should increase temperature randomly by [0 - 3] if heating is on
program should decrease temperature randomly by [0 - 3] if heating is off
this checks will happen every second
turning heating on / off is considered switch the heting_on variable to True / False 
"""
import time
import datetime
import random

temperature = 26
heating_on = False
mn = int(input("Enter your desired min temperature: "))
mx = int(input("Enter your desired max temperature: "))

# start = timse.time()
# i = 0
while True:
    # i += 1
    # if (time.time() - start) >= 1:
    #     print(i)
    #     break
    print(f'[{datetime.datetime.now()}]: {temperature = }')
    change = random.randint(0, 3)
    if heating_on:
        temperature += change
    else:
        temperature -= change

    if temperature < mn:
        print("Turning on the heating")
        heating_on = True
    elif mx < temperature:
        heating_on = False
        print("Turning on the heating")

    time.sleep(1)
