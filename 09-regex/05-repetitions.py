# Le point d'interrogation demande que le caractère soit présent zéro ou une
# fois. Mais on peut aussi utiliser :

# a* : recherche de la lettre a, optionnelle mais pouvant être présente
# plusieurs fois (donc entre 0 et n)

# a+ : recherche de la lettre a, obligatoire mais pouvant être présente
# plusieurs fois (donc entre 1 et n)

# Voici un exemple dans lequel on cherche une chaîne "hello" présente au moins
# une fois, potentiellement plusieurs fois

import re

match = re.search(r'(hello)+', 'hellohello')
if (match):
    print("La chaîne contient hello au moins une fois")

# On cherche à valider des numéros de commandes. Un numéro valide est composé :
# du caractère hashtag "#"
# de zéro ou plusieurs fois la lettre A
# d'un ou plusieurs chiffres

# Quelques numéros valides : #A89, #12345 #AAA2...

################################################################################
def is_valid_command(number: str) -> bool:
    return True
################################################################################





















print('\033[92m✓ OK' if is_valid_command("#A89") and is_valid_command("#12345") and is_valid_command("#AAA8") and not is_valid_command("X#A89") and not is_valid_command("#AAA") and not is_valid_command("#A89!") else '\033[91m❌KO')
