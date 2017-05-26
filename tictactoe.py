winningPositions = [[[0, 0], [0, 1], [0, 2]], [[0, 0], [1, 0], [2, 0]],
                    [[2, 0], [2, 1], [2, 2]], [[2, 2], [1, 2], [0, 2]],
                    [[2, 0], [1, 1], [0, 2]], [[2, 0], [1, 1], [0, 2]]]

gameBoard = []


def generateBoard():
    for row in range(3):
        gameBoard.append([])
        for col in range(3):
            gameBoard[row].append("X")


def printBoard():
    for row in gameBoard:
        print(
            " ".join(row))


if __name__ == '__main__':
    generateBoard()
    printBoard()
    #     var = input("Please enter something: ")
    #     print("you entered", var)
