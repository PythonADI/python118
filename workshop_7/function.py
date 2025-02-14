import datetime
import time

plate = []
def prepare_khinkali(should_scream = True):
    if should_scream:
        print("-" * 10)
        print("ვიღებთ ცომს")
        print("ვიღებთ ხორცს")
        print("ხორცს ვდებ ცომზე")
        print("ნაოჭები გავუკეთე")

    time.sleep(0.1)
    return datetime.datetime.now()

def prepare_batch_of_khinkali(count = 20):
    print(f"I got an order of {count} khinkali")
    plate = []
    for _ in range(count):
        plate.append(prepare_khinkali(False))

    return plate

plate += prepare_batch_of_khinkali(10)


for timestamp in plate:
    dt = datetime.datetime.now() - timestamp
    # print(timestamp, type(timestamp))
    dt = dt.total_seconds() * 1000
    if (dt < 500):
        print(f"{timestamp} is hot")
    else:
        print(f"{timestamp}is cold")


for _ in range(5):
    timestamp = plate.pop()
    print(f"eating khinkali: {timestamp}")

print(f"We have {len(plate)} khinkali")

# plate = prepare_batch_of_khinkali(10)

# new_plate = prepare_batch_of_khinkali(10)
# for i in range(len(new_plate)):
#     plate.append(new_plate.pop())
# print(f"We have {len(new_plate)} khinkali on a new plate")

# plate.extend(prepare_batch_of_khinkali(10))
plate += prepare_batch_of_khinkali(10)



# for _ in range(10):
#     plate.append(prepare_khinkali())
print(f"We have {len(plate)} khinkali")
