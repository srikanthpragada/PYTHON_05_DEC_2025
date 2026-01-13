import sys

g = (n * n for n in range(1, 10000))
print(type(g))
print(sys.getsizeof(g))

l = [n * n for n in range(1, 10000)]
print(type(l))
print(sys.getsizeof(l))