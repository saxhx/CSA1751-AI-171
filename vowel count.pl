% Define the vowels
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

% Predicate to count the number of vowels in a string (list of characters).
count_vowels([], 0).  % Base case: Empty list has 0 vowels.
count_vowels([H | T], Count) :-
    (   vowel(H)              % Check if the head is a vowel
    ->  count_vowels(T, SubCount),  % Recurse with the tail
        Count is SubCount + 1       % Increment the count
    ;   count_vowels(T, Count)       % Otherwise, just recurse with the tail
    ).

% Helper predicate to convert a string to a list of characters and count vowels.
count_vowels_in_string(String, Count) :-
    string_chars(String, Chars),  % Convert string to list of characters
    count_vowels(Chars, Count).   % Count vowels in the list

% Define some test cases
test_count_vowels :-
    count_vowels_in_string('hello world', Count1),
    write('Number of vowels in "hello world": '), write(Count1), nl,

    count_vowels_in_string('prolog programming', Count2),
    write('Number of vowels in "prolog programming": '), write(Count2), nl.

% Run the test cases
:- test_count_vowels.
