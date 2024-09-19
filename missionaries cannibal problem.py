from collections import deque

# Check if a state is valid
def is_valid(state):
    M_left, C_left, M_right, C_right, boat_position = state  # Unpack all five elements
    if (M_left >= C_left or M_left == 0) and (M_right >= C_right or M_right == 0):
        return True
    return False

# Generate possible next states
def get_successors(state):
    M_left, C_left, M_right, C_right, boat_position = state
    successors = []
    
    if boat_position == 0:  # Boat on the left side
        # Try to move people to the right side
        if M_left >= 2:
            successors.append((M_left - 2, C_left, M_right + 2, C_right, 1))  # Two missionaries
        if M_left >= 1:
            successors.append((M_left - 1, C_left, M_right + 1, C_right, 1))  # One missionary
        if C_left >= 2:
            successors.append((M_left, C_left - 2, M_right, C_right + 2, 1))  # Two cannibals
        if C_left >= 1:
            successors.append((M_left, C_left - 1, M_right, C_right + 1, 1))  # One cannibal
        if M_left >= 1 and C_left >= 1:
            successors.append((M_left - 1, C_left - 1, M_right + 1, C_right + 1, 1))  # One missionary and one cannibal
    else:  # Boat on the right side
        # Try to move people to the left side
        if M_right >= 2:
            successors.append((M_left + 2, C_left, M_right - 2, C_right, 0))  # Two missionaries
        if M_right >= 1:
            successors.append((M_left + 1, C_left, M_right - 1, C_right, 0))  # One missionary
        if C_right >= 2:
            successors.append((M_left, C_left + 2, M_right, C_right - 2, 0))  # Two cannibals
        if C_right >= 1:
            successors.append((M_left, C_left + 1, M_right, C_right - 1, 0))  # One cannibal
        if M_right >= 1 and C_right >= 1:
            successors.append((M_left + 1, C_left + 1, M_right - 1, C_right - 1, 0))  # One missionary and one cannibal

    # Return only valid successors
    return [successor for successor in successors if is_valid(successor)]

# Breadth-First Search to solve the problem
def missionaries_and_cannibals_bfs():
    initial_state = (3, 3, 0, 0, 0)  # (M_left, C_left, M_right, C_right, boat_position)
    goal_state = (0, 0, 3, 3, 1)    # All on the right side
    
    # Queue for BFS
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)
    
    while queue:
        current_state, path = queue.popleft()
        
        # If the current state is the goal, return the solution path
        if current_state == goal_state:
            return path + [current_state]
        
        # Get all valid successors
        for successor in get_successors(current_state):
            if successor not in visited:
                visited.add(successor)
                queue.append((successor, path + [current_state]))
    
    return None  # No solution found

# Run the BFS algorithm
solution = missionaries_and_cannibals_bfs()

# Print the solution
if solution:
    print("Solution found!")
    for step in solution:
        M_left, C_left, M_right, C_right, boat = step
        print(f"Left side -> Missionaries: {M_left}, Cannibals: {C_left}, Right side -> Missionaries: {M_right}, Cannibals: {C_right}, Boat on {'left' if boat == 0 else 'right'}")
else:
    print("No solution exists.")