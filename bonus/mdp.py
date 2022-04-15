# Écrivez un programme que génère un mot de passe de 8 caractères aléatoires,
# choisis parmi les 26 lettres minuscules et les 10 chiffres.

from random import choice

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

mdp = ""

for i in range(0, 8):
    lettre = choice(alpha)
    mdp = mdp + lettre

print(mdp)
