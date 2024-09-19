% Facts: fruit and its color.
fruit(apple, red).
fruit(banana, yellow).
fruit(grape, purple).
fruit(orange, orange).
fruit(lemon, yellow).
fruit(strawberry, red).
fruit(blueberry, blue).

% Rule to find the color of a fruit.
fruit_color(Fruit, Color) :-
    fruit(Fruit, Color).

% Rule to explore all fruits of a particular color.
find_fruit_by_color(Color, Fruit) :-
    fruit(Fruit, Color).
