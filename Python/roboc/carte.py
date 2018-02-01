# -*-coding:Utf-8 -*
# print "Il est passé par ici.."
# print "Il repassera par la.."
from fonctions import *
"""Ce module contient la classe Carte."""

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom       
        self.labyrinthe = creer_labyrinthe_depuis_chaine(chaine)
        self.posXline=0 #Le numéro de la ligne sur laquel est le robot
        self.posXindex=0 #L'index de la positionn du robot
        self.OldPosDoor=False

    def __repr__(self):
        return "<Carte {}>".format(self.nom)
        
    def afficher(self):
        for line in self.labyrinthe:
            print(line)
    def deplacement(self,destination):
        #On recherche la position du robot et on note le numéro de sa ligne ainsi que son index dans celle ci
        i=0
        for line in self.labyrinthe:               
            if "X" in line:
                posXline=i
                posXindex=line.index("X")
            i+=1
        #Si la destination est vers l'est
        if(destination)=="E":
            tempLigne=list(self.labyrinthe[posXline])
            if(tempLigne[posXindex+1]==" "):
                if(self.OldPosDoor==True):
                    tempLigne[posXindex]="."
                    self.OldPosDoor=False
                else:
                    tempLigne[posXindex]=" "
                tempLigne[posXindex+1]="X"
                self.labyrinthe[posXline]=''.join(tempLigne)
            if(tempLigne[posXindex+1]=="U"): 
                tempLigne[posXindex+1]="X"
                tempLigne[posXindex]=" "
                self.labyrinthe[posXline]=''.join(tempLigne)
                return True
            if(tempLigne[posXindex+1]=="."):
                tempLigne[posXindex+1]="X"
                tempLigne[posXindex]=" "
                self.OldPosDoor=True      
                self.labyrinthe[posXline]=''.join(tempLigne)        
        #Si la destination est vers l'ouest                
        if(destination)=="O":
            tempLigne=list(self.labyrinthe[posXline])
            if(tempLigne[posXindex-1]==" "):
                if(self.OldPosDoor==True):
                    tempLigne[posXindex]="."
                    self.OldPosDoor=False
                else:
                    tempLigne[posXindex]=" "
                tempLigne[posXindex-1]="X"
                self.labyrinthe[posXline]=''.join(tempLigne)
            if(tempLigne[posXindex-1]=="U"):
                tempLigne[posXindex-1]="X"
                tempLigne[posXindex]=" "
                self.labyrinthe[posXline]=''.join(tempLigne)
                return True
            if(tempLigne[posXindex-1]=="."):
                tempLigne[posXindex-1]="X"
                tempLigne[posXindex]=" "
                self.OldPosDoor=True      
                self.labyrinthe[posXline]=''.join(tempLigne)
        #Si la destination est vers le nord                
        if(destination)=="N":
            tempLigne=list(self.labyrinthe[posXline-1])
            tempLigne2=list(self.labyrinthe[posXline])
            if(tempLigne[posXindex]==" "):
                if(self.OldPosDoor==True):
                    tempLigne2[posXindex]="."
                    self.OldPosDoor=False
                else:
                    tempLigne2[posXindex]=" "
                tempLigne[posXindex]="X"
                self.labyrinthe[posXline]=''.join(tempLigne2)         
                self.labyrinthe[posXline-1]=''.join(tempLigne)
            if(tempLigne[posXindex]=="U"):
                tempLigne[posXindex]="X"
                tempLigne2[posXindex]=" "
                self.labyrinthe[posXline]=''.join(tempLigne2)         
                self.labyrinthe[posXline-1]=''.join(tempLigne)
                return True
            if(tempLigne[posXindex]=="."):
                tempLigne[posXindex]="X"
                tempLigne2[posXindex]=" "
                self.OldPosDoor=True
                self.labyrinthe[posXline]=''.join(tempLigne2)         
                self.labyrinthe[posXline-1]=''.join(tempLigne)             
        #Si la destination est vers le sud
        if(destination)=="S":
            tempLigne=list(self.labyrinthe[posXline+1])
            tempLigne2=list(self.labyrinthe[posXline])
            if(tempLigne[posXindex]==" "):
                if(self.OldPosDoor==True):
                    tempLigne2[posXindex]="."
                    self.OldPosDoor=False
                else:
                    tempLigne2[posXindex]=" "
                tempLigne[posXindex]="X"
                self.labyrinthe[posXline]=''.join(tempLigne2)         
                self.labyrinthe[posXline+1]=''.join(tempLigne)  
            if(tempLigne[posXindex]=="U"):
                tempLigne[posXindex]="X"
                tempLigne2[posXindex]=" "
                self.labyrinthe[posXline]=''.join(tempLigne2)         
                self.labyrinthe[posXline+1]=''.join(tempLigne)  
                return True
            if(tempLigne[posXindex]=="."):
                tempLigne[posXindex]="X"
                tempLigne2[posXindex]=" "
                self.OldPosDoor=True
                self.labyrinthe[posXline]=''.join(tempLigne2)         
                self.labyrinthe[posXline+1]=''.join(tempLigne)  
        
