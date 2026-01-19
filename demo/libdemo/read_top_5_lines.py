# Print top 3 lines from the file

with open("names.txt", "rt") as f:
    lineno = 1
    while True:
        line = f.readline()
        if line == "":  # EOF
            break

        print(line, end='')
        lineno += 1

        if lineno > 3:
            break
