# Le juste prix
# choisir aléatoirement un prix entre 1 et 20
# tant que le jeu n'est pas fini
#     - demander au joueur d'entrer un prix
#     - s'il trouve le juste prix c'est gagné
#     - sinon on affiche "C'est moins" ou "C'est plus"

import random

# choisir un nombre aleatoire entre 1 et 50
prix = random.randint(1, 50)

# statut du jeu
gagne = False

# tant que le jeu est en cours d'éxécution
while gagne == False:

    # demander à joueur d'entrer un prix dans la console
    reponse = int(input("Entrer un prix: "))

    # si le prix est le meme que le juste prix
    if reponse == prix:
        print("Trouvé !")
        # fin du jeu
        gagne = True

    # si le prix de joueur est supérieur au prix à trouver
    elif reponse > prix:
        print("C'est moins")

    # si le prix de joueur est inférieur au prix à trouver
    elif reponse < prix:
        print("C'est plus")

# fin du jeu après la boucle
print("Fin du jeu !")
