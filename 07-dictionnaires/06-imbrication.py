# Rien n'empêche d'imbriquer un dictionnaire dans un autre, c'est même bien 
# pratique.

# Le code suivant définit un objet town (zip_code -> code postal).

# On souhaite associer chaque ville à un pays.
# Creéz un type "Country" contenant une clé name, et un booléen is_eu_member
# (pour savoir s'il fait partie de l'union européenne).

# Dans le type Town, ajoutez une clé country dont le type sera "Country"

# Creéz ensuite les variables pour les villes paris, bordeaux et casablanca
# avec les valeurs adaptées. Vous devrez auparavant créer les variables pour 
# les pays concernés.

from typing import TypedDict

################################################################################
class Country(TypedDict):
    name : str
    is_eu_member : bool

class Town(TypedDict):
    name: str
    is_capital: bool
    country : Country

France : Country = {"name": "France", "is_eu_member" : True}
Maroc : Country = {"name": "Maroc", "is_eu_member" : False}
paris : Town = {"name" : "Paris","is_capital" : True, "country" : France }
bordeaux : Town = {"name" : "Bordeaux","is_capital" : False, "country" : France }
casablanca : Town = {"name" : "Casablanca","is_capital" : False, "country" : Maroc }
################################################################################

# Attention ! L'inclusion et l'héritage sont très différents.

# Une ville est incluse dans un pays, mais une ville n'est pas un type de pays
# (contrairement au train qui était un type de véhicule).
# Une ville partage une relation avec un pays, mais pas ses propriétés.





































print('\033[92m✓ OK' if paris["name"] == "Paris" and paris["is_capital"] and paris["country"]["name"] == "France" and paris["country"]["is_eu_member"] and bordeaux["name"] == "Bordeaux" and not bordeaux["is_capital"] and bordeaux["country"]["name"] == "France" and bordeaux["country"]["is_eu_member"] and casablanca["name"] == "Casablanca" and not casablanca["is_capital"] and casablanca["country"]["name"] == "Maroc" and not casablanca["country"]["is_eu_member"] else '\033[91m❌KO')
