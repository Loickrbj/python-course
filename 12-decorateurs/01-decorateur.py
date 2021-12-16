# Un décorateur est une fonction qui prend en paramètre une fonction et qui
# modifie son comportement.

from typing import Callable

def print_before_and_after(function: Callable): # on passe la fonction qu'on souhaite "décorer"
    def wrapper(): # wrapper est un nom souvent donné à la fonction interne
        print("Before")
        function() # on exécute la fonction originale
        print("After")

    return wrapper

# Voici notre fonction cobaye
def say_hello():
    print("Hello")

# On passe notre fonction au décorateur pour obtenir une nouvelle fonction
say_hello_decorated = print_before_and_after(say_hello)

say_hello_decorated() # Exécutez et regardez l'output !

# Créez une fonction de décoration test_duration(function: Callable)
# Ce décorateur exécute mille fois la fonction passée en entrée et print
# le temps d'exécution

# Voici comment mesurer une durée :

# import time
# start: float = time.time()
# # do something
# end: float = time.time()
# print("Temps écoulé :", end - start)

# Dans une fonction sort_array, utilisez [5, 2, 7].sort() pour faire une
# opération de tri quelconque 
# Passez votre fonction sort_array à votre décorateur et stockez le résultat
# dans une variable timed_sort_array
# Appelez timed_sort_array : vous devez voir le temps d'éxécution

################################################################################

################################################################################

# Pas de correction automatique pour cet exercice.
# Vérifiez que les valeurs imprimées sont cohérentes