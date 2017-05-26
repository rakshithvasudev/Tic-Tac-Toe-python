# All the winning positions to check and validate
winningPositions = [[[0, 0], [0, 1], [0, 2]], [[0, 0], [1, 0], [2, 0]],
                    [[2, 0], [2, 1], [2, 2]], [[2, 2], [1, 2], [0, 2]],
                    [[2, 0], [1, 1], [0, 2]], [[2, 0], [1, 1], [0, 2]]]
# Game board {List} that has to be setup.
gameBoard = []
# Init with no winning.
gameWon = False
# Number of times the X has been replaced.
timesMoved = 0


def generateBoard():
    """ Generates 3 * 3 game board """
    for row in range(3):
        gameBoard.append([])
        for col in range(3):
            gameBoard[row].append("X")


def printBoard():
    """Print the generated game board"""
    for row in gameBoard:
        # print the board such that every element of the row must be
        # in its appropriate position by joining the row list.
        print(" ".join(row))


def setPosition(currentrow, currentcol, playername):
    """Set the location of the cursor to the required position"""
    if gameBoard[currentrow][currentcol] == 'X':
        gameBoard[currentrow][currentcol] = playername
        global timesMoved
        timesMoved += 1
    else:
        print("Can't Change already used cell ", [currentrow+1][currentrow+1])


if __name__ == '__main__':
    playerName = input("Please enter Name: ")
    print("Your name will be referred to as :", playerName[0].upper())
    print("The following is the board: ")
    generateBoard()
    printBoard()

    while timesMoved < 6:
        print("Where do you want the move to be? Enter an inclusive value between 0 and 3.")
        row = int(input("Enter row: ")) - 1
        col = int(input("Enter col: ")) - 1
        setPosition(row, col, playerName[0].upper())
        printBoard()
        print("timesMoved: ", timesMoved)


