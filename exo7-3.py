# Le juste prix
# choisir aléatoirement un prix entre 1 et 20
# tant que le jeu n'est pas fini
#     - demander au joueur d'entrer un prix
#     - s'il trouve le juste prix c'est gagné
#     - sinon on affiche "C'est moins" ou "C'est plus"
# l'utilisateur n'a que 3 coups

import random

# choisir un nombre aleatoire entre 1 et 50
prix = random.randint(1, 50)

# statut du jeu
gagne = False

# nombre de coup
nb_coup = 0

# tant que le jeu est en cours d'éxécution
while gagne == False:

    # demander à joueur d'entrer un prix dans la console
    reponse = int(input("Entrer un prix: "))
    nb_coup = nb_coup + 1

    # si le prix est le meme que le juste prix
    if reponse == prix:
        print("Trouvé !")
        # fin du jeu
        gagne = True

    # si le prix de joueur est supérieur au prix à trouver
    elif reponse > prix:
        print(f"C'est moins ! il vous reste {3 - nb_coup} essais")

    # si le prix de joueur est inférieur au prix à trouver
    else:
        print(f"C'est plus ! il vous reste {3 - nb_coup} essais")

    if nb_coup == 3:
        break

# fin du jeu après la boucle
print("Fin du jeu !")
