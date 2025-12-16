
st  = "20,44,55,a,60"

parts = st.split(',')

total = 0
for p in parts:
    if p.isdigit():
        total += int(p)

print(total)
