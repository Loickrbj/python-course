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
playing = True
player_coord : list[int] = [0,0]
tresor_coord : list[int] =  [5,2]

def execute(command: str) -> None:
    global playing 
    if len(command.split(" ")) == 1 : command = command + " 1" 
    match command.split(" "):
        case ["nord", number]:
            player_coord[1] += int(number)
        case ["sud", number]:
            player_coord[1] -= int(number)
        case ["ouest", number]:
            player_coord[0] -= int(number)
        case ["est", number]:
            player_coord[0] += int(number)
        case _ :
            print("Commande invalide reéssayez")
    print('tu est en x: ' +  str(player_coord[0]) + " y: " + str(player_coord[1]))
    if player_coord == tresor_coord:
        print("Tu as trouvé le trésor FELICITATION !!!!")
        playing = False

################################################################################






while playing:
    execute(input("Que souhaitez-vous faire ?\n"))

# Il n'y a pas de validation automatique pour cet exercice. Testez bien toutes
# les possibilités.