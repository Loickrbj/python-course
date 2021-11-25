# ÉTAPE 1
# Vous devez générer une liste "discount_products" qui contiendra uniquement
# les produits discount.
# Pour ces produits, vous devrez ajouter une clé "discount_cost" dont la valeur
# sera calculée en fonction du coût et de la réduction
# Exemple : -25% sur le tournevis, donc discount_cost = 3

# ÉTAPE 2
# Un client commande vos deux articles en promotion.
# Créez un dictionnaire "order" de type Order (type à créer) contenant les clés
# total_cost et total_discount_cost qui sont deux entiers.
# Calculez dans ce dictionnaire le total des articles, avec le prix original
# et le prix discount.

from typing import TypedDict

class Product(TypedDict, total=False):
    name: str
    cost: int
    discount: int
    discount_cost: float

products: list[Product] = [
  {
    "name": "Aspi Turbo Max",
    "cost": 150,
    "discount": 50
  },
  {
    "name": "Tournevis",
    "cost": 4,
    "discount": 25
  },
  {
    "name": "Marteau",
    "cost": 10
  }
]

################################################################################
discount_products  : list[Product] = list(filter(lambda discount_prod : 'discount' in discount_prod , products))

for discount_product in discount_products :
  if ("cost" in discount_product and "discount" in discount_product) :
    discount_product['discount_cost']  = float(discount_product["cost"] * (1-(discount_product["discount"]/100)))
print(discount_products)



################################################################################

# Lorsqu'on travaille avec des types aux propriétés optionnelles (voir
# total=False dans le type Product), il faut vérifier l'existence d'une
# propriété avant de s'en servir.

























#print('\033[92m✓ OK' if len(discount_products) == 2 and discount_products[0]['discount_cost'] == 75.0 and discount_products[1]['discount_cost'] == 3.0 and order['total_cost'] == 154 and order['total_discount_cost'] == 78 else '\033[91m❌KO')
