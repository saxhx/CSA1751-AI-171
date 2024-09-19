% Facts about planets
planet('Mercury', 'Terrestrial', 57.91e6). % distance in km
planet('Venus', 'Terrestrial', 108.2e6).
planet('Earth', 'Terrestrial', 149.6e6).
planet('Mars', 'Terrestrial', 227.9e6).
planet('Jupiter', 'Gas Giant', 778.3e6).
planet('Saturn', 'Gas Giant', 1.429e9).
planet('Uranus', 'Ice Giant', 2.871e9).
planet('Neptune', 'Ice Giant', 4.495e9).

% Query to find the type of a planet
find_type(Planet, Type) :-
    planet(Planet, Type, _).

% Query to find the distance of a planet from the Sun
find_distance(Planet, Distance) :-
    planet(Planet, _, Distance).

% Query to find planets of a specific type
find_planets_by_type(Type, Planets) :-
    findall(Planet, planet(Planet, Type, _), Planets).

% Query to find the planet closest to a given distance
find_closest_planet(Distance, Planet) :-
    planet(Planet, _, PlanetDistance),
    abs(PlanetDistance - Distance, Difference),
    \+ (planet(_, _, OtherDistance), abs(OtherDistance - Distance, OtherDifference), OtherDifference < Difference).
