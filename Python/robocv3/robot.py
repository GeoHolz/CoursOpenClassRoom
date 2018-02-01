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
        
