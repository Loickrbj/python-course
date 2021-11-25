# Quand on souhaite faire une boucle basée non pas sur un nombre de répétitions
# précis, mais sur une condition, la boucle while devient utile.

# Voici une boucle while qui ne s'exécutera qu'une fois (puisque la condition)
# devient fausse dès la première exécution de la boucle :

# active = True
# while active:
#     active = False

# Utilisez une boucle while pour stocker dans un tableau toutes les puissances
# de 2 inférieures à 10000 : [2, 4, 8, 16]...

# Stocker le resultat dans un tableau "powers".

################################################################################
powers : list[int] = []
i : int  = 1
while (2**i <10000):
    powers.append(2**i)
    i = i+1



################################################################################

# Astuce : la fonction pow() vous permet de calculer des puissances
# (voir la documentation).
# Vous pouvez aussi utiliser la dernière valeur du tableau et la multiplier par
# deux.






















print('\033[92m✓ OK' if powers == [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192] else '\033[91m❌KO')
