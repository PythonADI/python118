def add(a, b = -100):
    print(f'{a = }', f'{b = }', sep=" | ")

add(5, 7)
add(a=7, b=9)
add(b=7, a=9)
add(7, b=9)
# Error
# add(a=7, 9)

