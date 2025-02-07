temperatures = [11, 14, 13, 5, 6, 7, 8, 9, 10]

print(f'We recorded {len(temperatures)} day temperature')
print(f'first day the temperature was: {temperatures[0]} celsius')
# print(f'1st day the temperature was: {temperatures[len(temperatures) - 1]} celsius')
print(f'first day the temperature was: {temperatures[-1]} celsius')


# day {day number} was {temperature} celsius
for i in range(len(temperatures)):
    print(f'day {i + 1} was {temperatures[i]} celsius')


for temperature in temperatures:
    print(temperature)


for day, temperature in enumerate(temperatures):
    print(f'Day - {day + 1} - {temperature}')
