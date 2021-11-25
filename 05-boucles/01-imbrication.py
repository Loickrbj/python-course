# Une boucle dans une boucle, ça vous dit ? C'est tout à fait possible :

# for i in [1, 2, 3]
#     for j in ["a", "b", "c"]

# Sera équivalent à :

# i -> 1
#     j -> "a"
#     j -> "b"
#     j -> "c"
# i -> 2
#     j -> "a"
#     j -> "b"
#     j -> "c"
# i -> 3
#     j -> "a"
#     j -> "b"
#     j -> "c"

# La variable ci-dessous est un tableau de tableaux, qui représentent les notes
# obtenues par trois étudiants distincts.

# Utilisez deux boucles imbriquées pour calculer les moyennes de chaque
# étudiant. Stockez ces moyennes dans un tableau averages contenant 3 nombres.

################################################################################
notes = [
    [10, 8, 4, 5, 9],
    [15, 18, 4, 14],
    [9, 9, 12, 15]
]

averages : list[float] = []
somme : float = 0
################################################################################
for i in range(len(notes)):
    for j in range(len(notes[i])):
        somme = somme + notes[i][j]
    
    averages.append(somme/len(notes[i]))
    somme = 0































print('\033[92m✓ OK' if averages == [7.2, 12.75, 11.25] else '\033[91m❌KO')
