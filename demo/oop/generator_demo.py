#Generator
def squares(num):
    for n in range(1, num + 1):
        yield n * n

s = squares(5)
print(type(s))
print(next(s))
print(next(s))
for v in s:
    print(v)

