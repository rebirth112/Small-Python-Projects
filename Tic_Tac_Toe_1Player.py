import random
playerMoveList = ['1','2','3','4','5','6','7','8','9']
turn = 'X'
count = 0
theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


while True:
    printBoard(theBoard)
    print('Move on which space?')
    move = input()
    if theBoard[move] == ' ':
        playerMoveList.remove(move)
        theBoard[move] = turn
        count += 1
    else:
        print('this is filled already. pick something else')
        continue
    if playerMoveList != []:
        computerMove = random.choice(playerMoveList)
        playerMoveList.remove(computerMove)
        theBoard[computerMove] = '0'
        count += 1
    else:
        pass
    if count >= 5:
        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(theBoard['7'] + ' won')
            x=input()
        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(theBoard['4'] + ' won')
            x=input()
        elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(theBoard['1'] + ' won')
            x=input()
        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(theBoard['1'] + ' won')
            x=input()
        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(theBoard['2'] + ' won')
            x=input()
        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(theBoard['3'] + ' won')
            x=input()
        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(theBoard['7'] + ' won')
            x=input()
        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(theBoard['1'] + ' won')
            x=input()
        elif count >= 9:
            print('tie!')
            x=input()

