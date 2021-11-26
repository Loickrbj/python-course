# Il est possible de savoir si la chaîne testée commence ou finit par une
# chaîne précise.

# Le caractère ^ symbolise le début d'une chaîne, et le caractère $ symbolise
# la fin. Il suffit de les ajouter à votre expression de recherche :

import re

match = re.search(r'^hello', 'hello world!')
if (match):
    print("La chaîne commence par hello")

# Complétez la fonction pour qu'elle renvoit True si la chaîne se termine par
# la cible donnée

################################################################################
def ends_with(target: str, sample: str) -> bool:
    return True
################################################################################

# Info : remplacez re.search() par re.match() pour demander automatiquement
# une recherche en début de string (équivaut à l'utilisation du symbole ^)




























print('\033[92m✓ OK' if ends_with("world", "hello world") and not ends_with("hello", "hello world") else '\033[91m❌KO')
