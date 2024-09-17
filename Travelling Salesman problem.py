import itertools

def calculate_path_cost(path, distance_matrix):
    """Calculate the total cost of a given path."""
    cost = 0
    for i in range(len(path) - 1):
        cost += distance_matrix[path[i]][path[i + 1]]
    cost += distance_matrix[path[-1]][path[0]]  # Return to the starting city
    return cost

def traveling_salesman_backtracking(distance_matrix):
    """Find the shortest path using backtracking."""
    n = len(distance_matrix)
    cities = list(range(n))
    min_cost = float('inf')
    best_path = None
    
    # Generate all permutations of cities
    for perm in itertools.permutations(cities):
        current_cost = calculate_path_cost(perm, distance_matrix)
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = perm
    
    return best_path, min_cost

# Example distance matrix (symmetric, with diagonal as 0)
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Find the shortest path
best_path, min_cost = traveling_salesman_backtracking(distance_matrix)

# Display the result
print("Shortest path:", best_path)
print("Minimum cost:", min_cost)