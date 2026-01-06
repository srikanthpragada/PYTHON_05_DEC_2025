class Course:
    def __init__(self, title):
        self.title = title


c1 = Course('Python Programming')
print(c1.__dict__)

print(getattr(c1, 'title'))
print(getattr(c1, 'duration', 24))

setattr(c1, 'duration', 36)
print(hasattr(c1, 'duration'))

delattr(c1, 'duration')
print(hasattr(c1, 'duration'))
