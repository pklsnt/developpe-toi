# il y a trois jarre : 1, 2 et 3
# tirer aléatoirement un numéro de jarre
# le joueur doit donner un n° de jarre
# la joueur à 5 vies
# s'il choisit la même jarre que l'ordinateur, il gagne 10 point (afficher "Gagné ! vous avez x points")
# sinon il a perd une  vie (afficher "Perdu ! il vous reste x sur 5")
# le jeu s'arrête lorsque le joeur n'a plus de vie
# NOTE : à chaque fois que le joueur gagne, il faut retirer un numéro

import random

vies = 5
points = 0
reponse = random.randint(1, 3)

while vies > 0:
    choix = int(input("Choisit une jarre : 1, 2, 3: "))
    if choix == reponse:
        points += 10
        print(f"Gagné ! vous avez {points} points")
        reponse = random.randint(1, 5)
    else:
        vies = vies - 1
        print(f"Perdu ! il vous reste {vies} sur 5")

print(f"Terminé ! ton score est de {points}")
