# Tic Tac Toe game
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([spot == player for spot in row]):
            return True
    
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

def is_board_full(board):
    for row in board:
        if any([spot == " " for spot in row]):
            return False
    return True

def tic_tac_toe():
    # Initialize a 3x3 empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0
    
    # Game loop
    while True:
        print_board(board)
        print(f"Player {players[current_player]}'s turn")
        
        # Get player input
        row, col = map(int, input("Enter row and column (0, 1, 2): ").split())
        
        # Check if the move is valid
        if board[row][col] != " ":
            print("Invalid move, try again.")
            continue
        
        # Place player's mark on the board
        board[row][col] = players[current_player]
        
        # Check if the current player has won
        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break
        
        # Check for a draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = 1 - current_player

# Start the game
tic_tac_toe()