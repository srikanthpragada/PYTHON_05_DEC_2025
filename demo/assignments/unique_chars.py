s1 = "rust"
s2 = "javascript"

unique_chars = []
for c in s1 + s2:
    if c not in unique_chars:
        unique_chars.append(c)

print(unique_chars)
