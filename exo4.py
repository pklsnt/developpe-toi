# demander la valeur porte monnaie de l'utilisateur
# creer un produit qui aura pour valeur 50
# demander a l'utilisateur combien il achete de produit
# enlever le prix des produits au porte monnaie
# afficher la nouvelle valeur du porte monnaie

# demander la valeur porte monnaie de l'utilisateur
porte_monnaie = int(input("Combien avez vous dans votre porte monnaie ?: "))

# creer un produit qui aura pour valeur 50 euros
prix_produit = 50

# demander a l'utilisateur combien il achete de produit
nombre = int(input("Combien de produit voulez vous acheter ?: "))

# enlever le prix des produits au porte monnaie
porte_monnaie = porte_monnaie - (prix_produit * nombre)

# afficher la nouvelle valeur du porte monnaie
print(f"Apres votre achat, il vous reste {porte_monnaie}")
