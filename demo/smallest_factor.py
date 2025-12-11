# Accept a number and display smallest factor other than 1
# For prime numbers, we display number as smallest factor

num = int(input("Enter a number:"))

for n in range(2, num // 2 + 1):
    if num % n == 0:
        print(n)
        break
else:
    print(num)





