#Create Game Board
board = [
    " ", "|", " ", "|", " ",  "\n",
    "-", "+", "-", "+", "-",  "\n",
    " ", "|", " ", "|", " ",  "\n",
    "-", "+", "-", "+", "-",  "\n",
    " ", "|", " ", "|", " ",  "\n",
]

#Possible Moves
tl = ["tl", 0]
tm = ["tm", 2]
tr = ["tr", 4]
ml = ["ml", 12]
mm = ["mm", 14]
mr = ["mr", 16]
bl = ["bl", 24]
bm = ["bm", 26]
br = ["br", 28]

pm = [
    tl, tm, tr,
    ml, mm, mr,
    bl, bm, br
]

#Winning conditions
s1 = ["tl","tm","tr"]
s2 = ["ml","mm","mr"]
s3 = ["bl","bm","br"]
s4 = ["tl","ml","bl"]
s5 = ["tm","mm","bm"]
s6 = ["tr","mr","br"]
s7 = ["tl","mm","br"]
s8 = ["bl","mm","tr"]
wc = [s1,s2,s3,s4,s5,s6,s7,s8]

#Global Variables
x = "X"
o = "O"
xmoves = []
omoves = []
executed = []
currentplayer = x
xwins = 0
owins = 0
ties = 0
score = [xwins, owins, ties]

#Place Current Move on Board
def move(currentmove, currentplayer):

    if xmoves == any(wc):
        print("X Wins!")

    for m in pm:
        if currentmove == m[0]:
            if currentmove in executed:
                print("\n" + "".join(board))
                print("That move has already been played!\n")
                next(currentplayer)
            executed.append(currentmove)
            board[m[1]] = currentplayer
            print("\n" + "".join(board))
            if currentplayer == x:
                xmoves.append(currentmove)
                currentplayer = o
            else:
                omoves.append(currentmove)
                currentplayer = x
            next(currentplayer)
            return
    print("\n" + "".join(board))
    print("Error: Invalid move\n")
    next(currentplayer)

#Change player
def next(currentplayer):
#Check to see if anyone wins
    global xwins, owins, ties, score
    for condition in wc:
        if all(elem in xmoves for elem in condition):
            print("X Wins!\n")
            xwins += 1
            score = [xwins, owins, ties]
            print("X: {} | O: {} | T: {} \n".format(*score))
            newgame()
        elif all(elem in omoves for elem in condition):
            print("O Wins!\n")
            owins += 1
            score = [xwins, owins, ties]
            print("X: {} | O: {} | T: {} \n".format(*score))
            newgame()
        elif len(executed) == 9:
            print("It's a tie!\n")
            ties += 1
            score = [xwins, owins, ties]
            print("X: {} | O: {} | T: {} \n".format(*score))
            newgame()
#Get next move
    currentmove = input("Where would you like to place an " + currentplayer + "?\n(options: tl, tm, tr, ml, mm, mr, bl, bm, br)\n")
    move(currentmove, currentplayer)
    

def newgame():
    global xmoves, omoves, executed, currentplayer, board
    option = input("Would you like to play again?\noptions: y or n\n")
    if option == "y":
        xmoves = []
        omoves = []
        executed = []
        board = [
            " ", "|", " ", "|", " ",  "\n",
            "-", "+", "-", "+", "-",  "\n",
            " ", "|", " ", "|", " ",  "\n",
            "-", "+", "-", "+", "-",  "\n",
            " ", "|", " ", "|", " ",  "\n",
        ]
        print("\n" + "".join(board))
        next(currentplayer)
    elif option == "n":
        print("\nThanks for playing!\n")
        return
    else:
        print("Invalid response")
        newgame()
        


#Initiate game with current variables
print("\n" + "".join(board))
next(currentplayer)