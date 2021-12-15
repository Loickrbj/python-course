# Votre but est de coder un mini-jeu de recherche de trésor.

# Au départ, le personnage se trouve aux coordonnées 0, 0. Le monde dans lequel
# il se déplace n'a pas de limite (les coordonées peuvent aussi
# aller dans le négatif).

# Le but du jeu est de trouver un trésor qui se trouve aux coordonnées 5, 2

# Le programme demande des actions au joueur puis les passe à la fonction
# execute.

# Voici ce que le joueur peut faire :
# - "nord" : le joueur se déplace d'un pas vers le nord
#  (coordonnées 0, 1 si on part de 0, 0). Idem pour sud, est, ouest
# - "nord 4" le joueur se déplace de 4 pas vers le nord + autres directions

# Après chaque action du joueur, indiquez-lui ses coordonnées.

# Le jeu s'arrête quand les coordonnées du joueur correspondent à celle du
# trésor (variable playing -> false)

################################################################################
def execute(command: str) -> None:
################################################################################

playing = True

while playing:
    execute(input("Que souhaitez-vous faire ?\n"))

# Il n'y a pas de validation automatique pour cet exercice. Testez bien toutes
# les possibilités.