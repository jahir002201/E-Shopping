class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.__password = password
    
    def check(self, password):
        return self.__password == password