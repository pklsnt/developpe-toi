liste = [8, 24, 48, 2, 16]
long = len(liste)

# afficher les elements de la liste
for i in range(0, len(liste)):
    print("element", liste[i])

# liste miroir
for i in range(0, len(liste)):
    print("mirroir", liste[len(liste) - 1 - i])
