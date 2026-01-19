names = ['George', 'Larry', 'Mark', 'Richards', "Kevin"]

f = open("names.txt", "wt")  # create file

for name in names:
    f.write(name + "\n")

f.close()



