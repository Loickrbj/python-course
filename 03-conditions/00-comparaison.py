# Un booléen permet de stocker le résultat d'une comparaison.

# L'égalité se teste avec un double égal (==), la supériorité et l'infériorité
# avec > et < (ou >= et <= pour inférieur ou égal / supérieur ou égal).

# La différence se teste avec !=

# La variable is_minor vous permet de comprendre la syntaxe à utiliser

# Créez un booléen is_adult qui sera vrai si la variable age est supérieure
# ou égale à 18

# Créez un booléen is_male qui sera vrai si la variable gender vaut "M"

# Créez un booléen is_stranger qui sera vrai si la variable nationality est
# différente de "French"

################################################################################
age: int = 18
gender: str = "F"
nationality: str = "French"

is_minor = (age < 18)

is_adult : bool = (age>=18)
is_male : bool = (gender == "M")
is_stranger : bool = (nationality != "French")

################################################################################

# Les parenthèses autour du test sont optionnelles, mais peuvent vous aider à
# mieux discerner l'objet du test




















print('\033[92m✓ OK' if is_adult and not is_male and not is_stranger else '\033[91m❌KO')
