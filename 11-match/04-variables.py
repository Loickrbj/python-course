# Les motifs deviennent encore plus intéressant lorsqu'on manipule les variables
# utilisées pour détecter les motifs.

# Voici notre exemple mis à jour, observez bien les print ajoutés :

from typing import Tuple

def get_color_type(color: Tuple[int, int, int] | Tuple[int, int, int, int] | str) -> str:
    match color:
        case [r, g, b]:
            print("Le niveau de rouge est", r);
            print("Le niveau de vert est", g);
            print("Le niveau de bleu est", b);
            return "rgb color"
        case [r, g, b, a]:
            print("Le niveau de transparence est", a);
            return "rgba color"
        case hex:
            return "hex color"

# On souhaite écrire une fonction get_formatted_date qui renverra une date
# sous la forme d'une tuple (year, month, day).
# Rappel: un tuple est un ensemble non modifiable de valeurs associées entre
# elles, et symbolisé par des parenthèses.

# Or on ne sait pas sous quelle forme on reçoit la date. Cela peut-être :
# - un tuple (year, month, day) (dans ce cas, pas de transformation à appliquer)
# - un tuple (month, day) (dans ce cas, l'année sera l'année courante à ajouter en dur)
# - une chaîne de caractère YYYY-MM-dd (dans ce cas, il faut utiliser un split)

# On part du principe qu'on ne recevra pas un autre type de données.
# On ne vérifie pas la cohérence de la date.

################################################################################
def get_formatted_date(date: Tuple[int, int, int] | Tuple[int, int] | str) -> Tuple[int, int, int]:
################################################################################

# Il n'est pas toujours évident de gérer les types dans ces cas-là, mais on
# peut y arriver. Ils sont même vitaux pour nous éviter des cas imprévus.



















import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = int(date.strftime("%Y"))

print('\033[92m✓ OK' if get_formatted_date((2021, 12, 12)) == (2021, 12, 12) and get_formatted_date((12, 12)) == (year, 12, 12) and get_formatted_date("2021-12-12") == (2021, 12, 12) else '\033[91m❌KO')
