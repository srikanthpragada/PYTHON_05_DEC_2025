def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def domath(n1, n2, func):
    print(func(n1, n2))


domath(10, 20, add)
domath(10, 20, mul)
#domath(10, 20, abs)


