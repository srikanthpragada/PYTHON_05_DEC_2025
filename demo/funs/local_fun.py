g = 100    # Global variable

def f1():
    a = 1   # Enclosing variable
    # local function
    def f2():
        b = 2    # Local variable
        nonlocal a
        a = 10   # ref to enclosing variable a
        print(g, a, b)

    f2()
    print(g, a)

f1()





