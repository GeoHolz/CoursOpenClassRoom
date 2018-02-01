 # -*-coding:Utf-8 -*

def creer_labyrinthe_depuis_chaine(chaine):
    labyrinthe=[]
    for line in chaine.split('\n'):      
        labyrinthe.append(line)
    return labyrinthe