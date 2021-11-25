# On souhaite parfois faire une boucle while, mais en précisant la condition à 
# la fin et non pas au début. La boucle sera donc exécutée au moins une fois, et
# si la condition est vérifiée, on recommence.

# Ce genre de structure appelée "do while" n'existe pas en python, mais on en a
# régulièrement besoin et on peut la simuler avec un "while True" et un "break" :

#  number: int = 0
#  while True:
#     number += 1
#     if number > 5:
#         break

# En utilisant cette structure, partez du nombre 1, puis multipliez le par 2,
# puis multipliez le résultat par 3, puis par 4...

# Stockez le premier nombre dépassant 10000 dans une variable "result"

################################################################################
number : int = 1
result : int = 1
while True : 
    number = number +1
    result = result * number
    if result > 10000:
        break
################################################################################




































print('\033[92m✓ OK' if result == 40320 else '\033[91m❌KO')
