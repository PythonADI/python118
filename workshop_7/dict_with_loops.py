person = {
    "first_name": "George",
    "last_name": "Washington",
    "address": "Washington D.C.",
    "tel": "+1 180-234-123",
    "age": 27,
    "friends": [
        "Kate",
        "Nick",
        "mary"
    ],
    "is_alive": True
}
print("\nOnly keys")
for key in person.keys():
    print(key)

print("\nOnly Values")
for value in person.values():
    print(value)

print("\nitems")
for key, value in person.items():
    print(key, value)
