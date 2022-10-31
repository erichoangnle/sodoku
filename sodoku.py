import random


def generate_initial_board():
    """
    Generate empty board with 3 diagonal boxes filled in with number from 1 to 9
    in random order. Since diagonal boxes are independent of each other row and 
    column wise, no need to check for safety in row and column.
    """

    board = [[0 for _ in range(9)] for _ in range(9)]
    x = [0, 3, 6, 9]

    for k in range(3):

        numbers = [_ for _ in range(1, 10)]
        random.shuffle(numbers)
        for i in range(x[k], x[k + 1]):
            for j in range(x[k], x[k + 1]):
                board[i][j] = numbers[0]
                numbers.pop(0)

    return board


def is_safe(board, number, i, j):
    """
    Check if number placement doesn't break game rules.
    """

    # Check for row
    for k in range(9):
        if k != j:
            if number == board[i][k]:
                return False

    # Check for column
    for k in range(9):
        if k != i:
            if number == board[k][j]:
                return False

    # Check for box
    for x in range((i // 3) * 3, (i // 3) * 3 + 3):
        for y in range((j // 3) * 3, (j // 3) * 3 + 3):
            if x != i and y != j:
                if number == board[x][y]:
                    return False

    return True


def fill_board(board, i, j):
    """
    Create a solved sodoku puzzle.
    """

    if i == 8 and j == 9:
        return True

    if j == 9:
        i += 1
        j = 0

    if board[i][j] != 0:
        return fill_board(board, i, j + 1)

    for number in range(1, 10):

        if is_safe(board, number, i, j):

            board[i][j] = number
            if fill_board(board, i, j + 1):
                return True

        board[i][j] = 0

    return False


sodoku = generate_initial_board()
fill_board(sodoku, 0, 0)
for row in sodoku:
    print(row)