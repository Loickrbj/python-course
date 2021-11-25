# Voici votre premier boss de fin de niveau, un problème un peu plus complexe et
# avec un peu moins d'aide. Prenez votre temps : l'important est la réflexion
# que # vous développerez par vous même pour résoudre le problème.

# D'abord, déclarez une variable "a" possédant la valeur 42
# Ensuite, déclarez une variable "b" qui contiendra le carré de la variable "a"

# Enfin, trouvez un moyen d'intervertir les deux valeurs, de sorte que "b"
# contienne 42 et que "a" contienne le carré de 42.

# Attention, vous ne pouvez écrire "42" qu'une seule fois.

################################################################################
a : int = 42
b : int = pow(a,2)
c : int = a
a = b
b = c
################################################################################

print("a: ", a);
print("b: ", b);


































print('\033[92m✓ OK' if a == 1764 and b == 42 else '\033[91m❌KO')
