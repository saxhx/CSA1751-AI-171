% Facts about students
student('Alice', 1).
student('Bob', 2).
student('Charlie', 3).

% Facts about teachers
teacher('Mr. Smith', 1).
teacher('Ms. Johnson', 2).
teacher('Dr. Brown', 3).

% Facts about subjects
subject('Math', 1).
subject('Science', 2).
subject('History', 3).

% Facts about which student is taught by which teacher
teaches('Mr. Smith', 'Alice').
teaches('Ms. Johnson', 'Bob').
teaches('Dr. Brown', 'Charlie').

% Facts about which subject is taught by which teacher
subject_teaches('Math', 'Mr. Smith').
subject_teaches('Science', 'Ms. Johnson').
subject_teaches('History', 'Dr. Brown').

% Query to find the teacher of a student
find_teacher(Student, Teacher) :-
    teaches(Teacher, Student).

% Query to find the subject taught by a teacher
find_subject(Teacher, Subject) :-
    subject_teaches(Subject, Teacher).

% Query to find the subject taken by a student
find_subject_for_student(Student, Subject) :-
    teaches(Teacher, Student),
    find_subject(Teacher, Subject).
