class Person:
    def __init__(self,name, email):
        self.name = name
        # private attribute
        self.__email = email

    def getemail(self):
        return  self.__email

p = Person('Mark', 'mark@gmail.com')
#print(p.__email)
print(p.name, p._Person__email)
