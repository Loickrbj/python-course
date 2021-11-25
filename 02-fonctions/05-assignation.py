# Le retour d'une fonction peut être stocké dans une variable comme le montre 
# l'exemple ci-dessous

# Créez une fonction get_square qui retourne le carré du nombre envoyé.

# Stockez le carré de 8 dans une variable "square"

# Puis appelez à nouveau la fonction get_square, mais cette fois en lui passant
# la variable "square", de sorte à obtenir le carré du carré, et stockez le dans
# une variable "double_square".

################################################################################
def multiple(a: float, b: float) -> float:
    return a * b

result: float = multiple(6, 8)
################################################################################
def get_square(x : float):
    return pow(x,2)

square : float = get_square(8)
double_square : float  = get_square(square)
print("square :", square)
print("cube :", double_square)

































print('\033[92m✓ OK' if get_square(9) == 81 and square == 64 and double_square == 4096 else '\033[91m❌KO')
