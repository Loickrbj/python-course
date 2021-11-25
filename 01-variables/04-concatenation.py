# Il est possible de concaténer (rassembler) plusieurs chaînes à la suite en
# créant une nouvelle variable et en liant chaque partie par "+".

# chaine3: str = chaine1 + chaine2

# Créez une variable full_name qui contiendra le nom complet de cet illustre
# personnage. Attention à ne pas oublier l'espace entre le prénom et le nom !

################################################################################
first_name: str = "Patrick"
last_name: str = "Sébastien"
full_name: str = first_name + " " + last_name
################################################################################

































print('\033[92m✓ OK' if full_name == "Patrick Sébastien" else '\033[91m❌KO')
