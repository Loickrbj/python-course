# Les guards sont des conditions que l'on peut associer à un case.

# Voici comment en utiliser dans notre exemple
# (voir les deux conditions ajoutées) :

from typing import Tuple, Any

def get_color_type(color: Tuple[int, int, int] | Tuple[int, int, int, int] | str) -> str:
    match color:
        case [r, g, b] if r == g == b:
            return "grey color"
        case [r, g, b]:
            return "rgb color"
        case [r, g, b, a]:
            return "rgba color"
        case hex if len(hex) == 7:
            return "hex color"
        case _:
            return "unknown"

# Modifiez votre fonction précédente pour vérifier certaines choses avant de
# renvoyer le tuple (year, month, day):
# - Si une date est donnée sous la forme (year, month, day), vérifiez que
# year est supérieure ou égale à 1900
# - Si une date est donnée sous la forme d'une variable unique,
# vérifiez qu'elle contient deux séparateurs "-"
# - Sinon, regardez si elle contient deux séparateurs "/",
# et acceptez ce format également
# - Si aucun de ces cas-là ne fonctionne, renvoyez None.

################################################################################
def get_formatted_date(date: Any) -> Tuple[int, int, int] | None:
################################################################################

# Cette fois-ci, on utilise le type date: Any, car notre fonction peut recevoir
# n'importe quel type de données et renvoyer quelque chose de cohérent (type
# à réserver aux cas spéciaux comme celui-ci !).

# En complexifiant un peu tout cela et en appelant d'autres méthodes dans les
# conditions, nous pourrions faire une validation de date complète !


























import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = int(date.strftime("%Y"))

print('\033[92m✓ OK' if get_formatted_date((2021, 12, 12)) == (2021, 12, 12) and get_formatted_date((12, 12)) == (year, 12, 12) and get_formatted_date("2021-12-12") == (2021, 12, 12) and get_formatted_date((1899, 12, 12)) == None and get_formatted_date("2021/12/12") == (2021, 12, 12) and get_formatted_date("20121212") == None else '\033[91m❌KO')
