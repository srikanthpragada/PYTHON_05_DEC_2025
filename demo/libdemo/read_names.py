
with open("names.txt", "rt") as f:
    for line in f.readlines():
        print(line.strip())  # remove newline at the end of line


