# Félicitations, vous êtes l'heureux(se) propriétaire d'une pizzeria.

# Vous recevez les commandes des clients sous la forme d'un tableau de
# dictionnaires de type Pizza.

# Le coût d'une pizza est basé sur ses ingrédients. Les coûts sont stockés dans
# le tableau available_ingredients.

# Écrivez le contenu de la fonction get_cost_for_order pour qu'elle renvoit le
# coût total de la commande.

from typing import TypedDict

class Ingredient(TypedDict):
    name: str
    cost: int

class Pizza(TypedDict):
    quantity: int
    ingredients: list[Ingredient]

available_ingredients: list[Ingredient] = [
    { "name": "tomato", "cost": 1 },
    { "name": "onions", "cost": 1 },
    { "name": "egg", "cost": 2 },
    { "name": "olives", "cost": 1 },
    { "name": "cheese", "cost": 2 }
]

################################################################################

def get_cost_for_order(pizzas: list[Pizza]) -> int:

  cost : int = 0
  for pizza in pizzas :
    for ingredient in pizza["ingredients"]:
      cost += ingredient.get('cost') * pizza.get("quantity")
  return cost;


################################################################################

# Exemple de commande :
# 2 pizzas avec tomates, onions et oeuf (1€ + 1€ + 2€) = 4€ * 2 = 8€
# 1 pizza avec tomates, oeuf et fromage (1€ + 2€ + 2€) = 5€
# Total = 8€ + 5€ = 13€

order: list[Pizza] = [
    {
        "quantity": 2,
        "ingredients": [available_ingredients[0], available_ingredients[1], available_ingredients[2]]
    },
    {
        "quantity": 1,
        "ingredients": [available_ingredients[0], available_ingredients[2], available_ingredients[4]]
    }
]
get_cost_for_order(order)

































order1: list[Pizza] = [
  {
    "quantity": 2,
    "ingredients": [available_ingredients[0], available_ingredients[1], available_ingredients[2]]
  },
  {
    "quantity": 1,
    "ingredients": [available_ingredients[0], available_ingredients[2], available_ingredients[4]]
  }
]
order2: list[Pizza] = [
  {
    "quantity": 5,
    "ingredients": [available_ingredients[0], available_ingredients[1], available_ingredients[2], available_ingredients[3], available_ingredients[4]]
  }
]
print('\033[92m✓ OK' if get_cost_for_order(order1) == 13 and get_cost_for_order(order2) == 35 else '\033[91m❌KO')
