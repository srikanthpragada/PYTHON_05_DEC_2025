# Take a number and print math table

num = int(input("Enter a number :"))

for v in range(1, 11):
    print(f"{num} * {v:2} = {num * v:5}")