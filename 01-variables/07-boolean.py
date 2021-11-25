# Dernier type incontournable, le booléen ne prend que deux valeurs:
# True ou False

# Il est essentiel pour gérer les conditions.

# Créez des variables "water_is_green" et "fire_is_hot" avec les valeurs
# appropriées.

################################################################################
sky_is_blue: bool = True
water_is_green : bool = False
fire_is_hot : bool = True
################################################################################

# On fera attention à nommer nos boolens comme des affirmations pour fluidifier
# la lecture de notre code. sky_is_blue est meilleur que blue_sky, plus évasif.
























print('\033[92m✓ OK' if not water_is_green and fire_is_hot else '\033[91m❌KO')
