# Une fonction peut retourner le résultat d'une comparaison.

# La fonction is_centenary renvoit true si l'âge passé en paramètre est
# supérieur ou égal à 100.

# Créez une fonction can_drink qui prend en premier paramètre "USA" ou "France",
# et en second paramètre l'âge de la personne. Cette fonction doit retourner
# un booléen.

################################################################################
def is_centenary(age: int) -> bool:
    return age >= 100
################################################################################

def can_drink(country : str, age : int):
    return (country == "France" and age >= 18 or country =="USA" and age >= 21)























print('\033[92m✓ OK' if not can_drink("USA", 20) and can_drink("USA", 21) and not can_drink("France", 17) and can_drink("France", 18) else '\033[91m❌KO')
