largest = ""
while True:
    name = input("Enter name [end to stop]:")
    if name.lower() == 'end':
        break
    if name > largest:
        largest = name

print('Largest name :', largest)
