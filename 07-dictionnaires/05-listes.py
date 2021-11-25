# Une liste peut contenir des dictionnaires, et un dictionnaire peut contenir
# des listes !

# Creéz une tableau "students" qui contiendra 3 dictionnaire de type "Student" 
# que vous aurez créé. Typez bien le tableau pour qu'il ne puisse contenir que
# des dictionnaires de type "Student".

from typing import TypedDict

class Student(TypedDict):
    firstname: str
    lastname: str
    notes: list[int]

################################################################################
students : list[Student] = [
    {   "firstname" : "loick","lastname" : "Roberjot","notes" : [10,30,20]},
    {   "firstname" : "loick","lastname" : "Roberjot","notes" : [10,30,20]},
    {   "firstname" : "loick","lastname" : "Roberjot","notes" : [10,30,20]}
]



################################################################################






































print('\033[92m✓ OK' if len(students) == 3 else '\033[91m❌KO')
