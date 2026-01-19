customers = []

with open("customers.txt", "rt") as f:
    for line in f.readlines():
        name, mobile = line.strip().split(",")
        customers.append( (name, mobile))  # add tuple to list

for name, mobile in sorted(customers):
    print(f"{name:20}  {mobile}")

