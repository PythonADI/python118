# Type cast / conversion
# print(int("33"))
age = int(input("age: "))

is_adult = age >= 18

if age < 18:
    # indentation
    print("You are not allowed here")
    print("ask your parents")
else:
    print("Welcome")

print(f"You are {age} years old! {is_adult = }")
print(type(age))
