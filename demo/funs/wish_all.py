def wish(*users, message = 'Hi'):
    for u in users:
        print(message, u)


wish('Bill', 'Tom', 'Bruce', message='Hi')
wish('Mark')
wish()

print(10, 20, 30, sep='*')
