def add(*values):
    print(f'{values = } | {type(values) = }')
    total = 0
    for value in values:
        total += value
    return total

def func(a, b, *args):
    print(f'{a = }')
    print(f'{b = }')
    print(f'{args = }')



print(add(1, 2, 3, 4, 5, 6))
print(add())
func("Testing", 27, [5, 6, 7], 37, "Hello", {"a": 5})

