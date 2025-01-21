import sys


def board_maker(board, output_file):
    # A list is taken by the function and is reorganized according to the function it will send.
    # Constraint values are added to the edges of the new board.
    new_board = []
    board[2].insert(0, '')
    board[2].append('')
    board[3].insert(0, '')
    board[3].append('')
    new_board.append(board[2])
    # The first element of the input is added to the first column, and the second element is added to the last column.
    for i in range(len(board)-4):
        board[4 + i].insert(0, board[0][i])
        board[4 + i].append(board[1][i])
        new_board.append(board[4 + i])
    new_board.append(board[3])
    #   The list is sent to the main game function.
    if not solve_sudoku_with_steps(new_board, output_file):
        output_file.write('No solution!')


def find_empty_location(board, empty_location):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 'L' or board[i][j] == 'U':
                empty_location[0] = i
                empty_location[1] = j
                return True
    return False


#   col = column
def is_valid(board, row, col, letter, empty_cell):
    #   Whether values can be placed in those cells is checked by the function, and if they can, the values are put in.
    if empty_cell == 'L':
        if letter == 'HB':
            if board[row][col - 1] == 'H' or board[row - 1][col] == 'H':
                return False
            if board[row][col + 1 + 1] == 'B' or board[row - 1][col + 1] == 'B':
                return False
            else:
                board[row][col] = 'H'
                board[row][col + 1] = 'B'
                return True
        if letter == 'BH':
            if board[row][col - 1] == 'B' or board[row - 1][col] == 'B':
                return False
            if board[row][col + 1 + 1] == 'H' or board[row - 1][col + 1] == 'H':
                return False
            else:
                board[row][col] = 'B'
                board[row][col + 1] = 'H'
                return True
        elif letter == 'NN':
            board[row][col] = 'N'
            board[row][col + 1] = 'N'
            return True
    if empty_cell == 'U':
        if letter == 'HB':
            if board[row][col - 1] == 'H' or board[row - 1][col] == 'H' or board[row][col + 1] == 'H':
                return False
            if board[row + 1][col - 1] == 'B':
                return False
            else:
                board[row][col] = 'H'
                board[row + 1][col] = 'B'
                return True
        if letter == 'BH':
            if board[row][col - 1] == 'B' or board[row - 1][col] == 'B' or board[row][col + 1] == 'B':
                return False
            if board[row + 1][col - 1] == 'H':
                return False
            else:
                board[row][col] = 'B'
                board[row + 1][col] = 'H'
                return True
        if letter == 'NN':
            board[row][col] = 'N'
            board[row + 1][col] = 'N'
            return True


def check_constraints(board):
    rows, cols = len(board), len(board[0])
    # Sequentially, first H than B numbers in rows and then columns are checked.
    for x in range(1, rows - 1):
        h_count_row = int(board[x][0])
        if 0 <= h_count_row != board[x].count('H'):
            return False

    for y in range(1, cols - 1):
        h_count_col = int(board[0][y])
        if 0 <= h_count_col != [board[x][y] for x in range(1, rows - 1)].count('H'):
            return False

    for x in range(1, rows - 1):
        b_count = int(board[x][-1])
        if 0 <= b_count != board[x][1:-1].count('B'):
            return False

    for y in range(1, cols - 1):
        b_count = int(board[-1][y])
        if 0 <= b_count != [board[x][y] for x in range(1, rows - 1)].count('B'):
            return False
    return True


def solve_sudoku_with_steps(board, output_file):
    empty_location = [0, 0]

    if not find_empty_location(board, empty_location):
        #  Whether the table is filled or not is checked by the function.
        if check_constraints(board):
            #  If the game is over, constraint values are removed from the table, and the rest are written to the output
            board.pop()
            board.pop(0)
            for j in range(len(board)):
                board[j].pop()
                board[j].pop(0)
            print_board(board, output_file)
            return True
        return False

    row, col = empty_location
    empty_cell = board[row][col]
    letters = ['HB', 'BH', 'NN']

    #   The table is filled, and its compliance with the conditions is checked.
    #   If the conditions are not met, the next possibilities are attempted.
    #   If none of the three possibilities work, a step is retraced, and the process starts again from the beginning.

    for letter in letters:
        if is_valid(board, row, col, letter, empty_cell):
            if solve_sudoku_with_steps(board, output_file):
                return True
            #   If the result does not match the table, the current move is erased, and the next move is attempted
            if empty_cell == 'L':
                board[row][col] = 'L'
                board[row][col + 1] = 'R'
            elif empty_cell == 'U':
                board[row][col] = 'U'
                board[row + 1][col] = 'D'

    return False


def print_board(board, output_file):
    #   The table is printed to the output in the desired format.
    row = len(board)
    col = len(board[0])
    for i in range(row):

        row_str = ""
        for j in range(col):
            if j == col - 1:
                row_str += str(board[i][j])
            else:
                row_str += str(board[i][j]) + " "

        if i == row - 1:
            output_file.write(row_str)
        else:
            output_file.write(row_str + '\n')


def matrix(input_line):
    #   This function takes the input file and creates list.
    return [number for number in input_line.split()]


def main():
    input_file = open(sys.argv[1], 'r')
    output_file = open(sys.argv[2], 'w')
    board = [matrix(line) for line in input_file.readlines()]
    board_maker(board, output_file)


if __name__ == '__main__':
    main()
