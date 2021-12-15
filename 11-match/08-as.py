# Le mot clé as permet de donner un nom à une variable capturée.

# Voici un exemple :

def compute(command: str) -> None:
    match command.split():
        case [a, ('+' | '-' | '*' | '/') as operation, b]:
            print("L'opération est", operation)
        case _:
            print("Opération non valide")

# Complétez la fonction get_formatted_date pour transformer une date de type
# YYYY-MM-dd en tuple (year, month, day). On part du principe que le format
# est toujours correct.
# Seules les années 2021, 2022 et 2023 sont acceptées, mais vous ne pouvez pas
# utiliser de if.
# Renvoyez None dans les autres cas.

################################################################################
from typing import Tuple

def get_formatted_date(date: str) -> Tuple[(int, int, int)] | None:
################################################################################


























print('\033[92m✓ OK' if get_formatted_date("2021-12-12") == (2021, 12, 12) and get_formatted_date("2023-12-12") == (2023, 12, 12) and get_formatted_date("2024-12-12") == None else '\033[91m❌KO')
