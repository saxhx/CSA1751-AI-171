% Knowledge base: Disease and its associated symptoms.

disease(flu) :-
    has_symptom(fever),
    has_symptom(cough),
    has_symptom(sore_throat),
    has_symptom(runny_nose).

disease(cold) :-
    has_symptom(runny_nose),
    has_symptom(sneezing),
    has_symptom(cough).

disease(covid19) :-
    has_symptom(fever),
    has_symptom(cough),
    has_symptom(tiredness),
    has_symptom(loss_of_taste_or_smell).

disease(malaria) :-
    has_symptom(fever),
    has_symptom(chills),
    has_symptom(headache),
    has_symptom(sweating).

disease(diabetes) :-
    has_symptom(frequent_urination),
    has_symptom(increased_thirst),
    has_symptom(fatigue),
    has_symptom(unexplained_weight_loss).

% Ask the user if they have a specific symptom.
ask_symptom(Symptom) :-
    write('Do you have the following symptom: '), write(Symptom), write('? (yes/no)'), nl,
    read(Reply),
    (Reply == yes -> assert(has_symptom(Symptom)) ; fail).

% Diagnose the disease by checking the symptoms.
diagnose :-
    disease(Disease),
    write('Based on your symptoms, you might have: '), write(Disease), nl,
    retractall(has_symptom(_)). % Clear the symptoms after diagnosis

% Start the diagnosis process.
start_diagnosis :-
    retractall(has_symptom(_)), % Clear any previous symptoms
    write('Welcome to the medical diagnosis system.'), nl,
    write('Please answer yes or no for the following symptoms.'), nl,
    (   (ask_symptom(fever); true),
        (ask_symptom(cough); true),
        (ask_symptom(sore_throat); true),
        (ask_symptom(runny_nose); true),
        (ask_symptom(sneezing); true),
        (ask_symptom(tiredness); true),
        (ask_symptom(loss_of_taste_or_smell); true),
        (ask_symptom(chills); true),
        (ask_symptom(headache); true),
        (ask_symptom(sweating); true),
        (ask_symptom(frequent_urination); true),
        (ask_symptom(increased_thirst); true),
        (ask_symptom(fatigue); true),
        (ask_symptom(unexplained_weight_loss); true),
        diagnose;
        write('Sorry, no diagnosis could be made based on the symptoms provided.'), nl
    ).
