# La fonction map() permet de transformer chaque élément d'un tableau en lui
# appliquant une opération.

# Avec un peu d'habitude, elle permet de simplifier l'utilisation des boucles
# for.

# Ci-dessous se trouve un exemple de map() transformant chaque nombre d'un
# tableau en sa valeur au carré.

def square(number: int) -> int:
    return number * number

numbers: list[int] = [5, 13, 4, 1, 12]
squared_numbers: list[int] = list(map(square, numbers))

# Utilisez la même approche pour créer une variable "powers_of_two" qui
# contiendra la liste des nombres "numbers" utilisés en tant que puissance de 2
# (2^5 = 32, etc)

################################################################################
def power_of_two_funct(number : int) ->int :

    return 2**number


powers_of_two : list[int] = list(map(power_of_two_funct,numbers))
################################################################################

# Cette approche, qui se base plutôt sur des opérations que sur la programmation
# impérative classique, fait partie de l'approche appelée programmation
# fonctionnelle.

# Une différence importante avec la boucle for : aucune variable intermédiaire
# n'existe. Dans le cas d'une boucle for, nous aurions du déclarer un tableau
# vide et le remplir petit à petit. Dans des cas plus complexes, éviter les
# variables intermédiaires peut réduire le nombre d'erreurs.































print('\033[92m✓ OK' if powers_of_two == [32, 8192, 16, 2, 4096] else '\033[91m❌KO')
