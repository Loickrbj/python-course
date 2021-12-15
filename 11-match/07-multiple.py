# L'asterisque * vous permet de matcher des valeurs en nombre indéterminé.

# Voici un exemple de la documentation :

# match command.split():
#     case ["drop", *objects]:
#         for obj in objects:
#             print(obj)

# Créez une fonction compute qui permettra de faire des additions et
# multiplication de la façon suivante :

# compute("add 7") -> 7
# compute("add 7 2") -> 9
# compute("add 7 2 2") -> 11
# compute("multiply 7") -> 7
# compute("multiply 7 2") -> 14
# compute("multiply 7 2 2") -> 28
# Autre type de commande -> None

# On part du principe que les nombres passés sont toujours des entiers.

################################################################################
def compute(command: str) -> int | None:
################################################################################

# C'est peut-être l'occasion de ré-utiliser la fonction reduce pour le calcul ?






















print('\033[92m✓ OK' if compute("add 7") == 7 and compute("add 7 2") == 9 and compute("add 7 2 2") == 11 and compute("multiply 7") == 7 and compute("multiply 7 2") == 14 and compute("multiply 7 2 2") == 28 and compute("coucou") == None else '\033[91m❌KO')
