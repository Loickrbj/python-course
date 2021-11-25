# On accède à la valeur d'un dictionnaire comme avec une liste : en utilisant
# des crochets. Mais dans le cas d'un dictionnaire, les crochets contiennent
# une clé (le nom de la propriété) à la place du chiffre représentant l'index
# dans une liste.

# Inception et Interstellar ont le même réalisateur et le même compositeur.
# Sans toucher directement à l'initialisation du dictionnaire interstellar,
# utilisez les valeurs du dictionnaire inception pour compléter le dictionnaire
# interstellar.

inception = {
    "year": 2010,
    "director": "Christopher Nolan",
    "composer": "Hans Zimmer"
}

interstellar = {
    "year": 2014
}



################################################################################
interstellar["director"] = inception["director"]
interstellar["composer"] = inception["composer"]


################################################################################


































print('\033[92m✓ OK' if interstellar['director'] == "Christopher Nolan" and interstellar['composer'] == "Hans Zimmer" else '\033[91m❌KO')
