print("Pastrami is no longer available!")

sandwich_orders = ["Pastrami","Pastrami","Pastrami","Ham and cheese","Garlic butter"]

finished_sandwiches = []

for sandwich in sandwich_orders:
    while sandwich == "Pastrami":
        sandwich_orders.remove("Pastrami")
else:
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)

