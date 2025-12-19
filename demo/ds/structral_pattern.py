# d = {'name': 'Jack', 'email': 'jack@gmail.com'}
d = {'first': 'Scott'}
match d:
    case {'name': user}:
        print(f'Found name : {user}')
    case {'firstname': user}:
        print(f'Found firstname : {user}')
    case {'first': user}:
        print(f'Found first : {user}')
    case _:
        print('Username is not known!')
