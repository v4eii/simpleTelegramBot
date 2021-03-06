class User:
    name = ""
    surname = ""
    age = 0
    username = ""
    personal_links = {}

    def __init__(self, name, surname, age, username, personal_links):
        self.name = name
        self.surname = surname
        self.age = age
        self.username = username
        self.personal_links = personal_links

    def __str__(self):
        return self.name + " " + self.surname