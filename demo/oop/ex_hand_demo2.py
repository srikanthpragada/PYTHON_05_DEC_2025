
data = input("Enter a number :")
try:
    num = int(data)
    print(100 / num)
except Exception as e:
    print('Error :' + str(e))

print('The End!')