import secrets
import string
import pyperclip


al = string.ascii_letters + string.digits


def inputHandler():
    while True:
        try:
            n = input('How many characters? ')
            if int(n) > 0:
                return int(n)
            else:
                raise ValueError
        except ValueError:
            print('Please only enter positive integers.')


pyperclip.copy(''.join(secrets.choice(al) for i in range(inputHandler())))
print('Password has been copied to your clipboard!')
