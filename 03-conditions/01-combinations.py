# Et si on combinait les comparaisons ?

# Avec les mots clés "and" et "or", vous pouvez combiner des tests

# La variable is_teenager vous montre comment

# Créez une variable can_buy_gun qui sera vraie si le pays est "USA" et l'âge
# est supérieur ou égal à 21

# Créez une variable can_drink qui sera vraie si le pays est "France" et l'âge
# supérieur ou égal à 18, ou si le pays est "USA" et l'age supérieur ou égal à 
# 21 (âge minimum pour la vente d'alcool aux USA)

################################################################################
country: str = "France"
age: int = 20
is_teenager: bool = (age >= 10 and age <= 19)
################################################################################
can_buy_gun : bool = (age>= 21 and country == "USA")
can_drink : bool = (age >= 18 and country == "France" or age>= 21 and country =="USA")

print("Is teenager :", is_teenager);
print("Can buy gun :", can_buy_gun);
print("Can drink :", can_drink);

# Le code de vérification ne fait pas tout ! Vérifiez qu'en changeant vos deux
# variables country et age, le résultat est cohérent.


















print('\033[92m✓ OK' if not can_buy_gun and can_drink else '\033[91m❌KO')
