# Le signe | (pipe) permet de demander la présence d'une valeur ou d'une autre,
# tant que l'une d'entres elle est présente. Il est même possible de demander
# une valeur parmi un plus grand nombre.

# Voici un exemple :

import re

match = re.search(r'hello|goodbye', 'hello world!')
if (match):
    print("La chaîne contient hello ou goodbye")

# Complétez la fonction pour qu'elle renvoit True si la chaîne passée commence
# par une voyelle.

################################################################################
def starts_with_vowel(sample: str) -> bool:
    return True
################################################################################






























print('\033[92m✓ OK' if starts_with_vowel("abc") and not starts_with_vowel("bca") else '\033[91m❌KO')
