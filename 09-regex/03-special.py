# Il est possible de chercher un certain type de caractère grâce aux "special
# sequences". En voici quelques une utiles (liste non exhaustive) :

# \d : un chiffre
# \D : un caractère n'étant pas un chiffre
# \s : une espace
# \S : un caractère n'étant pas une espace
# \w : un caractère alphanumérique (0-9, a-z, A-z ou _)
# \W : un caractère n'étant pas alphanumérique

# Voici un exemple :

import re

match = re.search(r'\W', 'hello!')
if (match):
    print("La chaîne contient un caractère spécial")

# Modifiez la fonction pour qu'elle renvoit True si la chaîne passée est un
# numéro de version valide.
# Un numéro de version valide est composé de 2 ou 3 chiffres, séparés par des
# points.
# Exemples : 0.2, 4.5.6, 7.1...

################################################################################
def is_valid_version(version: str) -> bool:
    return True
################################################################################

# Attention ! Dans une regex, un point "." représente n'importe quel caractère.
# Pour demander précisément le caractère point, il faut l'échapper avec un
# slash d'abord : \.
















print('\033[92m✓ OK' if is_valid_version("0.2") and is_valid_version("0.2.2") and not is_valid_version("a0.2") and not is_valid_version("0.2a") and not is_valid_version("0!2") and not is_valid_version("0.2.2.2") else '\033[91m❌KO')
