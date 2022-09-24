while True:
    name = input('Enter your name : ')
    if name != 'steve':
        # print('hello Steve')
        continue
    password = input('Enter your PassWord : ')
    if password == 'pass':
        break
print('Thank You')