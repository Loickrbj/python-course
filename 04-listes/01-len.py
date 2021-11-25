# Il est possible de connaître la longueur d'une liste grâce à la fonction len().

# Exemple : len([1, 2, 3]) -> 3

# Utilisez cette fonction pour déterminer si il y a plus de membres chez les
# Beatles ou chez Muse. 

# Stockez le tableau le plus long dans une variable "biggest_band"

################################################################################
beatles: list[str] = ["Paul McCarntey", "John Lennon", "Ringo Starr", "George Harisson"]
muse: list[str] = ["Matthew James Bellamy", "Dominic James Howard", "Christopher Wolstenholme"]

biggest_band : list[str]
################################################################################

# Astuce : vous pouvez utiliser un ternaire pour assigner une valeur ou une
# autre en fonction d'une condition
# https://book.pythontips.com/en/latest/ternary_operators.html
if len(beatles) > len(muse) :
    biggest_band = beatles
else :
    biggest_band = muse






































print('\033[92m✓ OK' if biggest_band == beatles else '\033[91m❌KO')
