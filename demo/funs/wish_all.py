def wish(*users : list[str], message : str = 'Hi') -> None:
    """
    Prints the given message for each user
    :param *users: List of users
    :param message: Message to be printed. Default is Hi
    :return: None
    """
    for u in users:
        print(message, u)


wish('Bill', 'Tom', 'Bruce', message='Hi')
wish('Mark')
wish()

print(10, 20, 30, sep='*')

print(wish.__doc__)
