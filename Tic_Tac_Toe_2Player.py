import random

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

for i in range(10):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    if theBoard[move] == ' ':
        count = count + 1
        theBoard[move] = turn
    else:
        print('this is filled already. pick something else')
        continue
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
    if count < 9:
        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(theBoard['7'] + ' won')
            break
        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(theBoard['4'] + ' won')
            break
        elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(theBoard['1'] + ' won')
            break
        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(theBoard['1'] + ' won')
            break
        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(theBoard['2'] + ' won')
            break
        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(theBoard['3'] + ' won')
            break
        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(theBoard['7'] + ' won')
            break
        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
            printBoard(theBoard)
            print("\nGame Over.\n")
            print(theBoard['1'] + ' won')
            break
    if count == 9:
        print("It's a tie!")
        break


