# Une fonction peut en appeler une autre ! Et ce à l'infini...

# Cela va nous permettre d'organiser notre code intelligemment. Chaque fonction
# fera une petite chose pouvant être appelée dès que nécessaire.

# Vous pouvez voir ci-dessous que la fonction get_square_description fait appel
# à la fonction get_square_perimeter pour récupérer le périmètre du carré.

# Créez une fonction get_square_volume prenant un paramètre "size".
# Le volume étant la surface multipliée par la hauteur, utilisez la fonction
# get_square_surface au sein de cette nouvelle fonction pour retourner le
# volume.

# Modifiez la fonction get_square_description pour qu'elle renvoit
# "Voici un carré de 16cm2 de surface et de 48cm3 de volume", en remplaçant par
# les valeurs appropriées et utilisant votre nouvelle fonction.

################################################################################
def get_square_surface(size: float) -> float:
    return size * size

def get_square_description(size: float) -> str:
    return "Voici un carré de " + str(get_square_surface(size)) + "cm2 de surface" + " et de "+ str(get_square_volume(size)) + "cm3"

def get_square_volume(size: float) -> float :
    return get_square_surface(size)
################################################################################

print(get_square_description(4))

# Bien sûr, le volume c'est plus directement la taille elevée au cube... Mais
# il me faut bien des exemples !


























print('\033[92m✓ OK' if get_square_surface(3) == 9 and get_square_volume(3) == 27 and get_square_description(3) == "Voici un carré de 9cm2 de surface et de 27cm3 de volume" else '\033[91m❌KO')
