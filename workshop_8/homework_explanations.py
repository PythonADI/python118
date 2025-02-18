# 1
MESSAGE_COST_PER_WORD = 0.01

def get_word_count(setence):
    # return setence.count(" ") + 1
    return len(setence.split(" "))


def get_price(message):
    return get_word_count(message) * MESSAGE_COST_PER_WORD


def get_total_price(messages):
    total_price = 0
    for message in messages:
        total_price += get_price(message)
    return total_price

def format_message(message, sender):
    if not message or not sender:
        return "Invalid Message"
    return f"From: {sender}\nMessage: {message}"


def format_messages(messages, sender):
    formatted_messages = []
    for message in messages:
        formatted_messages.append(format_message(message, sender))

    return formatted_messages

message = "Hello there friend"
messages = [
    "testing new function",
    "hello there jimmy",
    "this is a kinda long sentence, that has many words"
]
print(f'{get_word_count(message) = }')
print(f'{get_price(message) = }')
print(f'{get_total_price(["test", "haha", "LMAO"]) = }')
print(f'{format_message("Alice", "Hello James, How are") = }')

print("\n", "-" * 10, sep="")
for formated_message in format_messages(messages, "James"):
    print(formated_message)
