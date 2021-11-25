# Un type de variable très courant est l'entier.

# En plus de la variable déjà présente, créez trois nouvelles variables :
# seconds_per_minute
# minutes_per_hour
# hours_per_day

# Donnez leur la valeur appropriée puis lancez le programme pour valider.

################################################################################
milliseconds_per_seconds: int = 1000
seconds_per_minute : int = 60
minutes_per_hour : int = 60
hours_per_day : int = 24
################################################################################
























print('\033[92m✓ OK' if seconds_per_minute == 60 and minutes_per_hour == 60 and hours_per_day == 24 else '\033[91m❌KO')