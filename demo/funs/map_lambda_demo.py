# def reverse(s):
#     return s[::-1].upper()


data = ['ABc', 'pQr', 'XY']

for s in map(lambda s: s[::-1].upper(), data):
    print(s)
