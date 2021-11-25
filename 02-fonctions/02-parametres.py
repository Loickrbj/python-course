# L'intérêt principal d'une fonction, c'est qu'elle peut prendre des paramètres
# et retourner une valeur différente en conséquence.

# Ci-dessous, la fonction get_square_surface prend en paramètre la taille d'un
# carré et retourne sa surface

# Créez une fonction get_square_perimeter qui retournera le périmètre d'un
# carré en fonction de sa taille "size"

# Créez une fonction get_square_description qui retournera la chaîne suivante :
# "Voici un carré de 4cm de côté", où 4 est remplacé par la "size" passée en
# paramètre

################################################################################
def get_square_surface(size: float) -> float:
    return pow(size,2)

def get_square_perimeter(size : float) -> float :
    return size * 4

def get_square_description(size : float) -> str :
    return "Voici un carré de " + str(size) +"cm de côté "
###############################################################################

print (get_square_surface(4));
print (get_square_perimeter(4));
print (get_square_description(4));

# Si votre extension VSCode Python est correctement activée, vous aurez une 
# alerte si vous essayez d'appeler une fonction avec autre chose que le type
# attendu en paramètre. Essayez !




























print('\033[92m✓ OK' if get_square_perimeter(2.5) == 10 and get_square_description(12) == "Voici un carré de 12cm de côté" else '\033[91m❌KO')
