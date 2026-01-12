try:
    n = int(input("Enter number :"))
    print(100 / n)
except Exception:
    print('Invalid Number!')
else:
    print('Done')
finally:
    print('Finally!')

print('The End')
