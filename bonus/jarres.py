# il y a trois jarre : 1, 2 et 3
# tirer aléatoirement un numéro de jarre
# le joueur doit donner un n° de jarre
# s'il choisit la même jarre que l'ordinateur il a gagné (afficher Gagner)
# sinon il a perdu (afficher Perdu)

import random

reponse = random.randint(1, 3)
choix = int(input("Choisit une jarre : 1, 2, 3 : "))

if choix == reponse:
    print("Gagné !")
else:
    print("Perdu !")
