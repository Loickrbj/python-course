# À partir d'une classe, on peut créer autant d'instances que l'on souhaite,
# chacune est un objet séparé. Ces objets peuvent être manipulés comme des
# variables (à vrai dire, ce sont des variables !).

# Reprenez votre classe User.

# En dehors de la classe, créez une fonction get_oldest(). Cette fonction doit
# prendre deux instances de la classe User en paramètre, et renvoyer le
# fullname (prénom + nom) de l'utilisateur le plus vieux
# (on ignore le cas où les âges sont égaux).

################################################################################

################################################################################

# N'oubliez pas le typage. Une classe est également un type, ce qui est bien
# pratique.
















test_adult = User("bob", "doe", 18)
test_child = User("child", "doe", 10)
print('\033[92m✓ OK' if get_oldest(test_adult, test_child) == "bob doe" else '\033[91m❌KO')