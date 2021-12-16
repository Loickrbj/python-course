# Le fait de devoir appeler notre fonction de décoration manuellement,
# la stocker dans une autre variable pour ensuite appeler cette variable est
# un peu pénible.

# Heureusement, il y a une syntaxe pour ça, que voici :

from typing import Callable

def print_before_and_after(function: Callable):
    def wrapper():
        print("Before")
        function()
        print("After")

    return wrapper

# C'est là que ça se passe. Comparez avec la version précédente !
@print_before_and_after
def say_hello():
    print("Hello")

say_hello() # Exécutez et regardez l'output !

# Faîtes la même chose sur votre décorateur test_duration.

################################################################################

################################################################################

# Pas de test automatique sur cet exercice. Vérifiez que le décorateur
# fonctionne toujours.