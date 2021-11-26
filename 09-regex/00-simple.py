# Une expression régulière (regex) permet de savoir si une chaîne correspond
# à un schéma donné.

# Utilisez cet outil (en sélectionnant python comme langage) pour vous aider
# au fil de ces exercices : https://regex101.com/

# Voici ci-dessous comment détecter si la chaîne "hello" est présente dans une
# chaîne test.

import re

match = re.search(r'hello', 'hello world!')
if (match):
    print("La chaîne hello a été trouvée")

# Complétez la fonction ci-dessous en utilisant une regex.
# Elle doit renvoyer True si target est trouvée dans sample, False sinon

################################################################################
def contains(target: str, sample: str) -> bool:
    return True
################################################################################

# Il existe une syntaxe pour transformer un résultat de match en booléen ;)

























print('\033[92m✓ OK' if contains("hello", "hello world") and not contains("goodbye", "hello world") else '\033[91m❌KO')
