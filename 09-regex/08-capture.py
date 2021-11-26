# Un aspect puissant de des regex est la capacité de capturer à la volée
# certaines parties d'une chaîne pour les récupérer dans des variables nommées.

# Pour cela, on utilise la syntaxe (?P<var>...)
# Où var est le nom de notre variable, et ... notre sélecteur

# On peut ensuite récupérer notre variable grâce à match.group("var")

# Voici un exemple :

import re

match = re.search(r'Hello (?P<name>[a-zA-Z]+)', 'Hello Mary')
if (match):
    print("Un prénom a été trouvé :", match.group("name"))

# À partir de la variable date, récupérez les variables year, month et day

################################################################################
year: str = ""
month : str = ""
day : str = ""
date: str = "2021-12-31"
match = re.search(r'^(?P<year>\d{1,})-(?P<month>\d{1,2})-(?P<day>\d{1,2})$',date)

if(match):
    year = match.group("year")
    print(year)
    month = match.group("month")
    print(month)
    day = match.group('day')
    print(day)
################################################################################




























print('\033[92m✓ OK' if year == "2021" and month == "12" and day == "31" else '\033[91m❌KO')
