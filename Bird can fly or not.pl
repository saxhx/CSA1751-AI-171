% Facts: defining some birds and their ability to fly or specific characteristics
bird('Sparrow').
bird('Penguin').
bird('Ostrich').
bird('Eagle').
bird('Kiwi').

% Facts about birds that cannot fly
cannot_fly('Penguin').
cannot_fly('Ostrich').
cannot_fly('Kiwi').

% General rule: If a bird is listed as 'cannot fly', it can't fly. Otherwise, it can fly.
can_fly(Bird) :-
    bird(Bird),
    \+ cannot_fly(Bird).

% Query to check if a bird can fly or not
check_flight_status(Bird, Status) :-
    ( can_fly(Bird) -> Status = 'can fly'
    ; Status = 'cannot fly' ).
