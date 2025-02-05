# La surcharge de méthodes devient réellement intéressante lorsque l'on s'en
# sert avec le mot clé "super". Ce dernier permet d'appeler des méthodes de la
# classe parente.

# Il devient donc possible de surcharger le fonctionnement d'une méthode tout en
# appelant la méthode originale.

# Voici un exemple :

class MyClass:
    def __init__(self, letter: str):
        self.letter = letter

class MySubClass(MyClass):
    def __init__(self, letter: str, number: int):
        super().__init__(letter)
        self.number = number

# Pour initialiser la classe enfant, nous sommes passé de :
# MyClass.__init__(self, letter)
# à
# super().__init__(letter)

# L'écriture est plus simple et seuls les paramètres varieront d'une classe
# à l'autre.

# Mais il est possible d'utiliser super() dans d'autres méthodes que __init__.

# Reprenez vos classes User et Student
# Actuellement, la méthode add_followers de Student fait quasiment la même chose
# que celle de User, elle vérifie simplement en plus si l'étudiant est diplômé.

# D'une part, cela est redondant, mais si la méthode de User change, la
# cohérence ne sera plus assurée.

# En utilisant super(), modifiez la méthode add_followers pour déléguer toute
# la logique redondante à la classe parente.

# Utilisez également la syntaxe présentée plus haut pour la fonction __init__.

################################################################################
class User :
    def __init__(self,firstname : str, lastname : str, age) -> None:
        self._firstname = firstname
        self._lastname = lastname
        self._age = age
        self._followers = 0

    def get_full_name(self):
        return (self._firstname + " " + self._lastname)
    
    def _is_adult(self):
        if self._age >= 18 : 
            return True
        else:
            return False
    
    def add_followers(self,count : int) :
        if self._is_adult():
            self._followers += count
        return self._followers
    
    def get_age(self):
        return self._age
        
def get_oldest(user1 : User, user2: User):
    
    if user1.get_age() > user2.get_age():
        return user1.get_full_name()
    else :
        return user2.get_full_name()


class Student(User):

    def __init__(self, firstname : str, lastname : str, age ,school : str, level : int):
        super().__init__(firstname, lastname, age) 
        self._school = school
        self._level = level

    def has_degree(self):
        if self._level >= 3:
            return True
        else : 
            return False


    def add_followers(self,count : int) :
        if (self.has_degree()):
            super().add_followers(count)

bob = User("Bob","Doe",18)
################################################################################























user = User("bob", "doe", 18)
user.add_followers(3)
student_with_degree = Student("bob", "doe", 18, "cnam", 3)
student_with_degree.add_followers(1);
student_with_degree.add_followers(2);
student__without_degree = Student("bob", "doe", 18, "cmam", 2)
student__without_degree.add_followers(1);
student__without_degree.add_followers(2);
print('\033[92m✓ OK' if user._followers == 3 and student_with_degree._followers == 3 and student__without_degree._followers == 0 else '\033[91m❌KO')
