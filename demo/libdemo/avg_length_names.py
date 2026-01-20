# Find out avgerage length of names in names.txt

with open("names.txt", "rt") as f:
    total_len = 0
    lines = f.readlines()
    for name in lines:
        total_len += len(name) - 1

    print(total_len // len(lines))


