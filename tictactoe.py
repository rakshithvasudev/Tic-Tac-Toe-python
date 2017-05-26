winningPositions = [[[0, 0], [0, 1], [0, 2]], [[0, 0], [1, 0], [2, 0]],
                    [[2, 0], [2, 1], [2, 2]], [[2, 2], [1, 2], [0, 2]],
                    [[2, 0], [1, 1], [0, 2]], [[2, 0], [1, 1], [0, 2]]]

gameBoard = []
gameWon = False


def generateBoard():
    for row in range(3):
        gameBoard.append([])
        for col in range(3):
            gameBoard[row].append("X")


def printBoard():
    for row in gameBoard:
        print(" ".join(row))



def setPosition(currentrow, currentcol, playername):
    gameBoard[currentrow][currentcol] = playername


if __name__ == '__main__':
    playerName = input("Please enter Name: ")
    print("Your name will be referred to as :", playerName[0])
    print("The following is the board: ")
    generateBoard()
    printBoard()
    print("Where do you want the move to be? ")
    row = int(input("Enter row: ")) - 1
    col = int(input("Enter col: ")) - 1
    setPosition(row, col, playerName[0])
    printBoard()
