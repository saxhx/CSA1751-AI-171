def is_safe(board, row, col, n):
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, n):
    if row >= n:
        return True
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place the queen
            
            if solve_n_queens(board, row + 1, n):  # Recur to place rest of the queens
                return True
            
            board[row][col] = 0  # Backtrack if placing queen here leads to no solution
    
    return False

def print_solution(board, n):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))

def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    if not solve_n_queens(board, 0, n):
        print(f"No solution exists for {n} queens.")
    else:
        print(f"Solution for {n} queens:")
        print_solution(board, n)

# Sample input and output
n = int(input("Enter the value of N: "))
n_queens(n)