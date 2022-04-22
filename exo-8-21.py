# faire une boucle while qui demande des notes à l'élève
# et les mets dans un tableau tant que la réponse n'est pas "fin"
# parcourrir cette liste et calculer la moyenne
# afficher la moyenne de l'eleve
# "la moyenne de l'elève est x"
# Afficher en plus la note min et max

notes = []
somme = 0

while True:
    reponse = input("Entrez une note ou fin : ")
    if reponse == "fin":
        break
    else:
        notes.append(float(reponse))

for note in notes:
    somme = somme + note

moyenne = somme / len(notes)

print(f"Votre moyenne est de {moyenne}")
