# demandez à l'utilisateur de saisir un mot de passe
# calculer la longeur du mot de passe
# si la longeur est inférieur à 8 afficher le message "mot de passe trop court"
# si la longeur est entre 8 et 10 afficher le message "mot de passe moyen"
# si la longeur est supérieur ou égale à 10 afficher le message "mot de passe fort"

mot_de_passe = input("Entrez votre mot de passe: ")
longeur = len(mot_de_passe)

# verifier si le mot de passe est < 8 caractères
if longeur < 8:
    print("mot de passe trop court")
elif longeur >= 8 and longeur < 10:
    print("mot de passe moyen")
else:
    print("mot de passe valide")
