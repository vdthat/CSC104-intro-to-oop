class User:
    def register(self, name, phone, email, password):
        return name
    def login(self,email,password):
        if email=="test@mail.com" and password=="abc":
            return True
        else:
            return False