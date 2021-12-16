# Pour comprendre ce qu'est un décorateur, il faut déjà comprendre qu'une
# fonction peut en renvoyer une autre !

# Voyez plutôt :

from typing import Callable

def get_number_generator() -> Callable[[], int]:
    print("Je suis la fonction qui retourne une autre fonction")

    def generate_number(): # Fonction définie dans le scope de get_number_generator
        print("Je suis la fonction interne et renvoyée")
        return 8

    return generate_number # On retourne la fonction (sans parenthèses, pas d'exécution ici)
  
# Le type Callable[[], int] correspond à une fonction qui ne prend pas de
# paramètre et qui retourne un entier.

# Si on essaie d'exécuter generate_number(), ça ne fonctionne pas ! Elle n'est
# pas dans le scope global.

# Voici comment récupérer la fonction:

my_number_generator: Callable[[], int] = get_number_generator()

# my_number_generator contient une référence à la fonction generate_number(),
# mais cette dernière n'a pas encore été appelée.

# On l'appelle comme une fonction (puisque c'en est une)

number: int = my_number_generator()
print(number) #8

# Écrivez une fonction get_hello_generator(french: bool)
# Si french est True, la fonction doit renvoyer une autre fonction
# qui elle-même renvoit "Bonjour"
# Sinon, la fonction renvoyée renvoit la valeur "Hello"

################################################################################

################################################################################

# La condition peut-être gérée directement dans la fonction que vous renvoyez
# (plutôt que de renvoyer deux fonctions différentes).
# En effet, la fonction interne a accès au scope de la fonction principale (et
# donc à la variable french), même après avoir été renvoyée !
# C'est ce qu'on appelle une closure.














print('\033[92m✓ OK' if get_hello_function(True)() == "Bonjour" and get_hello_function(False)() == "Hello" else '\033[91m❌KO')
