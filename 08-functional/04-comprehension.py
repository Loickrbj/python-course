# L'utilisation de l'interprétation des listes (comprehension list en anglais)
# est un autre moyen de simplifier l'écriture d'un map
# (le mot-clé map lui-même disparaît).

# Exemple :

numbers: list[int] = [5, 13, 4, 1, 12]
squared_numbers: list[int] = [number * number for number in numbers]

# Utilisez cette syntaxe pour créer une variable "powers_of_two" qui
# contiendra la liste des nombres "numbers" utilisés en tant que puissance de 2
# (2^5 = 32, etc)

################################################################################
powers_of_two : list[int] = [2**number for number in numbers]
################################################################################

# Il s'agit probablement de la syntaxe la plus simple à comprendre !



































print('\033[92m✓ OK' if powers_of_two == [32, 8192, 16, 2, 4096] else '\033[91m❌KO')
