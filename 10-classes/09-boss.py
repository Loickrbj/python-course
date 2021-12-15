# Le but de cet exercice est de créer une classe Pokemon et trois classes
# Bulbasaur, Charmander & Squirtle

# 1) LA CLASSE PARENTE

# Le type Attack mentionné ci-après possède les attributs suivants :
# - name (str)
# - damage (int)

# La classe Pokémon respecte les contraintes suivantes :
# - attribut _name (str, le seul attribut passé en paramètre)
# - attribut _type (str, aucune valeur pour le moment)
# - attribut _life_points (int, aucune valeur pour le moment)
# - attribut _attack (dictionnaire de type Attack, aucune valeur pour le moment)
# - méthode get_name(self) qui renvoit le nom
# - méthode get_type(self) qui renvoit le type
# - méthode is_ok(self) qui renvoit true si les points de vie sont positifs
# - méthode take_damage(self, damage: int) qui retire des points de vie (mais
# sans aller en dessous de 0)
# - méthode fight(self, opponent: 'Pokemon') qui prend en paramètre un autre
# Pokemon # et appelle sa fonction take_damage en fonction de la puissance de
# l'attaque (le type 'Pokemon' est bien entre quotes, c'est un cas particulier
# d'auto-référence)

# 2) LES TROIS POKEMONS

# Trois classes vont hériter de Pokemon. Attention, on parle bien de classes
# et pas encore d'instances de classes ! Celles-ci seront créées plus tard.

# La classe Bulbasaur hérite de la classe Pokemon avec les valeurs suivantes :
# _name: passé à __init__ (chaque individu peut avoir un nom différent)
# _type: grass
# _life_points: 40
# _attack: {"name": "Leech Seed", "damage": 20}
# Surchargez la méthode take_damage : ce pokémon est résistant, retirez 5 à la
# valeur de chaque attaque qui lui est infligée.

# La classe Charmander hérite de la classe Pokemon avec les valeurs suivantes :
# _name: passé à __init__ (chaque individu peut avoir un nom différent)
# _type: fire
# _life_points: 50
# _attack: {"name": "Ember", "damage": 30}
# Surchargez la méthode fight : si la cible est de type "grass", on ajoute +10
# aux dégats.

# La classe Squirtle hérite de la classe Pokémon avec les valeurs suivantes :
# _name: passé à __init__ (chaque individu peut avoir un nom différent)
# _type: water
# _life_points: 40
# _attack: {"name": "Bubble", "damage": 15}
# Surchargez la méthode fight : si la cible est de type "fire", les dégats
# sont doublés.

# 3) INSTANCES

# Vous pouvez désormais créer des instances de Pokemon ainsi :
# bulby = Bulbasaur("Bulby")

# Pokemon est une "classe abstraite" : on ne doit pas l'instancier directement,
# elle sert juste de plan aux trois autres.

# 4 ) LE COMBAT

# Écrivez une méthode fight(pokemon_1: Pokemon, pokemon_2: Pokemon) qui simule
# un combat entre deux Pokemon et renvoit le Pokemon gagnant.

# Le pokemon passé en premier à la fonction est le premier à attaquer.
# Les deux pokemons s'attaquent à tour de rôle jusqu'à ce que l'un d'eux soit
# KO.

# Ajoutez des prints() pour suivre toute l'intensité de la bataille.

# Bonne chance !
from typing import TypedDict
################################################################################
class Dict_Attack(TypedDict):
  name : str
  damage : int

class Pokemon : 
  _type : str 
  _life_point : int
  _attack : Dict_Attack

  def __init__(self,name):
    self._name : str = name


  def get_name(self):
    return self._name

  def get_type(self):
    return self._type
  
  def is_ok(self):
    
    return self._life_point != 0
  
  def take_damage(self, damage : int):
      self._life_point = max(self._life_point-damage,0)

  def fight(self, oppponent : 'Pokemon'):
    oppponent.take_damage(self._attack["damage"])
  

class Bulbasaur(Pokemon):
  _life_point = 40
  def __init__(self, name : str):
    super().__init__(name)
    self._type = "grass"
    self._attack  = {'name' : "Leed Seed", "damage": 20}

  def take_damage(self, damage: int):
    return super().take_damage(damage - 5)

class Charmander(Pokemon):
  _life_point = 50
  def __init__(self, name : str):
    super().__init__(name)
    self._type = "fire"

    self._attack  = {'name' : "Ember", "damage": 30}

  def fight(self, oppponent: 'Pokemon'):
      if oppponent.get_type() == "grass":
        oppponent.take_damage(self._attack["damage"] + 10)
      else:
        oppponent.take_damage(self._attack["damage"])

class Squirtle(Pokemon):
  _life_point = 40
  def __init__(self, name : str):
    super().__init__(name)
    self._type = "water"
    self._attack  = {"name": "Bubble", "damage": 15}

  def fight(self, oppponent: 'Pokemon'):
      if oppponent.get_type() == "fire":
        oppponent.take_damage(self._attack["damage"]*2)
      else:
        oppponent.take_damage(self._attack["damage"])

  

bulby = Bulbasaur("Bulby")
sophie_chacharamander = Charmander("sophie_chacharamander")

def fight(pokemon_1 : Pokemon, pokemon_2 : Pokemon):
  while pokemon_1.is_ok() and pokemon_2.is_ok():
    pokemon_1.fight(pokemon_2)
    if(pokemon_2.is_ok()):
      pokemon_2.fight(pokemon_1)
  if not pokemon_1.is_ok():
    print(pokemon_2.get_name() + "gagne")
    return pokemon_2
  else :
    print(pokemon_1.get_name() + "gagne")
    return pokemon_1

      

################################################################################
























print('\033[92m✓ OK' if isinstance(fight(Squirtle("lol"), Charmander("iiii")), Squirtle)
  and isinstance(fight(Charmander(""), Squirtle("")), Charmander)
  and isinstance(fight(Squirtle(""), Bulbasaur("")), Bulbasaur)
  and isinstance(fight(Bulbasaur(""), Squirtle("")), Bulbasaur)
  and isinstance(fight(Charmander(""), Bulbasaur("")), Charmander)
  and isinstance(fight(Bulbasaur(""), Charmander("")), Charmander) else '\033[91m❌KO')
