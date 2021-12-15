# Comme vous l'avez constaté, le mot clef "self" permet d'interagir avec les
# attributs de la classe, mais aussi avec ses méthodes.

# Modifiez votre classe User pour ajouter une fonction
# add_followers, qui prendra un entier en paramètre (en plus du "self"
# obligatoire) et ajoutera l'entier au nombre actuel de followers.

# Attention ! Cette fonction ne doit fonctionner que si l'utilisateur est un
# adulte. Il faut donc utiliser votre méthode is_adult au sein de la méthode
# add_followers. Si l'utilisateur n'est pas un adulte, la fonction n'a pas
# d'impact.

# La fonction devra renvoyer le nombre de followers final dans tous les cas.

################################################################################
class User :
    def __init__(self,firstname : str, lastname : str, age) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.followers = 0

    def get_full_name(self):
        return (self.firstname + " " + self.lastname)
    
    def is_adult(self):
        if self.age >= 18 : 
            return True
        else:
            return False
    
    def add_followers(self,count : int) :
        if self.is_adult():
            self.followers += count
        return self.followers
        

bob = User("Bob","Doe",18)
################################################################################

# C'est pour ce genre de raison qu'on préfère utiliser des getters et setters
# plutôt que de manipuler les variables de la classe directement. C'est elle
# qui dicte ses règles. De l'extérieur, on ne fait pas ce qu'on veut !
























test_adult = User("bob", "doe", 18)
test_adult.add_followers(1);
test_adult.add_followers(2);
test_child = User("bob", "doe", 10)
test_child.add_followers(1);
test_child.add_followers(2);
print('\033[92m✓ OK' if test_adult.followers == 3 and test_child.followers == 0 else '\033[91m❌KO')
