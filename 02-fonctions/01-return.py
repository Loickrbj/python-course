# Une fonction peut faire plein de choses en son sein, mais souvent, son 
# intérêt est qu'elle retourne une valeur dont on pourra ensuite se servir

# Par exemple, la fonction get_seconds_per_hour ci-dessous renvoit un entier,
# grâce au mot clé "return"

# On peut voir que le type de valeur renvoyée est défini juste après le nom de
# la fonction, grâce à une flèche

# On peut ensuite afficher le retour de la fonction grâce à print (ou stocker
# ce retour dans une variable pour l'utiliser plus tard)

# Définissez une fonction get_first_day_of_week qui renvoit "Sunday".

################################################################################
def get_seconds_per_hour() -> int:
    return 3600

def get_first_day_of_week( ) -> str:
    return "Sunday"

################################################################################

print(get_seconds_per_hour());
print(get_first_day_of_week());

# Pour l'instant, une fonction qui renvoit toujours le même résultat ne vaut pas
# mieux qu'une simple variable... Mais chaque chose en son temps.























print('\033[92m✓ OK' if get_first_day_of_week() == "Sunday" else '\033[91m❌KO')
