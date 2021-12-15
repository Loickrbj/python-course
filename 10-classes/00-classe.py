# Les classes sont des moyens de "réunir des données et des fonctionnalités"
# qui forment un ensemble cohérent.

# Dans un programme, elles symbolise souvent un objet logique (un utilisateur,
# un article...)

# Découper son code en classe est un moyen répandu pour gérer la complexité
# d'un programme.

# Voici un exemple :

class MyClass:
    def __init__(self):
        print("Hello world")

my_instance = MyClass()
other_instance = MyClass()

# Le nom des classes s'écrit en CamelCase.
# my_instance et other_instance sont deux instances de le classes : deux objets
# séparés ayant le comportement dicté par MyClass, qui est une sorte de "modèle"
# pour créer des objets.

# La méthode __init__(self) est le constructeur : elle est toujours appelée lors
# de l'instanciation de la classe (donc ici, une fois pour chacune des deux
# instances)

# Créez une classe User avec son constructeur, puis créez une variable "alice"
# qui sera une instance de User.

################################################################################

################################################################################



















print('\033[92m✓ OK' if isinstance(alice, User) else '\033[91m❌KO')
