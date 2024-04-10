users = ["admin","sylwek872","anita298","bronek120","jola23"]

if users:
    for user in users:
        if user == "admin":
            print("Welcome admin! Would you like to see today report?")
        else:
            print(f"Welcome {user}! Thank you for logging again!")
else:
    print("We need to find some users!")

current_users = ["pepe","lolol","bubs","popos","ceeepeee"]

new_users = ["ovn","iewqb","pepe"]

current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry, this username is occupied.")
    else:
        print("This username is available")

numbers = list(range(0,11))
print(numbers)

for number in numbers:
    if number > 3:
        print(f"{number}th")
    if number == 2:
        print(f"{number}nd")
    if number == 1:
        print(f"{number}st")


