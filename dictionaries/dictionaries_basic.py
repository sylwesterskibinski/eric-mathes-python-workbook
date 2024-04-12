famous_person1 = {'first_name':'Michael','last_name':'Jordan','age':'55','city':'Chicago'}
famous_person2 = {'first_name':'Adam','last_name':'Malysz','age':'54','city':'Wisla'}
famous_person3 = {'first_name':'Joe','last_name':'Biden','age':'73','city':'Washinghton'}

peoples = [famous_person1,famous_person2,famous_person3]

for people in peoples:
    for key,value in people.items():
        print(key,value)


programming_words = {'tuple':'immutable object','variable':'value that we are assigning to',"python":"programming language"}

persons_for_questionnaire = {"maciek","ania","oliwia"}

persons_responded_to_questionnaire = {"maciek","malgosia","ania"}

for person in persons_for_questionnaire:
    if person in persons_responded_to_questionnaire:
        print(f"Thank you for fulfilling questionnaire {person}")
    else:
        print(f"We kindly ask you to fulfill questionnaire {person}")

for key,value in programming_words.items():
    print(f"{key} : {value}")

rivers = {"Nile":"Egypt","Vistula":"Poland","Thames":"United Kingdom"}

for key,value in rivers.items():
    print(f"{key} is located in {value}")


favourite_places = {"Eryk":["New York","Montreal","Moscow"],"Anna":["Warsaw","Chicago","Seattle"]}

for key,value in favourite_places.items():
    places = ', '.join(value)
    print(key,places)