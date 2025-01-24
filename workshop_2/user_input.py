first_name = input("What's your name? ").strip()
last_name = input("What's your last name? ").strip()
# first_name = first_name.strip()
# last_name = last_name.strip()

full_name = first_name + " " + last_name
# full_name = f'{first_name} {last_name}'


full_name = full_name.title()
print("Hello " + full_name)
print(full_name)
