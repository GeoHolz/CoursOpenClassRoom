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
        # On cherche le robot dans la carte existante et on l'efface
        AncienRobot=trouve_le_robot(self.map)
        self.map[AncienRobot[1]][AncienRobot[0]]=" "
        self.Fin = False


    def __repr__(self):
        return "<Carte {}>".format(self.nom)
        
    def afficher(self,PositionDesRobots):
        #Permet d'afficher la carte à l'écran
        tmpLaby=copy.deepcopy(self.map)  
        for Pos in PositionDesRobots:
            tmpLaby[Pos[1]][Pos[0]]="X"
        for row in tmpLaby:
            for column in row:
                print(column, end="")
            print(end="\n")
    def CreationNouvelleCarte(self,Joueur):
        #Permet d'afficher la carte en mode multijoueur
        tmpLaby=copy.deepcopy(self.map)  
        for Pos in Joueur:
            tmpLaby[Pos.Position[1]][Pos.Position[0]]=str(Pos.robot)
        strCarte=""
        for line in tmpLaby:
            strTemp = "".join(line)
            strCarte = strCarte +"\n"+ strTemp         
        return strCarte
        
    def PositionsLibres(self):
        # Renvoie une liste avec toutes les positions libres
        CaseAutorisee=[" "]
        cases=[]
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if(self.map[i][j] == " "):
                    cases.append((i,j))  
        return cases
        

    def PositionIsOk(self,position):
        # Permet de savoir si une position est ok pour s'y deplacer
        CaseAutorisee=[" ",".","U"]
        try:
            if(self.map[position[1]][position[0]] in CaseAutorisee):
                return True
        except IndexError:
            return False

    def PositionGagnee(self,position):
        #Permet de savoir si le robot se trouve sur la sortie
        if self.map[position[1]][position[0]] == "U":
            return True
        else:
            return False
        