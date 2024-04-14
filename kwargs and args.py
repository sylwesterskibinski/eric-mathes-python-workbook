'''def zamowienie_kanapek(*skladniki):
    for skladnik in skladniki:
        print(skladnik)

zamowienie_kanapek("szynka","ser")'''

'''def build_profile(name,surname,**user_info):
    user_info['first_name'] = name
    user_info['last_name'] = surname
    return user_info

user_profile = build_profile("Sylwester","Skibiński",location="Poznan",language="Polish")
print(user_profile)'''

def car(marka,model,**dodatkowe_info):
    dodatkowe_info['marka'] = marka
    dodatkowe_info['model'] = model
    return dodatkowe_info

car = car("Subaru","Impreza",offroad=True)
print(car)
