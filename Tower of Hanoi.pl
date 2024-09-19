% Move N disks from Source to Destination using Auxiliary
hanoi(0, _, _, _) :- !.  % Base case: No disk to move
hanoi(N, Source, Destination, Auxiliary) :-
    N > 0,
    M is N - 1,
    hanoi(M, Source, Auxiliary, Destination),  % Move N-1 disks from Source to Auxiliary
    format('Move disk ~w from ~w to ~w~n', [N, Source, Destination]),  % Move the largest disk
    hanoi(M, Auxiliary, Destination, Source).  % Move N-1 disks from Auxiliary to Destination
