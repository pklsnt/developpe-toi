# Écrire un programme qui crée une liste d’entiers, puis
# Compte le nombre de multiples de 3 présents dans la liste

liste = [9, 24, 48, 2, 16]

# nombre de multiples de 3 présents dans liste
mult3 = 0

for nb in liste:
    if nb % 3 == 0:
        mult3 = mult3 + 1

print("Nombre de multiples de 3 : ", mult3)
