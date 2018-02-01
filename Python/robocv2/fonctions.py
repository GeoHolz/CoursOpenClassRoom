# -*-coding:Utf-8 -*
# Fonctions
def creer_carte_depuis_chaine(chaine):
    labyrinthe=[]  
    tmpLigne=0
    for line in chaine.split('\n'):
        labyrinthe.append([])
        for char in line:
            labyrinthe[tmpLigne].append(char)
        tmpLigne=tmpLigne+1     
    return labyrinthe
    
def trouve_le_robot(labyrinthe):
    PositionY=0
    for row in labyrinthe:        
        if "X" in row:
            PositionX=row.index("X")
            break
        PositionY=PositionY+1
    return([PositionX,PositionY])
    