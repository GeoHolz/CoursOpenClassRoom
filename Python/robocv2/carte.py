# -*-coding:Utf-8 -*
from fonctions import *
import copy
"""Ce module contient la classe Carte."""
class Carte:

    """Classe permettant de gérer les cartes."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.map = creer_carte_depuis_chaine(chaine)
        self.PosRobot= trouve_le_robot(self.map)
        self.map[self.PosRobot[1]][self.PosRobot[0]]=" "


    def __repr__(self):
        return "<Carte {}>".format(self.nom)
        
    def afficher(self,PositionRobot):
  
        tmpLaby=copy.deepcopy(self.map)     
        tmpLaby[PositionRobot[1]][PositionRobot[0]]="X"
        for row in tmpLaby:
            for column in row:
                print(column, end="")
            print(end="\n")

        

    def PositionIsOk(self,position):
        CaseAutorisee=[" ",".","U"]
        if self.map[position[1]][position[0]] in CaseAutorisee:
            return True
        else:
            return False

    def PositionGagnee(self,position):
        if self.map[position[1]][position[0]] == "U":
            return True
        else:
            return False
        