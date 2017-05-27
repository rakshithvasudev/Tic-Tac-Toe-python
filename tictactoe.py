from random import randint

# All the winning positions to check and validate
winningPositions = [[0, 0, 0, 1, 0, 2], [0, 0, 1, 0, 2, 0],
                    [2, 0, 2, 1, 2, 2], [2, 2, 1, 2, 0, 2], [2, 0, 1, 1, 0, 2], [2, 0, 1, 1, 0, 2]]
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


def setUserPosition(currentrow, currentcol, playername):
    """Set the location of the cursor to the required position"""
    if gameBoard[currentrow][currentcol] == 'X':
        gameBoard[currentrow][currentcol] = playername
        global timesMoved
        timesMoved += 1
        return True
    else:
        print("Can't Change already used cell ")
    return False


def computerPlay():
    """This is the computer's turn to set the position it wants"""
    randoms = generateTwoRandoms()

    # Generate randoms as long as the cell matching the
    # random is 'X'
    while gameBoard[randoms[0]][randoms[1]] != 'X' and timesMoved < 10:
        randoms = generateTwoRandoms()

    setUserPosition(randoms[0], randoms[1], 'C')


def generateTwoRandoms():
    randomRow = randint(0, 2)
    randomCol = randint(0, 2)
    return [randomRow, randomCol]


def hasWon():
    """Traverse through the winning Sequences and 
    check if the same player has equal to 3 occurrences. """

    for winningPosition in winningPositions:
        userScore = {'C': 0, 'user': 0}
        condition = gameBoard[winningPosition[0]][winningPosition[1]]
        if condition == 'C':
            userScore['C'] += 1
        if condition != 'X' and condition != 'C':
            userScore['user'] += 1

        condition1 = gameBoard[winningPosition[2]][winningPosition[3]]
        if condition1 == 'C':
            userScore['C'] += 1
        if condition1 != 'X' and condition1 != 'C':
            userScore['user'] += 1

        condition2 = gameBoard[winningPosition[4]][winningPosition[5]]
        if condition2 == 'C':
            userScore['C'] += 1
        if condition2 != 'X' and condition2 != 'C':
            userScore['user'] += 1

        # print(userScore)
        if userScore['user'] == 3:
            print("You won the game!")
            global gameWon
            gameWon = True

        elif userScore['C'] == 3:
            print("Computer Won!")
            gameWon = True
    return True


if __name__ == '__main__':
    playerName = input("Please enter Name: ")
    print("Your name will be referred to as :", playerName[0].upper())
    print("The following is the board: ")
    generateBoard()
    printBoard()

    while not gameWon:
        if timesMoved >= 6:
            if hasWon():
                break

        print("Where do you want the move to be? Enter an inclusive value between 1 and 3.")
        row = int(input("Enter row: ")) - 1
        col = int(input("Enter col: ")) - 1
        if setUserPosition(row, col, playerName[0].upper()):
            print("Computer is playing now")
            if timesMoved < 9:
                computerPlay()
        printBoard()
        print("timesMoved: ", timesMoved)

# if __name__ == '__main__':
#     userScore = {'C': 0, 'user': 0}
#     generateBoard()
#     for winningPosition in winningPositions:
#         condition = gameBoard[winningPosition[0]][winningPosition[1]]
#         if condition == 'C':
#             userScore['C'] += 1
#         if condition != 'X' and condition != 'C':
#             userScore['user'] += 1
#
#         condition1 = gameBoard[winningPosition[1]][winningPosition[2]]
#         if condition1 == 'C':
#             userScore['C'] += 1
#         if condition1 != 'X' and condition1 != 'C':
#             userScore['user'] += 1
#
#         condition2 = gameBoard[winningPosition[2]][winningPosition[3]]
#         if condition2 == 'C':
#             userScore['C'] += 1
#         if condition2 != 'X' and condition2 != 'C':
#             userScore['user'] += 1
#
#     print(userScore)
