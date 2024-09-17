from collections import deque

# Function to check if we can measure exactly Z liters
def can_measure_water(jug1, jug2, target):
    if target > jug1 + jug2:  # If target is more than total capacity of both jugs
        return False
    
    # To store visited states to avoid repetition
    visited = set()
    
    # Using deque for BFS (queue)
    queue = deque([(0, 0)])  # Start with both jugs empty
    
    while queue:
        current_state = queue.popleft()
        x, y = current_state  # x is water in jug1, y is water in jug2
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        # If the current state contains the target amount of water
        if x == target or y == target or x + y == target:
            return True
        
        # Possible states after performing operations
        possible_states = [
            (jug1, y),  # Fill jug1
            (x, jug2),  # Fill jug2
            (0, y),     # Empty jug1
            (x, 0),     # Empty jug2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),  # Pour jug1 -> jug2
            (x + min(y, jug1 - x), y - min(y, jug1 - x))   # Pour jug2 -> jug1
        ]
        
        for state in possible_states:
            if state not in visited:
                queue.append(state)
    
    return False

# Sample input and output
jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount of water: "))

if can_measure_water(jug1, jug2, target):
    print(f"It is possible to measure exactly {target} liters.")
else:
    print(f"It is NOT possible to measure exactly {target} liters.")