# CSP: Map Coloring using Backtracking

# Function to check if the current color assignment is valid
def is_valid(assignment, neighbors, region, color):
    for neighbor in neighbors[region]:
        if assignment.get(neighbor) == color:
            return False
    return True

# Backtracking function to solve CSP
def backtrack(assignment, regions, colors, neighbors):
    # If every region is assigned a color, return the solution
    if len(assignment) == len(regions):
        return assignment
    
    # Choose the next region to color (uncolored region)
    for region in regions:
        if region not in assignment:
            break
    
    # Try assigning a color to the region
    for color in colors:
        if is_valid(assignment, neighbors, region, color):
            assignment[region] = color  # Assign the color
            
            # Recursively assign colors to the remaining regions
            result = backtrack(assignment, regions, colors, neighbors)
            
            if result:
                return result  # Return the valid assignment
            
            # If the assignment was not valid, backtrack
            del assignment[region]
    
    return None  # No valid assignment was found

# Map coloring problem setup
regions = ['A', 'B', 'C', 'D', 'E', 'F']
colors = ['Red', 'Green', 'Blue']
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D', 'F'],
    'F': ['D', 'E']
}

# Start the backtracking search
assignment = {}
solution = backtrack(assignment, regions, colors, neighbors)

# Display the solution
if solution:
    print("Solution found:")
    for region, color in solution.items():
        print(f"Region {region}: {color}")
else:
    print("No solution found.")