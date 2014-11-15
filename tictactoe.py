#Tic Tac Toe

import random

def drawBoard(board):
    print('  | |  ')
    print(' '+board[7]+'|'+board[8]+'|'+board[9])
    print('  | |  ')
    print('------------')
    print('  | |  ')
    print(' '+board[4]+'|'+board[5]+'|'+board[6])
    print('  | |  ')
    print('------------')
    print('  | |  ')
    print(' '+board[1]+'|'+board[2]+'|'+board[3])
    print('  | |  ')

def inputPlayerLetter():
    letter=' '
    while not(letter == 'X' or letter == 'O'):
        print("Do you want to be X or O?")
        letter=input().upper()
    if letter == "X":
        return ['X','O']
    else:
        return ['O','X']

def whogoesFirst():
    if random.randint(0,1)==0:
        return 'Computer'
    else:
        return 'player'

def playagain():
    print("Do you want to play again:Yes or No?")
    return input().lower().startswith('y')

def MakeMove(board,letter,move):
    board[move]=letter

def iswinner(bo,le):
    return ((bo[7]==le and bo[8]==le and bo[9]==le) or (bo[4]==le and bo[5]==le and bo[6]==le) or (bo[1]==le and bo[2]==le and bo[3]==le) or (bo[7]==le and bo[4]==le and bo[1]==le) or (bo[8]==le and bo[5]==le and bo[2]==le) or (bo[9]==le and bo[6]==le and bo[3]==le) or (bo[7]==le and bo[5]==le and bo[3]==le) or (bo[9]==le and bo[5]==le and bo[1]==le))

def getBoardCopy(board):
    dupeboard=[]
    for i in board:
        dupeboard.append(i)
    return dupeboard

def isspacefree(board,move):
    return board[move]==' '

def getplayermove(board):
    move=''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isspacefree(board,int(move)):
        print("What is your next move[1-9]?")
        move=input()
        return int(move)

def chooseRandommove(board,moveslist):
    possiblemoves=[]
    for i in moveslist:
        if isspacefree(board,i):
            possiblemoves.append(i)
    if len(possiblemoves)!=0:
        return random.choice(possiblemoves)
    else:
        return None

def getcompmove(board,computerletter):
    if computerletter=='X':
        playerletter='O'
    else:
        playerletter='X'
    for i in range(1,10):
        copy=getBoardCopy(board)
        if isspacefree(copy,i):
            MakeMove(copy,playerletter,i)
            if iswinner(copy,playerletter):
                return i
    move=chooseRandommove(board,[1,3,7,9])
    if move != None:
        return move

    if isspacefree(board,5):
        return 5

    return chooseRandommove(board,[2,4,6,8])

def isBoardFull(board):
    for i in range(1,10):
        if isspacefree(board,i):
            return False
    return True

print("Welcome to Tic Tac Toe!")

while True:
    theBoard=[' ']*10
    playerletter,computerletter=inputPlayerLetter()
    turn=whogoesFirst()
    print("The "+turn+" will go first")
    gameisplaying=True

    while gameisplaying:
        if turn=='player':
            drawBoard(theBoard)
            move=getplayermove(theBoard)
            MakeMove(theBoard,playerletter,move)
            if iswinner(theBoard,playerletter):
                drawBoard(theBoard)
                print("Hooray,you have won the game!!")
                gameisplaying=False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn="computer"
        else:
            move=getcompmove(theBoard,computerletter)
            MakeMove(theBoard,computerletter,move)
            if iswinner(theBoard,computerletter):
                drawBoard(theBoard)
                print("The computer has won the game!!")
                gameisplaying=False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn="player"
    if not playagain():
        break
