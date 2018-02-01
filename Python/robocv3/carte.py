# -*-coding:Utf-8 -*
from fonctions import *
import copy
"""Ce module contient la classe Carte."""
class Carte:

    """Classe permettant de gérer les cartes."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.map = creer_carte_depuis_chaine(chaine)
        self.PosRobot= [0,0]
        AncienRobot=trouve_le_robot(self.map)
        self.map[AncienRobot[1]][AncienRobot[0]]=" "
        self.Fin = False


    def __repr__(self):
        return "<Carte {}>".format(self.nom)
        
    def afficher(self,PositionDesRobots):
  
        tmpLaby=copy.deepcopy(self.map)  
        for Pos in PositionDesRobots:
            tmpLaby[Pos[1]][Pos[0]]="X"
        for row in tmpLaby:
            for column in row:
                print(column, end="")
            print(end="\n")
    def CreationNouvelleCarte(self,Joueur):
        tmpLaby=copy.deepcopy(self.map)  
        for Pos in Joueur:
            tmpLaby[Pos.Position[1]][Pos.Position[0]]=str(Pos.robot)
        strCarte=""
        for line in tmpLaby:
            strTemp = "".join(line)
            strCarte = strCarte +"\n"+ strTemp         
        return strCarte
        
    def PositionsLibres(self):
        CaseAutorisee=[" "]
        cases=[]
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if(self.map[i][j] == " "):
                    cases.append((i,j))  
        return cases
        

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
        