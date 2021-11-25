# Inverser l'ordre d'une boucle est un besoin récurrent.

# Pour cela, il suffit d'utiliser la fonction reversed() sur le tableau ou le 
# range utilisé.

# Utilisez une boucle for inversée pour trouver le plus grand nombre dont le
# carré est inférieur à 1000. Stockez le résultat dans une variable "result".

# N'oubliez pas d'utiliser break lorsque vous avez trouvé.

################################################################################
for i in reversed(range(50)):

    if (i**2 < 1000):
        result = i
        break
################################################################################

# Indice : de quel nombre partir ? n'importe lequel dont vous savez que son
# carré est supérieur à 1000, par exemple 50 (car 50 * 50 = 2500).

























print('\033[92m✓ OK' if result == 31 else '\033[91m❌KO')
