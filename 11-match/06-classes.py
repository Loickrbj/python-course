# Des instances de classes peuvent aussi être utilisées pour le match afin
# de poser la question : est-ce une instance de cette classe avec certaines
# valeurs précises ?

# Voici un exemple de la documentation :

class Point:
    x: int
    y: int

def location(point):
    match point:
        case Point(x = 0, y = 0):
            print("Origin is the point's location.")
        case Point(x = 0):
            print("The point is on the y-axis.")
        case Point(y = 0):
            print("The point is on the x-axis.")
        case Point():
            print("The point is located somewhere else on the plane.")
        case _:
            print("Not a point")

# Complétez la fonction get_subscription_price qui renverra :
# - 10 si l'utilisateur est un étudiant premium
# - 20 si l'utilisateur est un étudiant non premium ou un premium non-étudiant
# - 30 si l'utilisateur est un User normal
# - None si ce n'est pas un User


from typing import Any

class User:
    def __init__(self, name: str, student: bool, premium: bool):
        self.name = name
        self.student = student
        self.premium = premium

example_user = User("John", True, False)

################################################################################
def get_subscription_price(user: Any) -> int | None:
################################################################################

# N'oubliez pas que vous pouvez combiner les cas qui donnent le même résultat.

# Tout cela serait faisable avec des if/else, mais on peut comparer les deux
# pour se convaincre que cette syntaxe est bien plus claire !


















print('\033[92m✓ OK' if get_subscription_price(User("john", True, True)) == 10 and get_subscription_price(User("john", True, False)) == 20 and get_subscription_price(User("john", False, True)) == 20 and get_subscription_price(User("john", False, False)) == 30 and get_subscription_price("coucou") == None else '\033[91m❌KO')
