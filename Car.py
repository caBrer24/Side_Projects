started = False
while True:
    comma = input('> ').lower()
    if comma == "start":
        if started:
            print('Already started you foo')
        else:
            started = True #Is the car started?
            print('Car started... Ready to go!')
    elif comma == "help":
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit the game')

    elif comma == "stop":
        if not started:
            print('Cannot stop twice!')
        else:
            started = False
            print('Car has stopped')
    elif comma == "quit":
        break
    else:
        print('I do not get that')
