import math

# Function to implement the minimax algorithm with alpha-beta pruning
def minimax(depth, node_index, is_maximizing_player, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node_index]
    
    if is_maximizing_player:
        best_value = -math.inf
        
        for i in range(2):  # Assuming binary tree
            value = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            
            # Prune the branch
            if beta <= alpha:
                break
        
        return best_value
    else:
        best_value = math.inf
        
        for i in range(2):  # Assuming binary tree
            value = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            
            # Prune the branch
            if beta <= alpha:
                break
        
        return best_value

# Values at leaf nodes of the game tree
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Height of the game tree
max_depth = math.log2(len(values))

# Start minimax from the root (depth 0, node_index 0) for maximizer's turn
optimal_value = minimax(0, 0, True, values, -math.inf, math.inf, max_depth)

print(f"The optimal value is: {optimal_value}")