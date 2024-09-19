% Define initial facts.
fact(raining).
fact(sunny).

% Define rules.
rule1 :- fact(raining), assert(fact(umbrella_needed)).
rule2 :- fact(sunny), assert(fact(sunscreen_needed)).

% Define the backward chaining process.
prove(Goal) :-
    fact(Goal), !.  % Directly prove if the goal is a known fact.

prove(Goal) :-
    rule(Goal, Conditions),  % Find a rule that can satisfy the goal.
    prove_conditions(Conditions).  % Prove all conditions of the rule.

% Define rules in terms of goals and conditions.
rule(umbrella_needed, [raining]).
rule(sunscreen_needed, [sunny]).

prove_conditions([]).  % No conditions left to prove.
prove_conditions([Condition | Rest]) :-
    prove(Condition),  % Prove each condition recursively.
    prove_conditions(Rest).

% Define queries for testing.
% Example Queries:
% - Check if an umbrella is needed.
% ?- prove(umbrella_needed).
% - Check if sunscreen is needed.
% ?- prove(sunscreen_needed).
