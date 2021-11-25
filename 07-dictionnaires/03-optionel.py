# Pour typer un dicitonnaire mais sans rendre obligatoire toutes les clés, vous
# pouvez ajouter un paramètre total=False à la déclaration du type :

# class Album(TypedDict, total=False)

# Créez un type "Meal" possédant les clés firstcourse, maincourse
# et desert (entrée, plat principal et dessert). Chacune de ses clés sera
# optionnelle.

# Créez un dictionnaire utilisant ce type.

################################################################################
from typing import TypedDict


class Book(TypedDict, total = False):
    auteur : str
    title : str
    year: int
    read : bool

obo : Book = {

    "auteur" : "alexis",
    "title" : "legende hobo",
    "year" : 2014,
    "read" : True

}
################################################################################

# Pas de validation automatique pour cet exercice. À nouveau, vérifiez que votre
# éditeur vous informe de vos erreurs. Cette fois, il ne devrait pas relever
# l'absence d'une clé (mais toujours la présence d'une clé innatendue).

# Il n'est malheureusement pas possible de rendre certaines clés optionnelles 
# tout en gardant d'autres clés obligatoires.
