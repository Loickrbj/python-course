# Si les décorateurs sont des fonctions, ils doivent bien pouvoir recevoir
# des paramètres eux-même !

# Il faut être honnête : la syntaxe devient très complexe. On a maintenant
# trois fonction imbriquées. Ce n'est pas le genre de chose qu'on code pour
# se détendre, mais les possibilités sont alors décuplées !

# Voici un décorateur print(where: str), qui effectue un print en fonction
# d'un paramètre : avant si where vaut "before", après s'il vaut "after"

from typing import Callable

def print_around(where: str): # La fonction la plus haute prend un paramètre de décorateur
    def decorator(function: Callable): # Ensuite, on retombe sur le schéma orginal
        def wrapper(*args, **kwargs):
            if where == "before": # Utilisation du paramètre de décorateur
                print("Before")
            result = function(*args, **kwargs)
            if where == "after": # Utilisation du paramètre de décorateur
                print("After")
            return result

        return wrapper
    return decorator

@print_around("after") # Passage du paramètre au decorateur
def say_hello(name: str):
    return "Hello " + name

print(say_hello("jane")) # Exécutez et regardez l'output !

# Modifiez votre décorateur test_duration pour passer en paramètre le nombre
# d'itérations à tester.

################################################################################

################################################################################

# Pas de vérification automatique.
# Vérifiez que le timing varie en fonction du paramètre passé au décorateur
# (comme la méthode .sort() est très rapide, utilisez de grands nombres)