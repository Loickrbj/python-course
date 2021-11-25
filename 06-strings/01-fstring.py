# Les chaînes fstring permettent d'insérer des variables au sein de chaînes de
# façon plus simple (pas besoin d'ouvrir et fermer les guillements pour chaque
# variable).

# Exemple : f"Bonjour {name}"
# (notez le f au début de la chaîne)

# Créez une variable "message" qui stockera la chaîne suivante :
# "Nous sommes mercredi et il fait 17 degrés"
# Utilisez pour cela les variables à votre disposition.

################################################################################
day: str = "mercredi"
temperature: int = 17
################################################################################

message = f"Nous sommes mercredi et il fait {17} degrés"


























print('\033[92m✓ OK' if message == "Nous sommes mercredi et il fait 17 degrés" else '\033[91m❌KO')
