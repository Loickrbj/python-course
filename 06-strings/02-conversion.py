# Les inputs utilisateurs sont toujours des chaînes, même si l'utilisateur entre
# des chiffres.

# Si on attend des chiffres, il faut vérifier que l'utilisateur a bien rentré le
# format attendu grâce aux fonctions isnumeric() pour les entiers et isdigit()
# pour les décimaux.

# Demandez son âge à l'utilisateur.
# Si l'utilisateur ne répond pas par un nombre entier, affichez une erreur (le
# programme s'arrête).
# Si l'utilisateur répond par un entier, convertissez sa réponse et utilisez-là
# pour affichier si l'utilisateur est majeur ou non.

# Pas de validation automatique pour cet exercice.

################################################################################

age : str = input("age : ")
if (age.isnumeric()):
    if int(age) >= 18 :
        print("majeur")
    else:
        print("pas majeur")
else :
    print("ERREUR")
################################################################################

# Astuce : vous pouvez utiliser un ternaire pour afficher "Mineur" ou "Majeur"
# en fonction d'une variable.
# https://book.pythontips.com/en/latest/ternary_operators.html