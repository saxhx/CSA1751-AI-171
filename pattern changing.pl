% Define a predicate to match a pattern against a term.
match_pattern(Term, Pattern, Substitutions) :-
    unify(Term, Pattern, Substitutions).

% Unify two terms and return the substitutions.
unify(Term, Pattern, Substitutions) :-
    Term = Pattern,         % Perform unification
    capture_substitutions(Term, Pattern, [], Substitutions).

% Capture substitutions during unification.
capture_substitutions(Term, Term, Substitutions, Substitutions).
capture_substitutions(Term, Pattern, Acc, Substitutions) :-
    compound(Term),         % Check if Term is a compound term
    compound(Pattern),
    Term =.. [Functor | Args],
    Pattern =.. [Functor | PatternArgs],
    capture_args(Args, PatternArgs, Acc, Substitutions).

% Capture arguments of compound terms.
capture_args([], [], Substitutions, Substitutions).
capture_args([H | T], [PH | PT], Acc, Substitutions) :-
    (   var(PH)               % If PH is a variable, add to substitutions
    ->  (   memberchk(PH = H, Acc)
        ->  true
        ;   capture_substitutions(H, PH, Acc, NewAcc),
            capture_args(T, PT, NewAcc, Substitutions)
        )
    ;   H = PH,
        capture_args(T, PT, Acc, Substitutions)
    ).

% Define some test cases
test_pattern_matching :-
    % Define terms and patterns
    Term1 = foo(bar, 42),
    Pattern1 = foo(X, 42),
    Term2 = foo(bar, 13),
    Pattern2 = foo(Y, Z),

    % Match patterns
    match_pattern(Term1, Pattern1, Substitutions1),
    write('Substitutions for Term1 and Pattern1: '), write(Substitutions1), nl,

    match_pattern(Term2, Pattern2, Substitutions2),
    write('Substitutions for Term2 and Pattern2: '), write(Substitutions2), nl.

% Run the test cases
:- test_pattern_matching.
