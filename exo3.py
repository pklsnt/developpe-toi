# demander les 3 notes de l'eleve
# note1, note2, note3
# calculer la moyenne
# afficher la moyenne de l'eleve
# "la moyenne de l'elève est x"
# /!\ division

# demander les 3 notes de l'eleve
note1 = int(input("Entrez la premiere note: "))
note2 = int(input("Entrez la seconde note: "))
note3 = int(input("Entrez la dernière note: "))

# calculer la moyenne
moyenne = (note1 + note2 + note3) / 3

# afficher la moyenne de l'eleve
print("la moyenne de l'elève est " + str(moyenne))
print("la moyenne de l'elève est ", moyenne)
print(f"la moyenne de l'elève est {moyenne}")
