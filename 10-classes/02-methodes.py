# Un autre composant essentiel des classes sont leurs méthodes, des fonctions
# propres à chaque instance.

# Voici par exemple une fonction qui renvoit la variable "letter" contenue par
# la classe.

class MyClass:
    def __init__(self, letter: str):
        self.letter = letter

    def get_letter(self):
        return self.letter

my_instance = MyClass("a")
print(my_instance.get_letter())

# Notez que la fonction get_letter prend automatiquement, comme __init__, un
# paramètre self qui est une référence à l'instance de classe.

# En revanche, on ne passe rien lorsqu'on appelle my_instance.get_letter()

# Modifiez votre classe User pour ajouter une fonction get_full_name() qui
# renverra une chaîne constitué du prénom et du nom, séparé par une espace.

# Supprimer l'attribut self.adult (redondant) pour le remplacer par une
# méthode is_adult() qui renvoit True ou False en fonction de l'âge

################################################################################

################################################################################

# Une méthode qui renvoit une valeur (parfois transformée) de la classe est
# appelée getter.





















test_adult = User("bob", "doe", 18)
test_child = User("bob", "doe", 10)
print('\033[92m✓ OK' if test_adult.get_full_name() == "bob doe" and test_adult.is_adult() and not test_child.is_adult() else '\033[91m❌KO')
