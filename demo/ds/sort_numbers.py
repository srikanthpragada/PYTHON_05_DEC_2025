# Take numbers from user until 0 and sort them

l = []   # Empty list

while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    l.append(num)

l.sort()

for n in l:
    print(n, end = ' ')





