
data = input("Enter a number :")
try:
    num = int(data)
    print(100 / num)
except ValueError as e:
    print('Sorry! Invalid Number! --> ' + str(e))
except ZeroDivisionError:
    print('Zero is not valid!')

print('The End!')