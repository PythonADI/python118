class User:
    def __init__(self, name, age, email):
        self.name = name 
        self.age = age
        self.email = email
        
    def print_user(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}")
        
        
new_user = User("Nodo", 23, "nodogelashvili99@gmail.com")
new_user.print_user()