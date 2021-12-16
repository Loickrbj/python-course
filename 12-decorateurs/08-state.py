# Un décorateur peut retenir un état, ce qui est très pratique pour compter
# le nombre de fois où une fonction a été appelée.

# Créez un décorateur @count, sans arguments.
# Utilisez une structure classique avec un wrapper qui appelle la fonction
# passée et retourne sa valeur.

# Après la fonction wrapper(), utilisez la ligne suivante pour initialiser
# un compteur :
# wrapper.calls_count = 0

# Oui, on attribue une variable à la fonction wrapper ! Comme dans d'autres
# langages, les fonctions python sont en fait des objets, donc rien ne
# l'interdit...

# À l'intérieur de la fonction wrapper(), incrémentez cette variable
# (on y accède de la même façon) et affichez le nombre d'appel
# à function.__name__

# Utilisez à nouveau votre méthode sum(). Appelez-là plusieurs fois et admirez.

################################################################################

################################################################################

# Pas de vérification automatique pour cet exercice.