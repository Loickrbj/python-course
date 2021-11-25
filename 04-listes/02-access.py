# Il est possible d'accéder au n-ième élément d'un tableau grâce à la syntaxe
# list[n].

# Il est également possible de partir de la fin : list[-n] est le n-ième élément
# en partant de la fin du tableau.

# Attention, en python comme dans la plupart des langages, on commence à compter
# à partir de 0 !

# À partir du tableau days, créez une variable :
# "first_day" qui contiendra le premier jour de la semaine (ici dimanche)

# Considérez ensuite le tableau work_days qui contient la liste des jours
# travaillés (mais sous forme numérique).
# Grâce aux deux tableaux combinés, créez une variable "last_day_of_work" qui
# contient le dernier jour de travail de la semaine sous forme texuelle.

################################################################################
days: list[str] = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
work_days: list[int] = [1, 2, 3, 4, 5]
################################################################################


first_day : str = days[0]
last_day_of_work : str = days[work_days[-1]]





































print('\033[92m✓ OK' if first_day == "Sun" and last_day_of_work == "Fri" else '\033[91m❌KO')
