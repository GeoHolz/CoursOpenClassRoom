# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
import pickle
import re

from carte import Carte

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

#On charge et on affiche la partie sauvegardée  
try:
    with open('donnees', 'rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        cartes.append(mon_depickler.load())
        print("Partie sauvegardé trouvé :")
        print("  {} - {}".format(i + 2, cartes[i+1].nom))
except FileNotFoundError:
    print("Pas de partie sauvegardé trouvé")
    #doesn't exist
# Choix de la carte
choix = input("Quelle carte voulez vous jouer? ")
PartieEnCours=cartes[int(choix)-1]
PartieEnCours.afficher() 
EntreeUtilisateur="k"
while True:
    EntreeUtilisateur = input("Par ou qu'on va ? ")
    if not re.match("^[sSoOnNeEqQ][0-9]*$",EntreeUtilisateur):
        print("Entrée non valide, rappel touche N E S O pour la direction suivi du nombre de case (ex: s4 ) et Q pour quitter")
        continue
    if(EntreeUtilisateur.upper() == "Q"):
        print("A plus dans le bus")
        break
    if len(EntreeUtilisateur) == 1:
        EntreeUtilisateur=EntreeUtilisateur+"1"
    i=0
    while i < int(EntreeUtilisateur[1:]):
        destination=''.join(EntreeUtilisateur[0])
        destination=destination.upper()
        PartieGagnee=PartieEnCours.deplacement(destination)
        i+=1
        PartieEnCours.afficher()
        if(PartieGagnee):
            break
    if(PartieGagnee):
        print("Vous avez gagné la partie")
        try:
             os.remove("donnees")
        except:
            pass
        break
    #Enregistrement du coup joué
    with open('donnees', 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(PartieEnCours)
    
    