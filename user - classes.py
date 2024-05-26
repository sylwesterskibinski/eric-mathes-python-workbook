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

class Admin(User):
    def __init__(self, first_name, last_name, password,privileges=None):
        super().__init__(first_name, last_name, password)
    
    

    class Privileges():
        def __init__(self,privileges = None):
            if privileges is None:
                self.privileges = ['can_add_post','can_delete_post','can_ban_user']
            else:
                self.privileges = privileges
            
        def show_privileges(self):
            for privilege in self.privileges:
                print(privilege)

admin1 = Admin('Maciej','Nowak','MK123')
admin1.show_privileges()