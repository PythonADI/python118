"""
Edge cases:
1. მომხმარებელმა არ ჩაწერა რიცხვითი მონაცემი
2. არ არის მთელი რიცხვი
3. სფეისები იყოს
"""

age = int(input("Age: "))

if age < 4:
    print("Free")
elif 4 < age < 18:
    print("25$")
else:
    print("40$")
