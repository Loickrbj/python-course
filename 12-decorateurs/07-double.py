# Il est possible d'associer plusieurs décorateurs à une seule méthode.

# Pour cela, il suffit "d'empliler" les décorateurs au dessus de la méthode,
# un par ligne.

# Reprenez vos décorateurs test_duration et debug, ainsi que votre fonction sum.
# Appelez sum avec des valeurs de votre choix.

# Il faut ajouter un petit détail aux décorateurs pour qu'ils restent bien
# "identifiés" quand ils seront plusieurs. Avant la méthode wrapper, ajoutez
# la ligne suivante :
# @functools.wraps(function)

# Appliquez les deux décorateurs sur sum() et observez le résultat.

# Inversez l'ordre des décorateurs et comparez le résultat.

################################################################################

################################################################################

# Pas de validation pour cet exercice.
