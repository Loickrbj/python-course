# Si l'on souhaite connaître l'index de chaque élément au moment où on parcourt
# la liste, la fonction enumerate est utile :

# for index, letter in enumerate(["a", "b", "c"])

# letter vaudra "a", "b", "c", tandis que index vaudra 0, 1, 2

# Les nombres du tableau ci-dessous sont en ordre croissant, sauf un qui ne
# respecte pas la règle. Trouvez le et supprimez-le grâce à son index.

################################################################################
numbers: list[int] = [2, 5, 7, 9, 55, 98, 120, 152, 154, 120, 177, 497, 10598]
################################################################################

for index, number in enumerate(numbers):
    if (index >0 and number < numbers[index - 1]):
        numbers.pop(index)
        

































print('\033[92m✓ OK' if numbers == [2, 5, 7, 9, 55, 98, 120, 152, 154, 177, 497, 10598] else '\033[91m❌KO')
