# Et si nous combinions map() et filter() ?
# Grâce à l'interprétation des listes, c'est simple !

# Voici comment calculer les carrés d'une liste de nombre, en gardant uniquement
# les nombres pairs.

numbers: list[int] = [5, 13, 4, 1, 12]
squared_even_numbers: list[int] = \
  [number * number for number in numbers if number % 2 == 0]

# Résultat : [16, 144]

# Créez une variable "powers_of_two" qui contiendra la liste des nombres
# "numbers" utilisés en tant que puissance de 2, en excluant les nombres qui
# font partie du tableau "evil_numbers".

evil_numbers: list[int] = [13, 666]

################################################################################
powers_of_two : list[int] = [2**number for number in numbers if number not in evil_numbers]
################################################################################
























# Ignorez l'erreur de type sur le code de vérification
print('\033[92m✓ OK' if powers_of_two == [32, 16, 2, 4096] else '\033[91m❌KO')
