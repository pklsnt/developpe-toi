# demandez à l'utilisateur de saisir un mot de passe
# calculer la longeur du mot de passe
# si la longeur est inférieur à 8 afficher le message "mot de passe trop court"
# si la longeur est supérieur ou égale à 8 afficher le message "mot de passe valide"

mot_de_passe = input("Entrez votre mot de passe: ")
longeur = len(mot_de_passe)

# verifier si le mot de passe est < 8 caractères
if longeur < 8:
    print("mot de passe trop court")
else:
    print("mot de passe valide")
