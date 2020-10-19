started = False
while True:
    command = input('> ').lower()
    if command == "start":
        if started:
            print('Already started!')
        else:
            started = True #Is the car started?
            print('Car started... Ready to go!')
    
    elif command == "help": #Display helps command
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit the game')

    elif command == "stop": #Stops car
        if not started:
            print('Cannot stop twice!')
        else:
            started = False
            print('Car has stopped')
   
    elif command == "quit": #Exits game
        break
    else:
        print('I do not get that')
