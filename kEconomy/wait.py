from time import sleep as wait


wait(1)
print('Loading Scripts..')
wait(5)
print('Scripts Loaded!')
wait(2)
print('Loading Terminal..')
wait(5)
print('Terminal Loaded!')
wait(2)
print('Loading User Info..')
wait(7)
print('User Info Loaded!')
wait(2)
print('Connecting Files..')
wait(8)
print('Files Connected!')
wait(2)
print('Connecting..')
wait(6)
print('Connected!')
wait(2)
password = input('Please enter your password: ')


if password == "1helesa":
    import app
else:
    print('Invalid Password.')
