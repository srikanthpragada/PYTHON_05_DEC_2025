def show(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


show(a=10, b=20, c=100)
show(name='Python', author='Rossum')
