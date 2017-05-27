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

        if userScore['user'] == 3 and userScore['C'] == 3:
            print("Both won the game!")
            global gameWon
            gameWon = True
            return True

        elif userScore['user'] == 3:
            print("You won the game!")
            gameWon = True
            return True

        elif userScore['C'] == 3:
            print("Computer Won!")
            gameWon = True
            return True

        elif timesMoved == 9 and (userScore['user'] < 3 or userScore['C']) < 3:
            print("Draw Match")
            gameWon = True
            return True

    return False


if __name__ == '__main__':
    print("Welcome to Tic Tac Toe Game!")
    playerName = input("Please enter Name: ")
    while len(playerName) <= 3:
        playerName = input("Please enter Name having more than 3 characters: ")

    if playerName[0].lower() == 'c':
        playerName = playerName[1]

    playerName = playerName[0].upper()
    print("Your name will be referred to as :", playerName)
    print("The following is the board: ")
    generateBoard()
    printBoard()

    while not gameWon:
        # Check for winning condition only if there is than 6 or just 6 turns played.
        # checking before 6 is not optimal. It requires 3*2 turns to decide the winner.
        # Or Sometimes 5 is sufficient, only in few rare cases.
        if timesMoved >= 6:
            if hasWon():
                break

        print("Where do you want the next move to be? Enter an inclusive value between 1 and 3.")
        row = int(input("Enter row: ")) - 1
        col = int(input("Enter col: ")) - 1
        if setUserPosition(row, col, playerName):
            print("After Computer Playing the Results are:")
            print("'C' Represents the computer")
            if timesMoved < 9:
                computerPlay()
        printBoard()
