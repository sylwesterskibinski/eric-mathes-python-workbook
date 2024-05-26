class Restaurant:
    def __init__(self,restaurant_name,cuisine_type,number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}, {self.number_served}")

    def open_restaurant(self):
        print("Godziny otwarcia od 8 do 20")

    def set_number_served(self,update_served):
        self.number_served = update_served

    def increment_number_served(self,clients):
        self.number_served += clients

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavours = ['chocolate','strawberry','forest']

    def show_ice_flavours(self):
        for i in self.flavours:
            print(i)


restaurant = Restaurant("Concordia","Italian")
restaurant.open_restaurant()
restaurant.set_number_served(7)
restaurant.increment_number_served(2)
restaurant.describe_restaurant()

first_ice_cream_stand = IceCreamStand()
first_ice_cream_stand.show_ice_flavours()

restaurant_2 = Restaurant("Pepelolo","Greek")
restaurant_3 = Restaurant("PizzaPasta", "Polish",5)
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

class User:
    def __init__(self,first_name,last_name,password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def describe_user(self):
        print(f"{self.first_name},{self.last_name},{self.password}")

    def greet_user(self):
        print(f"Hello {self.first_name}!")

user1 = User("Maciek","Nowak","MN123")
user2 = User("Antoni","Bomba","Bobololo")

user1.describe_user()
user2.describe_user()
user1.greet_user()
user2.greet_user()