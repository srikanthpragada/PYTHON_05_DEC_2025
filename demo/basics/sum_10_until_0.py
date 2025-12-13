# Take 10 numbers or until 0 is given and display the total

total = 0
for i in range(10):    # 0 to 9
    n = int(input("Enter a number [0 to stop] :"))
    if n == 0:
        break     # terminate loop
    total = total + n

print(total)

