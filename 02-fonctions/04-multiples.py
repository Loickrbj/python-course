# Une fonction peut prendre plusieurs paramètres, séparés par des virgules.
# La fonction multiple renvoit la multiplication de ses deux paramètres.

# Créez une fonction get_rectangle_perimeter prenant en paramètre une largeur
# "width" et une hauteur "height". Elle devra renvoyer le périmètre du
# rectangle.

# Créez ensuite une fonction get_square_perimeter prenant en paramètre une
# taille # "size". Un carré étant un rectangle de côté égaux, appelez à
# l'intérieur de cette fonction la précédente fonction get_rectangle_surface, en
# passant deux fois "size" pour la largeur et la hauteur.

################################################################################
def multiple(a: float, b: float) -> float:
    return a * b
################################################################################

def get_rectangle_perimeter(width : float, height : float) :
    return 2*width + 2*height

def get_square_perimeter( size : float) : 
    return 4*size


print(multiple(3, 3.5))
print(get_rectangle_perimeter(5, 7.5))
print(get_square_perimeter(7))































print('\033[92m✓ OK' if get_square_perimeter(5.5) == 22 and get_rectangle_perimeter(10, 5.5) == 31 else '\033[91m❌KO')
