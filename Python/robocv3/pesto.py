# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du serveur du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
import pickle
import re
from robot import Robot
from carte import Carte
from serveurClass import *
from random import * 

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            cartes.append(Carte(nom_carte,contenu))

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))


 

# Choix de la carte
#choix = input("Quelle carte voulez vous jouer? ")
#CarteChoisie devient le choix de carte
CarteChoisie=cartes[1]

print("Attente de connexion des clients")



# calculate position for each robot
Joueur=[]
Joueur.append(Robot("1",CarteChoisie)) 
Joueur.append(Robot("2",CarteChoisie)) 
Joueur[0].Position= choice(CarteChoisie.PositionsLibres())
Joueur[1].Position= choice(CarteChoisie.PositionsLibres())
print(Joueur[0].Position)
print(Joueur[1].Position)






