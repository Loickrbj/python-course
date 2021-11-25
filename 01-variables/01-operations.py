# Il est possible de déclarer des variables en utilisant la valeur d'autres
# variables !

# Ci dessous, la deuxième variable utilise la première en la multipliant par 60.
# Vous pouvez bien sûr additionner, diviser, soustraire...

# Déclarez les variables suivantes et donnez leur des valeurs appropriées:
# milliseconds_per_hour
# milliseconds_per_day

# PS : vous pouvez utiliser la commande print(milliseconds_per_seconds) pour
# afficher une variable et comprendre ce qui se passe (ou plus souvent, ce qui
# ne se passe pas)

################################################################################
milliseconds_per_seconds: int = 1000
milliseconds_per_minutes: int = milliseconds_per_seconds * 60
milliseconds_per_hour : int =  milliseconds_per_minutes * 60
milliseconds_per_day : int = milliseconds_per_hour * 24
################################################################################




























print('\033[92m✓ OK' if milliseconds_per_hour == 1000 * 60 * 60 and milliseconds_per_day == 1000 * 60 * 60 * 24 else '\033[91m❌KO')