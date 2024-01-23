people = {
    "Dennis": "0277441627",
    "Ben": "0246210066"
}

name = input("Name: ")
if name in people:
    number = people[name]
    print(f"Number: {number}")
