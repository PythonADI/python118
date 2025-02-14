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

print(person)

print(person["first_name"])
print(person["last_name"])

person["dog"] = "Golden Retriever"

print(person["dog"])

print(f"Removed: {person.pop('tel')}")
# del person["tel"]
print(person)
person["first_name"] = "Jimmy"
print(person["first_name"])


list_of_keys = ["address", "age"]

for key in list_of_keys:
    person.pop(key)
print(person)
