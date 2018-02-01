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
from fonctions import *

def sendMapToAll():
    """Send map representation to all clients"""
        
    tmpCarte=CarteChoisie.CreationNouvelleCarte(Joueur)
    for client in server.connectedClients:
        server.sendString(client, tmpCarte)


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
choix = input("Quelle carte voulez vous jouer? ")
#CarteChoisie devient le choix de carte
CarteChoisie=cartes[int(choix)-1]

print("Attente de connexion des clients")

server = Server(CarteChoisie)
#Lancement du serveur
server.start()
#Le serveur attends que les clients se connectent et attends un c en retour pour commencer la partie
server.waitForClient()
# calculate position for each robot
Joueur=[]
NbrClientConnecte=0
for client in server.connectedClients:
    Joueur.append(Robot(NbrClientConnecte+1,CarteChoisie)) 
    PositionTemp=list(choice(CarteChoisie.PositionsLibres()))
    Joueur[NbrClientConnecte].Position[0]=PositionTemp[1]
    Joueur[NbrClientConnecte].Position[1]=PositionTemp[0]
    print("Positon du robot numéro {} au debut : {}".format(str(NbrClientConnecte+1),Joueur[NbrClientConnecte].Position))
    NbrClientConnecte+=1

    
############################################### DEBUG A LA CON ##################################################    
# for player in Joueur:
    # print(player.robot)
    # print(player.Position)
    # print(player.carte)
    
    
sendMapToAll()

# game loop :
#     - get next client
#     - notify him that it's his turn
#     - wait for client input
#     - move the robot
#     - send the updated map
currentClientIndex = -1
nbClients = len(server.connectedClients)
while not CarteChoisie.Fin:
    # switch to next client and tell him that it's his turn
    currentClientIndex = (currentClientIndex + 1) % nbClients
    currentClient = server.connectedClients[currentClientIndex]
    server.sendString(currentClient, "TURN")
    print("Player {0}'s turn".format(currentClientIndex + 1))

    # wait for client's input
    clientMove = currentClient.recv(server.MSG_LEN).decode().rstrip()
    
    # move his robot
    CarteChoisie.Fin=Joueur[currentClientIndex].deplacement(clientMove,CarteChoisie)


    # send the updated map to all players
    sendMapToAll()

# Avoid program from exiting
print('Partie termine, aurevoir')
for client in server.connectedClients:
    client.close()
    server.close()
