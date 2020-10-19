#  Variables
pin = '9311'
max_attempts = 3
attempts_made = 0


# Everytime the user types a pin, the variable "attempts_made" will increase by 1 unit

name = input("Name: ")
print(f'Hey {name}, you have 3 attempts to guess the pin and unlock the system')

while attempts_made < max_attempts:

    ask_pin = input('Insert pin: ')
    if len(ask_pin) != 4:
        print('Pin contains 4 numbers')

    elif ask_pin != pin:
        print('Oops! System still locked, try again')
        attempts_made += 1

    elif ask_pin == pin:
        print(f'System unlocked, good job {name}!')
        break

