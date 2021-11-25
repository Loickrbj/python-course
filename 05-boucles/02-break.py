# L'instruction break permet de stopper une boucle sans attendre qu'elle se
# termine, ce qui est parfois intéressant si on a trouvé ce que l'on cherche
# sans aller jusqu'au bout.

# for i in [1, 2, 3]:
#     if (i >= 2):
#         break

# Trouvez le premier multiple de 7 du tableau "numbers". Stoppez immédiatement
# la boucle lorsqu'il est trouvé. Stockez le résultat dans une variable
# "multiple_of_7".

################################################################################
numbers: list[int] = [4, 5, 78, 45, 84, 101, 10, 14, 87, 45, 2, 45, 66, 4, 48]
################################################################################

# Voir aussi : l'instruction continue permet de sauter directement à la
# prochaine itération de la boucle sans exécuter le reste du bloc.
# Son utilisation est plus rare.
multiple_of_7 : int
for i in range(len(numbers)):
    if (numbers[i]%7 == 0):
        multiple_of_7 = numbers[i]
        break
    else :
        continue





































print('\033[92m✓ OK' if multiple_of_7 == 84 else '\033[91m❌KO')
