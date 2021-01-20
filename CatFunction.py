class Cat:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def cat_name(self):
        return self.name

    def cat_age(self):
        return self.age

    def cat_gender(self):
        return self.gender


class Client:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def client_name(self):
        return self.name

    def client_balance(self):
        return self.balance


class info(Client):
    def __init__(self, name, balance, adress, profession):
        self.adress = adress
        self.profession = profession
        Client.__init__(self, name, balance)

    def adress_1(self):
        return self.adress

    def prof_1(self):
        return self.profession


