data = [(1, 50), (1, 70), (3, 66), (3, 90), (4, 45), (2, 80)]

students = {}

for rollno, marks in data:
    total = students.get(rollno, 0)
    students[rollno] = total + marks


print(students)

