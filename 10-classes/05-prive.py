# Une variable privée est une variable d'une classe qu'on ne peut pas lire de
# l'extérieur (c'est à dire qu'on ne peut pas faire instance.variable).
# Idem pour les méthodes : la classe peut avoir des méthodes internes qu'elle
# n'appelle qu'elle-même.

# Petite décéption, elles n'existent pas en python. Mais une convention bien
# connue les remplace : préfixer les variables et méthodes privées par un
# underscore "_".

class MyClass:
    def __init__(self, letter: str):
        self._letter = letter

    def get_letter(self):
        return self._letter

my_instance = MyClass("o")
my_instance._letter # INTERDIT ! L'underscore m'indique que la variable est privée.
my_instance.get_letter() # Ok

# Une pratique répandue est d'avoir toutes les variables en privé, et d'utiliser
# des méthodes pour écrire et lire les variables (setters et getters). Cela
# permet de contrôler strictement les règles associées à chaque variable.

# En partant de l'exercice précédent, transformez toute les variables de la
# classe User en variables privées.

# Du coup, votre méthode get_oldest() ne peut plus lire l'âge directement.
# Ajoutez un getter approprié pour vous adapter.

# On souhaite que is_adult ne puisse être appelée qu'au sein de la classe
# elle-même : utilisez la convention pour en faire une méthode privée.

################################################################################

################################################################################

# Respecter cette convention quand vous la voyez est cruciale : cela signifie
# que la logique interne de la classe à le droit de changer sans que le reste de
# votre ne programme ne soit impacté.

# On appelle parfois les éléments public d'une classe son interface.

















# Évidemment, le test accède aux variables privées alors qu'il n'a théoriquement pas le droit ;)

test_adult = User("bob", "doe", 18)
test_child = User("child", "doe", 10)
print('\033[92m✓ OK' if get_oldest(test_adult, test_child) == "bob doe" and test_adult._firstname == "bob" and test_adult._lastname == "doe" and test_adult._age == 18 and test_adult._is_adult() else '\033[91m❌KO')