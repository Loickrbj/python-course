# Les listes (ou tableaux) contiennent une suite ordonnée de valeurs de même
# type.

# days: list[str] = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

# Créez une variable "prime_numbers" contenant la liste
# des 10 premiers nombres premiers (1 n'en faisant pas partie).

# Créez une variable "voyels" contenant la liste des voyelles
# (en majuscule, en comptant "Y").

################################################################################

prime_numbers : list[int] = [2,3,5,7,11,13,17,19,23,29]
voyels : list[str] = ["A","E","I","O","U","Y"]

################################################################################








































print('\033[92m✓ OK' if prime_numbers == [2,3,5,7,11,13,17,19,23,29] and voyels == ['A', 'E', 'I', 'O', 'U', 'Y'] else '\033[91m❌KO')
