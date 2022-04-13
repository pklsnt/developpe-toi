# Place de cinema
# demander l'age de la personne "Quel est votre age ?"
# si la personne est mineur (-12 ans) -> 7€
# si la personne a entre 12 et 18 -> 9€
# si la personne est majeur
# demander si elle est étudiante (n ou o)
#   si elle est etudiante -> 12€
#   sinon 15€

age = int(input("Quel est votre age ?"))

if age < 12:
    prix = 7
elif age >= 12 and age < 18:
    prix = 9
else:
    etudiant = input("Etes-vous étudiant (o / n) ?")
    if etudiant == "o":
        prix = 12
    else:
        prix = 15

print(f"Vous devez payer {prix} €")
