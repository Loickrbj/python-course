# Un match peut servir à séparer différents motifs.

# Voici un exemple :

from typing import Tuple

def get_color_type(color: Tuple[int, int, int] | Tuple[int, int, int, int] | str) -> str:
    match color:
        case [r, g, b]:
            return "rgb color"
        case [r, g, b, a]:
            return "rgba color"
        case hex:
            return "hex color"

# Notez que les termes r, g, b, a et hex pourraient être n'importe quoi
# d'autres, mais leur donner un nom cohérent facilite la lecture. Ce qui compte,
# c'est la structure de données

# On souhaite écrire une fonction get_date_type qui renverra le type de date
# fourni sous la forme d'une chaîne :
# - "YYYYMMdd" si on reçoit un tuple du type (year, month, day)
# - "MMdd" si on reçoit un tuple du type (month, day)
# - "YYYY-MM-dd" si on reçoit autre chose

# On part du principe qu'on ne recevra pas un autre type de données.

################################################################################
def get_date_type(date: Tuple[int, int, int] | Tuple[int, int] | str) -> str:
################################################################################

















print('\033[92m✓ OK' if get_date_type((2021, 12, 12)) == "YYYYMMdd" and get_date_type((12, 12)) == "MMdd" and get_date_type("2021-12-12") == "YYYY-MM-dd" else '\033[91m❌KO')
