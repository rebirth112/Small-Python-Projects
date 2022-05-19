game = 'yes'
while game == 'yes':
    import random
    randomnumber = random.randint(1,20)
    print('I am thinking of a number between 1 and 20.')
    for guessesTaken in range(1,999999999):
        print('Take a guess.')
        guessednumber = input()
        guessednumber = int(guessednumber)
        if guessednumber != randomnumber:
            if guessednumber >= randomnumber:
                print('Your guess is too high.')
                continue
            elif guessednumber <= randomnumber:
                print('Your guess is too low.')
                continue
        break
    print('Congrats bro, you guessed my number in ' + str(guessesTaken) + ' tries!')
    print('Play Again? Type "yes" if you do!')
    game = input()


