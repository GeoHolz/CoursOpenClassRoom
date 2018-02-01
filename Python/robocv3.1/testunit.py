import random
import unittest
import copy
from fonctions import *
from random import * 
from carte import Carte
from robot import Robot

class RandomTest(unittest.TestCase):

    def test_CreationLabDepuisChaine(self):

        """Test le fonctionnement de la fonction 'creer_carte_depuis_chaine'."""
        chaine ="OOOO\nO .O\nOXOO"
        cartedepuischaine=creer_carte_depuis_chaine(chaine)
        TmpChaine=""
        Test = None
        for i in range(len(cartedepuischaine)):
            for j in range(len(cartedepuischaine[i])):
                TmpChaine=TmpChaine+cartedepuischaine[i][j]
            if(i != len(cartedepuischaine)-1):
                TmpChaine=TmpChaine+"\n"
        self.assertEqual(chaine,TmpChaine)

    def test_ConsitutionLab(self):
        """Test la constitution d'un labyrinthe standard :
            - test si aucun robot n'est present dans le lab apres son initialisation
            - test si le tableau de coordonées correspond bien à la chaine"""

        Test = None
        chaine="OOOUOOOO\nO      O\nU  X   U\nO      O\nOOOUOOOO"
        Laby=Carte("TestUnit",chaine)
        if("X" in Laby.map):
            Test = 123
        if((chaine.count("\n")+1) != len(Laby.map)):
            Test = 123
        self.assertIsNone(Test)

    def test_Multijoueur(self):
        """Test les fonctionnalités multijoueur. On instancie une carte et deux joueurs puis on test si les deux joueurs n ont pas la même place sur le laby et si ils sont bien affiches sur la carte transmis"""
        Test = None
        chaine="OOOUOOOO\nO      O\nU  X   U\nO      O\nOOOUOOOO"
        Laby=Carte("TestUnit",chaine)
        Joueur=[]
        PosLibre=copy.deepcopy(Laby.PositionsLibres())
        Joueur.append(Robot(0,Laby)) 
        PositionTemp=list(choice(PosLibre))
        Joueur[0].Position[0]=PositionTemp[1]
        Joueur[0].Position[1]=PositionTemp[0]
        PosLibre.remove(tuple(PositionTemp))
        Joueur.append(Robot(1,Laby)) 
        PositionTemp=list(choice(PosLibre))
        Joueur[1].Position[0]=PositionTemp[1]
        Joueur[1].Position[1]=PositionTemp[0]
        PosLibre.remove(tuple(PositionTemp))
        if(Joueur[0].Position == Joueur[1].Position):
            Test = 123
        
        ChaineAffichage = Laby.CreationNouvelleCarte(Joueur)
        if("0" not in ChaineAffichage):
            Test = 123
        if("1" not in ChaineAffichage):
            Test = 123
        self.assertIsNone(Test)