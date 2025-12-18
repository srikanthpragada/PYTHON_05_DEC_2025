
s = "hello"

d = {}  # Empty dict

for c in s:
    if c not in d:
        d[c] = ord(c)

print(d)

