# Écrivez la fonction is_valid_email qui suivra les règles (simplifiées)
# suivantes. Un mail valide doit :

# - commencer par une chaîne d'au moins trois caractère contenant soit :
#   - des lettres minuscules
#   - des chiffres
#   - des points (mais pas au début ou à la fin de la chaîne). On accepte que
#     plusieurs point se suivent pour simplifier l'exercice.
# - continuer avec un "@"
# - continuer avec un nom de domaine de la forme domaine.tld
#   - domaine respecte les mêmes règles que la chaîne avant @
#   - tld est une série de 2 ou 3 lettres minuscules

################################################################################B
import re

def is_valid_mail(mail: str) -> bool:
    return True
################################################################################

# Tous les mails suivants sont valides : 

valid: list[str] = [
    "john.doe@mail.com",
    "j0hn.doe@mai1.com",
    "john.doe.yeah.yeah.yeah@mail.com",
    "john.doe@mail.mail.mail.com",
    "j@mail.com",
    "j.j@mail.com",
    "johh.doe@m.com",
    "jj@mail.com"
]

# Tous les mails suivant sont invalides :

invalid: list[str] = [
    ".john.doe@mail.com",
    ".john.doe.@mail.com",
    "john.doe@.mail.com",
    "john.doe@mail..com",
    "john.doe@mail.c",
    "john.doe@mail.coooomm",
    "John.doe@mail.com",
    "john.doe@Mail.com"
    "@john.doe@mail.com",
    "john.doe@mail.com@"
]

# Utilise https://regex101.com/ pour construire votre regex. Dans "Test string",
# copiez les mails ci-dessus pour voir ceux qui sont matchés

# 10 exercices sont insuffisants !
# Pour aller plus loin : https://regexlearn.com/learn

# PS : Les contraintes réelles pour une adresse mail sont en réalité bien plus
# vastes ! Pour info, voici la "vraie" regex. Sympathique, n'est-ce pas ?s
# (?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])












error = False
for mail in valid:
    if not is_valid_mail(mail):
        error = True
for mail in invalid:
    if is_valid_mail(mail):
        error = True
print('\033[92m✓ OK' if not error else '\033[91m❌KO')
