# L'héritage permet de surcharger des méthodes, ce qui est très pratique pour
# modifier le comportement de la classe mère.

# Voici un exemple :

class MyClass:
    def say_hello(self):
        print("hello !")

class MyFrenchClass(MyClass):
    def say_hello(self):
        print("bonjour")

my_instance = MyFrenchClass()
my_instance.say_hello()

# Le comportement de la méthode say_hello est redéfini par MyFrenchClass.
# Sans cette redéfinition, la méthode appelée serait celle de la classe mère.

# En partant de vos classes User et Student,
# redéfinissez dans Student la méthode add_followers pour intégrer la règle
# suivante: on ne peut ajouter des followers que si has_degree() est vrai (oui,
# c'est un réseau un peu élitiste... c'est pour l'exemple !)
# Gardez aussi la condition sur is_adult.

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
        User.__init__(self, firstname, lastname, age) 
        self._school = school
        self._level = level

    def has_degree(self):
        if self._level >= 3:
            return True
        else : 
            return False

    def add_followers(self,count : int) :
        if self._is_adult() and self.has_degree():
            print("lol")
            self._followers += count
        return self._followers

bob = User("Bob","Doe",18)
################################################################################























user = User("bob", "doe", 18)
user.add_followers(3)
student_with_degree = Student("bob", "doe", 18, "cnam", 3)
student_with_degree.add_followers(1);
student_with_degree.add_followers(2);
student__without_degree = Student("bob", "doe", 10, "cmam", 2)
student__without_degree.add_followers(1);
student__without_degree.add_followers(2);
print('\033[92m✓ OK' if user._followers == 3 and student_with_degree._followers == 3 and student__without_degree._followers == 0 else '\033[91m❌KO')
