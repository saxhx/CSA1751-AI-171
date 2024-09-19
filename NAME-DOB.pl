% Facts: name and date of birth
person('Salvin Sabu', '2001-12-05').
person('John Doe', '1995-06-20').
person('Alice Smith', '1998-02-15').
person('Robert Brown', '2000-10-30').

% Query to find DOB by name
find_dob(Name, DOB) :- person(Name, DOB).
