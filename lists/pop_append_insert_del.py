guests = ['Michael Jordan', 'Marie Curie', 'Nicolaus Copernicus']

invitation_for_michael = f"You're invited {(guests[0].split())[0]}"
invitation_for_marie = f"You're invited {(guests[1].split())[0]}"
invitation_for_nicolaus = f"You're invited {(guests[2].split())[0]}"
print(invitation_for_michael)
print(invitation_for_marie)
print(invitation_for_nicolaus)
print(f"{guests[2]} won't be able to come")
guests.pop(2)
guests.append("Niels Bohr")
invitation_for_niels = f"You're invited {(guests[2].split())[0]}"
print(invitation_for_niels)
print("Hooray, we found bigger table!")
guests.insert(0,"Mahatma Gandhi")
guests.insert(2,"Lech Walesa")
guests.append("Neil Armstrong")

for i in guests:
    print(f"You're invited {i.split()[0]}")

print("We are really sorry, but we can invite only two persons")
popped_person1 = guests.pop()
print(f"We're really sorry {(popped_person1.split())[0]} but we cannot invite you")
popped_person2 = guests.pop()
print(f"We're really sorry {(popped_person2.split())[0]} but we cannot invite you")
popped_person3 = guests.pop()
print(f"We're really sorry {(popped_person3.split())[0]} but we cannot invite you")
popped_person4 = guests.pop()
print(f"We're really sorry {(popped_person4.split())[0]} but we cannot invite you")

for i in guests:
    print(f"You're invited {i.split()[0]}")

del guests[0]
del guests[0]

print(guests)