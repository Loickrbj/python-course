# Si plusieurs valeurs doivent produire les mêmes effets, il est possible
# d'utiliser un pipe "|" pour matcher une valeur ou une autre.

# case 401 | 403 | 404:
#    return "Not allowed"

# Reprenez la fonction de l'exercice précédent et optimisez là en utilisant
# seulement trois instructions "case".

################################################################################
def get_food_type(food: str):

################################################################################




































print('\033[92m✓ OK' if get_food_type("fries") == "vegan" and get_food_type("tomato") == "vegan" and get_food_type("cheese") == "veggie" and get_food_type("beef") == "animal" and get_food_type("chicken") == "animal" else '\033[91m❌KO')
