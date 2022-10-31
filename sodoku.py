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


def row_safe(board, number, i, j):
    """
    Check if number is already in row.
    """
    for k in range(9):
        if k != j:
            if number == board[i][k]:
                return False
    return True


def column_safe(board, number, i, j):
    """
    Check if number is already in column.
    """
    for k in range(9):
        if k != i:
            if number == board[k][j]:
                return False
    return True


def box_safe(board, number, i, j):
    """
    Check if number is already in box.
    """
    for x in range((i // 3) * 3, (i // 3) * 3 + 3):
        for y in range((j // 3) * 3, (j // 3) * 3 + 3):
            if x != i and y != j:
                if number == board[x][y]:
                    return False
    return True

numbers = [_ for _ in range(1,10)]
def fill_board(board):

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for number in numbers:
                    if row_safe(board, number, i, j) and column_safe(board, number, i, j) and box_safe(board, number, i, j):
                        board[i][j] = number



def filled(board):

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True


board = generate_initial_board()
fill_board(board)
for row in board:
    print(row)
print(f"Board filled: {filled(board)}")