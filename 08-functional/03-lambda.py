# Il n'est pas toujours intéressant de déclarer la fonction de mapping
# séparemment, surtout si elle est courte et n'est pas utilisée ailleurs.

# Si la fonction ne prend qu'une seule ligne (retour immédiat), il est possible
# de la déclarer à la volée. C'est ce qu'on appelle une fonction
# anonyme (car elle n'a pas de nom). On la déclare avec le mot clé "lambda".

# Exemple :

numbers: list[int] = [5, 13, 4, 1, 12]
squared_numbers: list[int] = list(map(lambda number: number * number, numbers))

# Utilisez une fonction lambda pour créer une variable "powers_of_two" qui
# contiendra la liste des nombres "numbers" utilisés en tant que puissance de 2
# (2^5 = 32, etc)

################################################################################
lambda pow2 : 2**pow2
powers_of_two : list[int] = list(map(lambda pow2 : 2**pow2,numbers))
################################################################################

# N'oubliez pas de respecter la longueur de 79 caractères max. par ligne de
# PEP8. Parfois, cela sera trop court pour une fonction lambda !


























print('\033[92m✓ OK' if powers_of_two == [32, 8192, 16, 2, 4096] else '\033[91m❌KO')
