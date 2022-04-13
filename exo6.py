# Place de cinema
# demander l'age de la personne "Quel est votre age ?"
# si la personne est mineur (-12 ans) -> 7€
# si la personne a entre 12 et 18 -> 9€
# si la personne est majeur -> 15€

age = int(input("Quel est votre age ?"))

if age < 12:
    prix = 7
elif age >= 12 and age < 18:
    # elif 12 <= age < 18:
    prix = 9
else:
    prix = 15

print(f"Vous devez payer {prix} €")
