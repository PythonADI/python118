import csv

records = []
with open("./workshop_9/test.csv") as f:
    # data = csv.reader(f)
    # for record in data:
    #     print(record)
    for line in f.readlines():
        print(line.strip().split(","))
        data = line.strip().split(",")
        id_, name, age = data
        print(id_, name, age)
        records.append({
            "id": int(id_),
            "name": name,
            "age": int(age)
        })

print(records)

        