# keyword-only args
def wish(*, name, message):
    print(message, name)


#wish('Andy', 'Hi')  # positional
wish(message = 'Hello', name = 'Anders')  # Keyword



