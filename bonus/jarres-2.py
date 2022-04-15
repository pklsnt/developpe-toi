# il y a trois jarre : 1, 2 et 3
# tirer aléatoirement un numéro de jarre
# le joueur doit donner un n° de jarre
# s'il choisit la même jarre que l'ordinateur gagne 1 point (afficher "Gagné ! vous avez x points")
# sinon il a perd un point (afficher "Perdu ! vous avez x points")
# le jeu s'arrête lorsque le joeur à 3 points
# NOTE : à chaque fois que le joueur gagne, il faut retirer un numéro

import random

points = 0
reponse = random.randint(1, 3)

while points != 3:
    choix = int(input("Choisit une jarre : 1, 2, 3: "))
    if choix == reponse:
        points += 1
        print(f"Gagné ! vous avez {points}/3")
        reponse = random.randint(1, 3)
    else:
        points -= 1
        print(f"Perdu ! vous avez {points}/3")

print("Tu deviens roi du temple")
