import json

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.email}"

p = Person("gosling", "gosling@aws.com")
print(p.__dict__) # convert Person object to dict
print(json.dumps(p.__dict__))   # convert dict to JSON



