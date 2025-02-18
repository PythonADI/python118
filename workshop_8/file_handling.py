f = open("./workshop_8/text.txt", "r")

# print(f.read())
for line in f.readlines():
    print(line, end="")
f.close()


with open("./workshop_8/dat.txt", "w") as f:
    f.write("Testing")

with open("./workshop_8/dat_2.txt", "a") as f:
    f.write("Testing")


try: 
    with open("./test.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("This file does not exist")
    