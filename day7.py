password = input('enter your password: ')

if len(password) < 5:
    print('too short')
elif len(password) > 15:
    print('too long')
else:
    print('successful')
