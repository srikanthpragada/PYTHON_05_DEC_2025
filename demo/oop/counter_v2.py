class Counter:
    # constructor
    def __init__(self, value = 0):
        # Object Attributes
        self.value = value
        self.initvalue = value

    # Methods
    def inc(self, step = 1):
        self.value += step

    def dec(self, step = 1):
        self.value -= step

    def getvalue(self):
        return self.value

    def reset(self):
        self.value = self.initvalue

c1 = Counter(100)  # create an object
c1.inc()  # call method
c1.inc(5)
c1.dec(2)
c1.reset()
print(c1.getvalue())

