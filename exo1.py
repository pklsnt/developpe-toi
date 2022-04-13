# demander le nom de l'utilisateur
# demander l'age de l'utilisateur
# afficher "Bonjour nom tu as age ans"

nom = input("Quel est ton nom?")
age = input("Quel est ton age?")

# methode 1
print("Bonjour", nom, "tu as", age, "ans")

# methode 2
print("Bonjour " + nom + " tu as " + age + " ans")

# methode 3 f-string
print(f"Bonjour {nom} tu as {age} ans")
