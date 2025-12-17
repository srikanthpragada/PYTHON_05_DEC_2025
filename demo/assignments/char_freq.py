# Char frequency
st = 'how do you do'

processed_chars = []

for c in st:
    if c not in processed_chars:
        print(c, st.count(c))
        processed_chars.append(c)

