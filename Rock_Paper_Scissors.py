import random, sys
print('ROCK, PAPER, SCISSORS (BO10)')
Wins = 0
Losses = 0
Ties = 0
while True:
    while True:
        print('%s Wins, %s Losses, %s Ties' %(Wins, Losses, Ties))
        while True:
            print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
            playerMove = input()
            if playerMove == 'q':
                sys.exit()
            elif playerMove == 'r' or playerMove == 'p' or playerMove == 's':
                break
            else:
                print('you did not enter a valid input')
                continue
        if playerMove == 'r':
            print('Rock versus...')
        elif playerMove == 'p':
            print('Paper versus...')
        elif playerMove == 's':
            print('Scissors versus...')
        randomNumber = random.randint(1,3)
        randomNumber == 1
        if randomNumber == 1:
            computerMove = 'r'
            print('ROCK')
        elif randomNumber == 2:
            computerMove = 'p'
            print('PAPER')
        elif randomNumber == 3:
            computerMove = 's'
            print('SCISSORS')
        if playerMove == computerMove:
            print('Tie!')
            Ties = Ties + 1
        elif playerMove == 'r' and computerMove == 's':
            print('You Win!')
            Wins = Wins + 1
        elif playerMove == 'p' and computerMove == 'r':
            print('You Win!')
            Wins = Wins + 1
        elif playerMove == 's' and computerMove == 'p':
            print('You Win!')
            Wins = Wins + 1
        elif playerMove == 'r' and computerMove == 'p':
            print('You Lose!')
            Losses = Losses + 1
        elif playerMove == 'p' and computerMove == 's':
            print('You Lose!')
            Losses = Losses + 1
        elif playerMove == 's' and computerMove == 'r':
            print('You Lose!')
            Losses = Losses + 1
        if Wins + Losses + Ties == 10:
            break
    if (Wins >= Losses) and (Wins >= Ties):
        print('You have won the game!!')
    elif (Losses >= Wins) and (Losses >= Ties):
        print('You lost the game!!')
    elif (Ties >= Losses) and (Ties >= Wins):
        print("The final score is a tie!!!")
    print('Do you want to play again? Please enter "y" if you do!')
    playerchoice = input()
    if playerchoice == 'y':
        Wins = 0
        Losses = 0
        Ties = 0
        continue
    else:
        print('Thank you for playing')
        nut=input()



