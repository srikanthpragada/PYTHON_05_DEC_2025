d = {1: 125, 2: 100, 3: 230, 5: 55, 4: 155}

# Sort dict by values
for t in sorted(d.items(), key = lambda t : t[1]):
    print(t)
