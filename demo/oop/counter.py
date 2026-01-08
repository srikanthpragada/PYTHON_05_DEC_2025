class Counter:
    # constructor
    def __init__(self):
        # Object Attributes
        self.value = 0

    # Methods
    def inc(self):
        self.value += 1

    @property
    def currentvalue(self):
        return self.value


c1 = Counter()  # create an object
c1.inc()  # call method
c1.inc()
print(c1.currentvalue)
#print(c1.value)
