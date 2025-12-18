# Print unique chars from 5 strings

names = ["Bill", "Joe", 'Steve', "Jack", "Andy"]

un_chars = set()   # Empty set
for name in names:
    un_chars = un_chars | set(name)
    print(un_chars)


