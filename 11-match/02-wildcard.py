# Il est d'usage d'ajouter un cas final correspondant à "aucun des autres cas",
# c'est à dire quelque chose qui se produira si aucune des valeurs précédentes
# ne correspondait.

# En python, cela s'effectue avec l'opérateur "case _:"

# D'autres aliments de type "animal" s'ajoutent à notre offre. Plutôt que de
# les lister une par une, conservez les matchs sur "veggie" et "vegan", et
# ajouter un cas final pour que tous les autres types renvoient "animal".

################################################################################
def get_food_type(food: str):

################################################################################



































print('\033[92m✓ OK' if get_food_type("fries") == "vegan" and get_food_type("tomato") == "vegan" and get_food_type("cheese") == "veggie" and get_food_type("beef") == "animal" and get_food_type("chicken") == "animal" and get_food_type("pork") == "animal" and get_food_type("salmon") == "animal" else '\033[91m❌KO')
