# Un point crucial concernant les classes est la notion d'héritage (comme
# pour les types !)

# Voici un exemple :

class MyClass:
    def __init__(self, letter: str):
        self.letter = letter

    def get_letter(self):
        return self.letter

class MySubClass(MyClass):
    def __init__(self, letter: str, number: int):
        MyClass.__init__(self, letter)
        self.number = number

    def get_number(self):
        return self.number

my_instance = MySubClass("a", 2)
print(my_instance.get_letter())
print(my_instance.get_number())

# Prenez bien le temps de comprendre ce qui se passe !
# MyClass possède un attribut letter et une méthode get_letter

# MySubClass hérite de cette classe, et donc du même attribut et de la même
# méthode. Observez bien les lignes 13 et 15 pour comprendre comment l'héritage
# se met en place.

# En plus des attributs et méthodes hérités, MySubClass possède un attribut
# number et une méthode get_number en supplément.

# Reprenez votre classe User.
# Créez une classe Student qui hérite de User et qui :
# - possède un attribut privé _school (str)
# - possède un attribut privé _level (int)
# - possède une méthode hasDegree() qui renvoit True si le level est supérieur
# ou égal à 3

################################################################################

################################################################################

# Pour vérifier que l'héritage est pertinent, demandez-vous si tous les Student
# sont des User et si chaque attribut et méthode s'appliquent aussi à un
# Student. Student est un type d'User particulier, une extension.

# Bien sûr, l'héritage multi-niveau est possible.

















test = Student("bob", "doe", 18, "cnam", 3)
test_bis = Student("bob", "doe", 18, "cnam", 2)
print('\033[92m✓ OK' if test.get_full_name() == "bob doe" and test._school == "cnam" and test._level == 3 and test.has_degree() and not test_bis.has_degree() else '\033[91m❌KO')