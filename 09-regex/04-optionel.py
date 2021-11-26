# Dans l'exercice précédent, il nous fallait vérifier que le numéro de version
# était de la forme "0.0" ou "0.0.0".

# On peut considérer qu'il s'agit de la même forme, sauf que le ".0" final
# est optionnel.

# Voici comment matcher une chaîne avec une partie optionelle :

import re

match = re.search(r'hello!?', 'hello')
if (match):
    print("La chaîne contient hello ou hello! (point d'exclamation optionnel)")

# Modifiez la fonction pour qu'elle valide à nouveau un numéro de version
# (0.0 ou 0.0.0), en utilisant un groupe optionel.

# Pour ce faire, mettez la partie optionelle entre parenthèses et ajoutez le
# point d'interrogation derrière.

################################################################################
def is_valid_version(version: str) -> bool:
    return True
################################################################################


























print('\033[92m✓ OK' if is_valid_version("0.2") and is_valid_version("0.2.2") and not is_valid_version("a0.2") and not is_valid_version("0.2a") and not is_valid_version("0!2") and not is_valid_version("0.2.2.2") else '\033[91m❌KO')
