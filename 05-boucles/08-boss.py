# En mathématiques, la suite de Fibonacci est une suite d'entiers dans laquelle
# chaque terme est la somme des deux termes qui le précèdent (Wikipédia).

# En voici le début :
# 0, 1, 1, 2, 3, 5, 8...

# Écrivez une fonction find_in_fibonacci_suite()
# Cette fonction prendra un tableau d'entiers.
# La fonction doit retourner le premier entier de la liste qui appartient à la
# suite de Fibonacci (ou 0 si aucun ne correspond).

################################################################################
def find_in_fibonacci_suite(nbrs : list[int]) :
    fibonacci : list[int] = [0,1]
    result : int  = 0
    for i in range(2,20):
        fibonacci.append(fibonacci[-2] + fibonacci[-1])

    for j in range(len(nbrs)):
        for x in range(len(fibonacci)) :
            if nbrs[j] == fibonacci[x] :
                return nbrs[j]
    return result
            


################################################################################






print('\033[92m✓ OK' if find_in_fibonacci_suite([1, 15, 75]) == 1 and find_in_fibonacci_suite([584, 987, 2]) == 987 and find_in_fibonacci_suite([144, 50, 89]) == 144 and find_in_fibonacci_suite([16, 87, 154]) == 0 else '\033[91m❌KO')
