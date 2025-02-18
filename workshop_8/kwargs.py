def func(a, b, *args, c, d, **kwargs):
    """
    c parameter is keyword only argument
    """
    print(f'{a = }', f'{b = }', f'{args = }', f'{c = }', f'{d = }', f'{kwargs = }', sep=" | ")


func(7, 8, c="test", d="another test", first_name="nick", age=7)
    