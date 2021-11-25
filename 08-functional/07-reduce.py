# La fonction reduce() est très utile lorsqu'on souhaite obtenir une valeur
# unique à partir des différentes valeurs d'un tableau.

# Voici par exemple comment calculer une somme (bien sûr, il serait plus simple
# d'utiliser la fonction sum() de python)

import functools

numbers: list[int] = [1, 2, 3, 4, 5]
sum: int = functools.reduce(lambda total, current: total + current, numbers)

# La variable "sum" vaut ici 15.
# Il est important de comprendre que "total" contient l'accumulation des opérations
# précédentes.
# À la première itération, total vaut 1 (première valeur) et current vaut 2 (seconde valeur).
# Ensuite, total vaut 3 (addition précédente) et current vaut 3 (troisième valeur).
# Ensuite, total vaut 6 (addition précédente) et current vaut 4 (quatrième valeur).
# Etc...

# Utilisez reduce() pour calculer la somme des nombres du tableau "numbers",
# mais en prenant uniquement les nombres impairs (et sans utiliser filter).

# Stockez le résultat dans une variable odd_numbers_sum.

################################################################################
odd_numbers_sum : int = functools.reduce(lambda total, current : total + current if current%2 !=0 else total, numbers)

print(odd_numbers_sum)
################################################################################

































print('\033[92m✓ OK' if odd_numbers_sum == 9 else '\033[91m❌KO')
