# Écrivez un programme qui simule un tirage Euro Millions :
# cinq numéros tirés au sort entre 1 et 50, suivi de deux étoiles numérotées de 1 à 12.

# Astuces : L'instruction numeros = list(range(a,b)) crée la liste des entiers entre a (compris)
# et b (non compris). Cela vous évitera d'écrire une liste de 50 nombres.

# exemple
# [37, 8, 25, 24, 44]
# [12, 3]

from random import choice

numeros = list(range(1, 51))
etoiles = list(range(1, 13))

tirage_numero = []
tirage_etoile = []

for i in range(5):
    tirage_numero.append(choice(numeros))

for j in range(2):
    tirage_etoile.append(choice(etoiles))

print(tirage_numero)
print(tirage_etoile)
