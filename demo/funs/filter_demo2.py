def hasupper(st):
    for c in st:
        if c.isupper():
            return True

    return False


names = ['tom', 'jack', 'Henry', 'George', 'andy']

for n in filter(hasupper, names):
    print(n)