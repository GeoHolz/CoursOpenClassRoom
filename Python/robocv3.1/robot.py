# -*-coding:Utf-8 -*

"""Ce module contient la classe Robot qui permet de déplacement."""

class Robot:

    """Classe représentant un Robot."""

    def __init__(self, robot,carte):
        self.robot = robot
        self.Position = ["0","0"]
        self.carte=carte

    def deplacement(self, destination, carte): 
        print("destination=",destination)
        #Si la destination est vers l'est
        print("Position du robot:",self.Position)
        if(destination)=="E":
            NouvellePosition=[0,0]
            NouvellePosition[0]=self.Position[0]+1
            NouvellePosition[1]=self.Position[1]
            if self.carte.PositionIsOk(NouvellePosition):
               self.Position[0]=NouvellePosition[0]
               self.Position[1]=NouvellePosition[1]
   
        #Si la destination est vers l'ouest                
        if(destination)=="O":
            NouvellePosition=[0,0]
            NouvellePosition[0]=self.Position[0]-1
            NouvellePosition[1]=self.Position[1]

            if self.carte.PositionIsOk(NouvellePosition):
               self.Position[0]=NouvellePosition[0]
               self.Position[1]=NouvellePosition[1]
               
        #Si la destination est vers le nord                
        if(destination)=="N":
            NouvellePosition=[0,0]
            NouvellePosition[0]=self.Position[0]
            NouvellePosition[1]=self.Position[1]-1
            if self.carte.PositionIsOk(NouvellePosition):
               self.Position[0]=NouvellePosition[0]
               self.Position[1]=NouvellePosition[1] 
               
        #Si la destination est vers le sud
        if(destination)=="S":
            NouvellePosition=[0,0]
            NouvellePosition[0]=self.Position[0]
            NouvellePosition[1]=self.Position[1]+1
            if self.carte.PositionIsOk(NouvellePosition):
               self.Position[0]=NouvellePosition[0]
               self.Position[1]=NouvellePosition[1]  
        #Test si le robot est sur la sortie
        if self.carte.PositionGagnee(self.Position):
            return True
    
    def CreerMur(self, destination, carte): 
        PositionDuMur=[0,0]
        if(destination[1] == "N"):
            PositionDuMur[0]=self.Position[0]
            PositionDuMur[1]=self.Position[1]-1
        if(destination[1] == "S"):
            PositionDuMur[0]=self.Position[0]
            PositionDuMur[1]=self.Position[1]+1
        if(destination[1] == "E"):
            PositionDuMur[0]=self.Position[0]+1
            PositionDuMur[1]=self.Position[1]
        if(destination[1] == "O"):
            PositionDuMur[0]=self.Position[0]-1
            PositionDuMur[1]=self.Position[1]
        print("Position du mur",PositionDuMur)
        print(carte.map[PositionDuMur[1]][PositionDuMur[0]])
        if(carte.map[PositionDuMur[1]][PositionDuMur[0]] == "."):
            carte.map[PositionDuMur[1]][PositionDuMur[0]]="O"

    def CreerPorte(self, destination, carte):
        PositionDeLaPorte=[0,0]
        if(destination[1] == "N"):
            PositionDeLaPorte[0]=self.Position[0]
            PositionDeLaPorte[1]=self.Position[1]-1
        if(destination[1] == "S"):
            PositionDeLaPorte[0]=self.Position[0]
            PositionDeLaPorte[1]=self.Position[1]+1
        if(destination[1] == "E"):
            PositionDeLaPorte[0]=self.Position[0]+1
            PositionDeLaPorte[1]=self.Position[1]
        if(destination[1] == "O"):
            PositionDeLaPorte[0]=self.Position[0]-1
            PositionDeLaPorte[1]=self.Position[1]
        print("Position de la porte",PositionDeLaPorte)
        print(carte.map[PositionDeLaPorte[1]][PositionDeLaPorte[0]])
        if(carte.map[PositionDeLaPorte[1]][PositionDeLaPorte[0]] == "O"):
            carte.map[PositionDeLaPorte[1]][PositionDeLaPorte[0]]="."
