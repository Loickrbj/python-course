# Il est possible de tester si une clé est présente dans un dictionnaire grâce 
# à l'opérateur "in".
# Exemple :
# if "email" in contact
# sera valide si le dictionnaire contact contient une clé "email"

# L'opérateur "not in" permet de tester l'absence d'une clé.

# Le but de cet exercice est de compter les membres premium de la liste.
# Pour qu'un membre soit considéré comme premium, il faut qu'il ait une clé
# "premium_since" mais qu'il n'ait pas été banni ("banned_on").

# Stockez le résultat dans une variable "premium_members_count"

from typing import TypedDict

class User(TypedDict, total=False):
    member_since: str
    premium_since: str
    banned_on: str

users: list[User] = [
    {
        "member_since": "2009-10-05"
    },
    {
        "member_since": "2007-10-05",
        "premium_since": "2020-02-04",
        "banned_on": '2021-11-11'
    },
    {
        "member_since": "2009-10-05",
        "premium_since": "2019-02-04",
    }
]

################################################################################
premium_members_count: int = 0
for user in users :
    if "premium_since" in user and "banned_on" not in user:
        premium_members_count += 1



################################################################################







































print('\033[92m✓ OK' if premium_members_count == 1 else '\033[91m❌KO')
