% Facts
male(john).
male(bob).
male(charles).
male(david).
male(jack).

female(mary).
female(susan).
female(alice).
female(emma).

parent(john, bob).    % john is a parent of bob
parent(john, alice).
parent(mary, bob).    % mary is a parent of bob
parent(mary, alice).
parent(bob, charles). % bob is a parent of charles
parent(susan, charles). % susan is a parent of charles
parent(bob, emma).
parent(susan, emma).
parent(alice, david).
parent(jack, david).

% Rules
father(X, Y) :- parent(X, Y), male(X).  % X is the father of Y
mother(X, Y) :- parent(X, Y), female(X).  % X is the mother of Y

child(X, Y) :- parent(Y, X).  % X is the child of Y

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).  % X is the grandparent of Y
grandfather(X, Y) :- grandparent(X, Y), male(X).  % X is the grandfather of Y
grandmother(X, Y) :- grandparent(X, Y), female(X).  % X is the grandmother of Y

sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.  % X and Y are siblings
brother(X, Y) :- sibling(X, Y), male(X).  % X is the brother of Y
sister(X, Y) :- sibling(X, Y), female(X).  % X is the sister of Y

cousin(X, Y) :- parent(A, X), parent(B, Y), sibling(A, B).  % X and Y are cousins
uncle(X, Y) :- brother(X, Z), parent(Z, Y).  % X is the uncle of Y
aunt(X, Y) :- sister(X, Z), parent(Z, Y).  % X is the aunt of Y
