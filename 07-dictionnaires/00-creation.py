# Un dictionnaire est un ensemble de clé / valeurs.

# Le dictionnaire user ci dessous possède une clé "firstname" ayant la valeur
# "Patrick".
# Ajoutez lui un "lastname" ayant pour valeur "Sébastien"
# Ajoutez lui un "age" ayant pour valeur 67
# Ajoutez lui un booleen "french" ayant la valeur True

################################################################################
user = {
    "firstname": "Patrick",
    "lastname" : "Sébastien",
    "age" : 67,
    "french" : True
}
################################################################################

# Dans d'autres langages, le dictionnaire est parfois appelé "objet" ou "tableau
# associatif"










































print('\033[92m✓ OK' if user['firstname'] == "Patrick" and user['lastname'] == "Sébastien" and user['age'] == 67 and user['french'] == True else '\033[91m❌KO')