# Utilisez les crochets pour capturer des ensembles de caractères :

# [abc] : un caractère au choix parmi a, b, c
# [a-z] : un caractère au choix parmi toutes les lettres de a à z
# [A-Z] : un caractère au choix parmi toutes les lettres de A à Z
# [0-9] : un caractère au choix parmi tous les chiffres (équivalent à \d)
# [a-zA-z] : combinaison d'ensembles (n'importe quelle lettre)

# Exemple :

import re

match = re.search(r'[a-z]+', 'hello')
if (match):
    print("La chaîne contient au moins une lettre minuscule")

# Renvoyez True si la couleur passée en paramètre est valide.
# Un format de couleur valide est #12A4F5 (six caractères hexadécimaux, c'est
# à dire les chiffres et les lettres de A à F)
# Les minuscules doivent être valides

################################################################################
def is_valid_color(color: str) -> bool:
    return True
################################################################################


























print('\033[92m✓ OK' if is_valid_color("#000000") and is_valid_color("#123Abc") and is_valid_color("#FFFFFF") and not is_valid_color("#1234567") and not is_valid_color("#12345") and not is_valid_color("123456") and not is_valid_color("!#123456") else '\033[91m❌KO')
