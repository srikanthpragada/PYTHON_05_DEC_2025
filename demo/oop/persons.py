class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show(self):
        print('Name  : ', self.name)
        print('Email : ', self.email)

    @property
    def emailaddress(self):
        return self.email


class Student(Person):
    def __init__(self, name, email, course):
        super().__init__(name, email)
        self.course = course

    #Overriding
    def show(self):
        super().show()
        print('Course :', self.course)


s1 = Student("James", "james@gmail.com", "Generative AI")
s1.show()
print(s1.emailaddress) # comes from superclass as subclass doesn't have it