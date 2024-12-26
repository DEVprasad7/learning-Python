def main():
    n = int(input("Enter the number of queens : "))
    # Create a 2D array of n x n board
    board = [[0 for i in range(n)] for j in range(n)]
    solve_n_queen(board)

def check_row(board, row, column):
    """Check if there is a queen in the same row.
    if there is a queen in the same row return False.
    alternative condition:
    for i in range(row):
        if board[i][column] == 1:
            return False
    return True
    """
    
    for i in range(column): 
        if board[row][i] == 1:
            return False
    return True

def check_upper_diagonal(board, row, column):
    """Check if there is a queen in the upper diagonal.
       if there is a queen in the upper diagonal return False.
       zip() function is used to combine two lists.
       range(row, -1, -1) will generate a list from row to 0 in reverse order.
       same for range(column, -1, -1)"""
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def check_lower_diagonal(board, row, column):
    """Check if there is a queen in the lower diagonal.
       if there is a queen in the lower diagonal return False.
       range(row, len(board), 1) will generate a list from row to len(board) in forward order."""
    for i, j in zip(range(row, len(board), 1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def check_column(board, row, column):
    """Check if there is a queen in the same column.
       if there is a queen in the same column return False.
       alternative condition:
       for i in range(column):
           if board[row][i] == 1:
               return False"""
    for i in range(row):
        if board[i][column] == 1:
            return False
    return True

def is_safe(board, row, column):
    """Check if the queen can be placed in the given row and column.
       if the queen can be placed in the given row and column return True."""
    return check_row(board, row, column) and check_upper_diagonal(board, row, column) and check_lower_diagonal(board, row, column) and check_column(board, row, column)

def n_queen(board, column):
    """Check if all the queens are placed in the board.
       if all the queens are placed in the board return True."""
    if column >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board, i, column):
            board[i][column] = 1
            if n_queen(board, column + 1):
                return True
            board[i][column] = 0
    return False

def solve_n_queen(board):
    """Solve"""
    if n_queen(board, 0):
        for row in board:
            print(row)
    else:
        print("No solution")


"""The time complexity of the n-queen problem is O(n!) because there are n! possible ways to place n queens on the board."""
if __name__ == '__main__':
    main()