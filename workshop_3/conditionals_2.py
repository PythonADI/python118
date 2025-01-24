temperature = -45

"""
თუ (40 გრადუსზე მეტია ტოლია) მაშინ ჩაირთოს კონდენციონერი
თუ (20 ზე ნაკლებია) მაშინ ჩაირთოს გათბობა და გამოირთოს კონდენციონერი
"""
if temperature >= 40:
    print("Turn off the central heating")
    print("Start air conditioning")
elif temperature < -15:
    print("Yelp")
elif temperature < 20:
    print("Turn off the AC")
    print("Turn on the CH")
# else:
#     if temperature < 20:
#         print("Turn off the AC")
#         print("Turn on the CH")



if temperature < 0:
    print("let's ski")

if temperature < -40:
    print("Hot chocolate")

if temperature > 30:
    print("let's swim")

if temperature > 45:
    print("bring ice")
