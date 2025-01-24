is_windy = False
is_rainy = False
is_sunny = True


if (is_sunny or is_rainy) and not is_windy:
    print("I love this kind of weather")


if is_rainy and is_windy:
    print("Hate that weather")
elif is_rainy and not is_windy:
    print("it's ok")
elif not is_rainy and is_windy:
    print("Hate that weather")
# elif not is_rainy and not is_windy:
#     print('good weather')
else:
    print("Good Weather")
