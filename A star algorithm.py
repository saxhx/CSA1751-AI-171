from queue import PriorityQueue

# Heuristic function: Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* search algorithm
def a_star_search(start, goal, grid):
    rows, cols = len(grid), len(grid[0])
    
    # Priority queue for the open list (nodes to be explored)
    open_list = PriorityQueue()
    open_list.put((0, start))  # (f(n), node)
    
    # Dictionaries to store the g(n) cost and the parent for path reconstruction
    g_cost = {start: 0}
    came_from = {start: None}
    
    while not open_list.empty():
        _, current = open_list.get()  # Get the node with the lowest f(n)
        
        # If goal is reached, reconstruct and return the path
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Return reversed path
        
        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_cost = g_cost[current] + 1  # Distance between two adjacent cells is 1
                
                if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                    g_cost[neighbor] = tentative_g_cost
                    f_cost = tentative_g_cost + heuristic(neighbor, goal)
                    open_list.put((f_cost, neighbor))
                    came_from[neighbor] = current
    
    return None  # If no path is found

# Grid (0 represents open space, 1 represents blocked)
grid = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 0]
]

start = (0, 0)  # Start point
goal = (5, 5)   # Goal point

# Perform A* search
path = a_star_search(start, goal, grid)

# Display the path
if path:
    print("Path found:", path)
else:
    print("No path found.")