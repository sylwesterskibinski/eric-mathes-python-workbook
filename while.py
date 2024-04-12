active = True

while active:
    user_age = input("Please provide your age: ")
    if user_age == "koniec":
        break
    elif int(user_age) < 3:
        print("Ticket is free.")
    elif int(user_age) >= 3 and int(user_age) < 12:
        print("Ticket costs 10 zl")
    elif int(user_age) != "koniec":
        print("Ticket costs 15 zl")