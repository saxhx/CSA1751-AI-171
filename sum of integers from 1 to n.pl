% Base case: the sum of integers from 1 to 1 is 1
sum_integers(1, 1).

% Recursive case: the sum of integers from 1 to N is N plus the sum of integers from 1 to N-1
sum_integers(N, Sum) :-
    N > 1,
    N1 is N - 1,
    sum_integers(N1, Sum1),
    Sum is N + Sum1.
