# De même qu'on souhaite savoir si un tableau va contenir des int, des strings
# ou autre chose, typer les dictionnaire va être indispensable pour ne pas
# laisser d'ambiguité sur la forme des données.

# En utilisant l'exemple ci-dessous, créez un type "Book", qui contiendra des 
# clés pour l'auteur(e), le titre, l'année et un booléen "read" qui vaudra True
# si vous l'avez lu.

from typing import TypedDict

class Album(TypedDict):
    artist: str  
    title: str
    year: int

album: Album = {
    "artist": "Led Zeppelin",
    "title": "Physical Grafitti",
    "year": 1975
}

################################################################################
class Book(TypedDict):
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

# Pas de validation automatique pour cet exercice.
# Vérifiez bien que python vous affiche une erreur lorsque vous ne respectez
# pas le type demandé (absence d'une clé ou ajout d'une clé innatendue).
