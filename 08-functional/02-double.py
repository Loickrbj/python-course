# Il est possible de faire un map sur deux tableaux en même temps !

# Pour cela, il suffit de passer le deuxième tableau en paramètre supplémentaire
# de la fonction map() :
# list(map(transformation, tableau1, tableau2))

# La fonction de transformation recevra alors deux paramètres qu'elle pourra
# utiliser pour créer la valeur finale.

# Dans une variable "total_cost", calculez le prix de chaque produit commandé,
# (stockés dans la variable "products") ,sachant que les quantités respectives
# de chaque produit sont dans la variable "quantities".

# Le dernier produit a été commandé en double, le résultat devra donc être
# [150, 4, 20]

from typing import TypedDict

class Product(TypedDict):
    name: str
    cost: int

products: list[Product] = [
  {
    "name": "Aspi Turbo Max",
    "cost": 150
  },
  {
    "name": "Tournevis",
    "cost": 4
  },
  {
    "name": "Marteau",
    "cost": 10
  }
]
quantities: list[int] = [1, 1, 2]

################################################################################
def calcul(product : Product, quantity : int) -> int :
  return product["cost"] * quantity

total_cost : list[int]  = list(map(calcul,products,quantities))

print(total_cost)
################################################################################






























print('\033[92m✓ OK' if total_cost == [150, 4, 20]  else '\033[91m❌KO')
