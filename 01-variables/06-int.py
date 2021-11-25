# L'inverse est aussi possible : transformer une chaîne en nombre.

# Cela peut être utile car lorsqu'on demandera des données à l'utilisateur de
# notre programme, tout ce qu'il rentera sera considéré comme une chaîne.

# Or nous voudrons parfois effectuer des calculs sur ces variables, et nous
# devrons donc les transformer en int ou float

# Grâce aux fonctions int() et float(), utilisez les deux variables présentes
# pour calculer une variable salary_per_year

################################################################################
number_of_months: str = "12"
salary_per_month: str = "1554.58"
salary_per_year : float = int(number_of_months) * float(salary_per_month)
################################################################################

print("Résultat: ", salary_per_year)

# Remarque : sur number_of_months, vous pouvez utiliser int() ou float().
# En effet, python considère que int * float = float (et float * float = float)



























print('\033[92m✓ OK' if salary_per_year == 12 * 1554.58 else '\033[91m❌KO')
