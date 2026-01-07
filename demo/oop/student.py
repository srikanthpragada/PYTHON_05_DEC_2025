class Student:
    total_fees = {'python' : 7500, 'genai' : 10000, 'aws' : 5000}

    def __init__(self, admno, name, course, feepaid = 0):
        self.admno = admno
        self.name = name
        self.course = course
        self.feepaid = feepaid

    def pay(self, amount):
        self.feepaid += amount

    def totalfee(self):
         return Student.total_fees[self.course]

    def getdue(self):
        return  self.totalfee() - self.feepaid

    def show(self):
        print('Admno  : ', self.admno)
        print('Name   : ', self.name)
        print('Course : ', self.course)
        print('Feepaid: ', self.feepaid)


s1 = Student(1, 'Tom', 'genai', 5000)
s1.show()
print(s1.getdue())

