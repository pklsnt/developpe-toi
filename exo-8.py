# mettre les 3 notes de l'eleve dans une liste
# parcourrir cette liste et calculer la moyenne
# afficher la moyenne de l'eleve
# "la moyenne de l'elève est x"
# Afficher en plus la note min et max

notes = [12, 5, 9, 8, 17]
somme = 0

for note in notes:
    somme = somme + note

moyenne = somme / len(notes)

print(f"Votre moyenne est de {moyenne}")
