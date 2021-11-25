# Il est pratiquement toujours nécessaire de vérifier que l'utilisateur a bien 
# entré une donnée dans le format attendu.

# En utilisant la boucle "while True" vue précédemment, demandez son âge à
# l'utilisateur. Si la donnée rentrée n'est pas valide (entier positif
# inférieur à 130), demandez à nouveau, jusqu'à ce qu'elle le soit.

# Pas de correction automatique pour cet exercice.

################################################################################
while True :
    age : str = input("Age: ")
    if age.isnumeric() and int(age) > 0 and int(age) < 130:
        break
    else :
        print("rentre une date vaide" )
################################################################################