s = "how do you do"

chars = {c: s.count(c) for c in set(s)}
print(chars)
