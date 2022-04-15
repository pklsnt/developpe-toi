notes = [12, 5, 9, 8, 17]
somme = 0

for note in notes:
    somme = somme + note

moyenne = somme / len(notes)

print(f"Votre moyenne est de {moyenne}")
