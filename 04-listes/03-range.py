# Il est possible d'extraire un sous tableau à partir d'un tableau en spécifiant
# un début, une fin, voire les deux.

# list[0:4] donnera tous les éléments d'index 0 à 4 (4 non inclus)
# Le 0 est optionnel : list[:4]

# À partir du tableau days, créez un tableau "work_days" qui ne contient pas 
# samedi et dimanche.

################################################################################
days: list[str] = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
################################################################################

# Conseil : utilisez un index négatif en borne finale, plutôt que de compter
# jusqu'où s'arrêter.
work_days : list[str] = days[1:-1]










































print('\033[92m✓ OK' if work_days == ["Mon", "Tue", "Wed", "Thu", "Fri"] else '\033[91m❌KO')
