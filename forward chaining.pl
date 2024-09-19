% Declare dynamic predicates
:- dynamic fact/1.
:- dynamic rule/1.

% Define initial facts
fact(umbrella_needed).

% Define rules
rule1 :-
    fact(umbrella_needed),
    assert(fact(take_umbrella)).

rule2 :-
    fact(take_umbrella),
    assert(fact(go_outside)).

% Apply all rules
apply_rules :-
    rule1,
    rule2.

% Run forward chaining
run :-
    apply_rules,
    list_facts.

% List all facts for debugging
list_facts :-
    findall(Fact, fact(Fact), Facts),
    write('Current facts: '), nl,
    write(Facts), nl.
