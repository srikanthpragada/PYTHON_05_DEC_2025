names = ['George', 'Larry', 'Mark', 'Richards', "Kevin"]

with open("names.txt", "wt") as f: # create file
    for name in names:
        f.write(name + "\n")



