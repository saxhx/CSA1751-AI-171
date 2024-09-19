% Define the graph using edges and distances (costs).
edge(a, b, 1).
edge(a, c, 4).
edge(b, d, 2).
edge(b, e, 5).
edge(c, f, 3).
edge(d, g, 6).
edge(e, g, 2).
edge(f, g, 4).

% Heuristic values (hypothetical straight-line distances to the goal).
heuristic(a, 7).
heuristic(b, 6).
heuristic(c, 3).
heuristic(d, 4).
heuristic(e, 2).
heuristic(f, 5).
heuristic(g, 0).

% Best First Search Algorithm
best_first_search(Start, Goal, Path) :-
    heuristic(Start, H),                  % Get the heuristic value for the start node
    bfs([[Start, H]], Goal, [], Path).    % Initialize the open list with the start node

% Base case: If the goal is found, return the path.
bfs([[Goal|Path] | _], Goal, _, [Goal | Path]).

% Recursive case: Expand the current node and continue searching.
bfs([[Node | Path] | Rest], Goal, Closed, FinalPath) :-
    findall([NextNode, [Node | Path], H],
            (edge(Node, NextNode, _), \+ member(NextNode, Closed), heuristic(NextNode, H)),
            NextMoves),
    append(Rest, NextMoves, UpdatedQueue),
    sort(2, @=<, UpdatedQueue, SortedQueue),  % Sort based on heuristic (Best First)
    bfs(SortedQueue, Goal, [Node | Closed], FinalPath).

% Helper predicate to append lists.
append([], L, L).
append([H | T], L, [H | R]) :- append(T, L, R).
