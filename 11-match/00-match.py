# Le filtrage par motif est une nouveauté bien pratique de python 3.10
# (assurez-vous qu'il s'agit de la version utilisée par votre éditeur).

# Voici un exemple tiré de la spécification :

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"

# Utilisez la même syntaxe pour compléter la fonction get_food_type

# Cette fonction doit retourner la chaîne :
# - "vegan" si la nourriture est "fries" ou "tomato"
# - "veggie" si la nourriture est "cheese"
# - "animal" si la nourriture est "beef" ou "chicken"

################################################################################
def get_food_type(food: str):

################################################################################
























print('\033[92m✓ OK' if get_food_type("fries") == "vegan" and get_food_type("tomato") == "vegan" and get_food_type("cheese") == "veggie" and get_food_type("beef") == "animal" and get_food_type("chicken") == "animal" else '\033[91m❌KO')
