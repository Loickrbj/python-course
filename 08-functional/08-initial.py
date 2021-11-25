# Lorsque vous utilisez reduce(), si le type de variable que vous souhaitez
# obtenir n'est pas le même que celui de la liste, il vous faut rajouter aux
# paramètres une valeur d'initialisation.

# Par exemple, pour former une string "12345" à partir d'un tableau d'entiers :

import functools

numbers: list[int] = [1, 2, 3, 4, 5]
numbers_str: str = functools.reduce(lambda a, b: str(a) + str(b), numbers, "")

# Ici, la logique change donc un peu :
# À la première itération, a vaut "" (valeur d'initialisation) et b vaut 1
# Ensuite, a vaut "1" et b vaut 2
# Ensuite, a vaut "12" et b vaut 3
# Etc...

# Reprenons notre liste de produit. Cette fois, utilisez reduce() pour obtenir
# non pas une liste de prix, mais le prix total de la commande. Stockez le
# résultat dans une variable "total_cost". Cette fois-ci, la quantité est
# stockée directement avec le produit.

from typing import TypedDict

class Product(TypedDict):
    name: str
    cost: int
    quantity: int

products: list[Product] = [
  {
    "name": "Aspi Turbo Max",
    "cost": 150,
    "quantity": 1
  },
  {
    "name": "Tournevis",
    "cost": 4,
    "quantity": 1
  },
  {
    "name": "Marteau",
    "cost": 10,
    "quantity": 2
  }
]

################################################################################
total_cost : int = functools.reduce(lambda cost, product : cost +  (product["quantity"] * product["cost"]), products, 0)
print (total_cost)
################################################################################

# Les valeurs d'initialisation peuvent être utiles même si on ne change pas de
# type de variable.




























print('\033[92m✓ OK' if total_cost == 174 else '\033[91m❌KO')
