import heapq

# Utility function to print the 8-puzzle board
def print_board(board):
    for row in board:
        print(' '.join([str(x) if x != 0 else ' ' for x in row]))
    print()

# Find the position of the blank space (0) on the board
def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return (i, j)

# Generate the list of possible moves from the current state
def get_neighbors(board):
    neighbors = []
    blank_x, blank_y = find_blank(board)
    
    # Define possible moves: (delta_x, delta_y)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for move_x, move_y in moves:
        new_x = blank_x + move_x
        new_y = blank_y + move_y
        
        # Ensure the move is within bounds
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            # Create a new board by swapping the blank space with the target tile
            new_board = [row[:] for row in board]
            new_board[blank_x][blank_y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[blank_x][blank_y]
            neighbors.append(new_board)
    
    return neighbors

# Calculate the Manhattan distance heuristic
def manhattan_distance(board, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                goal_x, goal_y = divmod(goal.index(board[i][j]), 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

# A* search algorithm to solve the 8-puzzle problem
def astar_solver(start, goal):
    # Priority queue (min-heap) for the open list
    open_list = []
    heapq.heappush(open_list, (0, start, []))  # (f_cost, current_board, path)
    
    # Set to store visited states
    visited = set()
    
    # Keep track of the number of steps
    steps = 0
    
    while open_list:
        steps += 1
        _, current_board, path = heapq.heappop(open_list)
        
        # Check if the current state is the goal
        if current_board == goal:
            print(f"Solved in {steps} steps!")
            return path + [current_board]
        
        # Add current board to visited
        visited.add(tuple(map(tuple, current_board)))
        
        # Generate neighbors
        for neighbor in get_neighbors(current_board):
            if tuple(map(tuple, neighbor)) not in visited:
                new_path = path + [current_board]
                g_cost = len(new_path)
                h_cost = manhattan_distance(neighbor, goal)
                f_cost = g_cost + h_cost
                heapq.heappush(open_list, (f_cost, neighbor, new_path))
    
    return None  # No solution found

# Main function to run the 8-puzzle solver
if __name__ == "__main__":
    # Initial state of the 8-puzzle (0 represents the blank space)
    start = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]
    
    # Goal state of the 8-puzzle
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    print("Initial State:")
    print_board(start)
    
    print("Goal State:")
    print_board(goal)
    
    solution = astar_solver(start, goal)
    
    if solution:
        print("Solution Found!")
        for step in solution:
            print_board(step)
    else:
        print("No solution exists.")