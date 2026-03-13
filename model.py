NB_CASES = 9

#ajout du champ "promu" dans les tuples de la liste
plateau = [
    [["香","Sente", False],["桂","Sente", False],["銀","Sente", False],["金","Sente", False],["王","Sente", False],["金","Sente", False],["銀","Sente", False],["桂","Sente", False],["香","Sente", False]],
    [["",None, False],["飛","Sente", False],["",None, False],["",None, False],["",None, False],["",None, False],["",None, False],["角","Sente", False],["",None, False]],
    [["歩","Sente", False],["歩","Sente", False],["歩","Sente", False],["歩","Sente", False],["歩","Sente", False],["歩","Sente", False],["歩","Sente", False],["歩","Sente", False],["歩","Sente", False]],
    [["",None, False]]*9,
    [["",None, False]]*9,
    [["",None, False]]*9,
    [["歩","Gote", False],["歩","Gote", False],["歩","Gote", False],["歩","Gote", False],["歩","Gote", False],["歩","Gote", False],["歩","Gote", False],["歩","Gote", False],["歩","Gote", False]],
    [["",None, False],["角","Gote", False],["",None, False],["",None, False],["",None, False],["",None, False],["",None, False],["飛","Gote", False],["",None, False]],
    [["香","Gote", False],["桂","Gote", False],["銀","Gote", False],["金","Gote", False],["王","Gote", False],["金","Gote", False],["銀","Gote", False],["桂","Gote", False],["香","Gote", False]],
]
priseSente = [["角",0],["飛",0],["金",0],["銀",0],["桂",0],["香",0],["歩",0]]
priseGote = [["角",0],["飛",0],["金",0],["銀",0],["桂",0],["香",0],["歩",0]]
indexPara = 0

def getPiece(x, y):
    return plateau[y][x][0]

def getParachutage(piece, joueur):
    i = 0
    global indexPara
    prisesDispo = []
    if(joueur == "Sente"):
        for p in priseSente:
            if p[1] > 0:
                prisesDispo.append(p[0])
        if piece < len(prisesDispo):
            return (prisesDispo[piece], "Sente")
    elif(joueur == "Gote"):
        for p in priseGote:
            if p[1] > 0:
                prisesDispo.append(p[0])
        if piece < len(prisesDispo):
            return (prisesDispo[piece], "Gote")
def parachutage(joueur, x, y, piece):
    global indexPara
    if plateau[y][x][0]=="":
        plateau[y][x]=[piece, joueur, False]
        if(joueur == "Gote"):
            for i in range(7):
                if priseGote[i][0] == piece:
                    priseGote[i][1]-=1
        else:
            for i in range(7):
                if priseSente[i][0] == piece:
                    priseSente[i][1]-=1
    indexPara=0
        

def deplacerPiece(x1, y1, x2, y2):
    reussiteDep = False
    prise = plateau[y2][x2][0]
    if(plateau[y1][x1][1] != plateau[y2][x2][1]):
        if(plateau[y1][x1][0]=="歩"):
            reussiteDep = deplacerPion(x1, y1, x2, y2, plateau[y1][x1][1])

        if(plateau[y1][x1][0]=="角"):
            reussiteDep = deplacerFou(x1, y1, x2, y2, plateau[y1][x1][1])

        if(plateau[y1][x1][0]=="飛"):
            reussiteDep = deplacerTour(x1, y1, x2, y2, plateau[y1][x1][1])

        if(plateau[y1][x1][0]=="香"):
            reussiteDep = deplacerLance(x1, y1, x2, y2, plateau[y1][x1][1])

        if(plateau[y1][x1][0]=="桂"):
            reussiteDep = deplacercavalier(x1, y1, x2, y2, plateau[y1][x1][1])

        if(plateau[y1][x1][0]=="銀"):
            reussiteDep = deplacerGeneralargent(x1, y1, x2, y2, plateau[y1][x1][1])

        if(plateau[y1][x1][0]=="金" or (plateau[y1][x1][2] == True and (plateau[y1][x1]!="飛" or plateau[y1][x1][0]!="角" or plateau[y1][x1]!="王"))):
            reussiteDep = deplacerGeneralor(x1, y1, x2, y2, plateau[y1][x1][1])

        if(plateau[y1][x1][0]=="王"):
            reussiteDep = deplacerRoi(x1, y1, x2, y2, plateau[y1][x1][1])
        if reussiteDep == True :
            if ((plateau[y2][x2][1] == "Gote")):
                if y2 <=2:
                    plateau[y2][x2][2]=True
                if prise != "":
                    for piece in priseGote:
                        if piece[0]==prise:
                            piece[1]+=1
            elif (plateau[y2][x2][1] == "Sente"):
                if y2 >=6:
                    plateau[y2][x2][2]=True
                if prise != "":
                    for piece in priseSente:
                        if piece[0] == prise:
                            piece[1]+=1
        
def deplacerPion(x1, y1, x2, y2, joueur):
    if(x1 == x2):
        if((y2 == y1+1 and joueur == "Sente")or(y2 == y1-1 and joueur == "Gote")):
                        plateau[y2][x2] = plateau[y1][x1]
                        plateau[y1][x1] = ("",None, False)
    return True

def deplacerFou(x1, y1, x2, y2, joueur): 
    dx = x2 - x1
    dy = y2 - y1

    # Vérifie diagonale
    if ((dx != dy)and(dx != -dy)):
        if(((abs(dx)==1 and abs(dy)==0)or(abs(dx)==0 and abs(dy)==1)) and plateau[y1][x1][2]==True):
            plateau[y2][x2] = plateau[y1][x1]
            plateau[y1][x1] = ("", None, False)
            return True
        return False

    step_x = 1 if dx > 0 else -1
    step_y = 1 if dy > 0 else -1

    x = x1 + step_x
    y = y1 + step_y

    # Vérifie chemin libre
    while (x, y) != (x2, y2):
        if plateau[y][x][0] != "":
            return False
        x += step_x
        y += step_y

    # Vérifie capture
    piece_cible, joueur_cible, _ = plateau[y2][x2]
    if joueur_cible == joueur:
        return False

    plateau[y2][x2] = plateau[y1][x1]
    plateau[y1][x1] = ("", None, False)
    return True

def deplacerTour(x1, y1, x2, y2, joueur):
    dx = x2 - x1
    dy = y2 - y1
    if dx != 0 and dy != 0:
        if((abs(dx) == 1 and abs(dx)== abs(dy)) and plateau[y1][x1][2]==True):
            plateau[y2][x2] = plateau[y1][x1]
            plateau[y1][x1] = ("", None, False)
            return True
        return False

    # Détermine la direction
    if dx != 0:
        step_x = 1 if dx > 0 else -1
        step_y = 0
    else:
        step_x = 0
        step_y = 1 if dy > 0 else -1

    x = x1 + step_x
    y = y1 + step_y

    # Vérifie que le chemin est libre
    while (x, y) != (x2, y2):
        if plateau[y][x][0] != "":
            return False
        x += step_x
        y += step_y

    # Vérifie capture
    piece_cible, joueur_cible, _ = plateau[y2][x2]
    if joueur_cible == joueur:
        return False

    # Déplacement
    plateau[y2][x2] = plateau[y1][x1]
    plateau[y1][x1] = ("", None, False)

    return True
    
def  deplacerLance(x1, y1, x2, y2, joueur):  
    dx = x2 - x1
    dy = y2 - y1

    # La lance ne peut bouger que verticalement
    if dx != 0:
        return False

    # Direction selon joueur
    if joueur == "Gote":
        if dy >= 0:  # Gote avance vers le haut (dy négatif)
            return False
        step_y = -1
    else:  # blanc
        if dy <= 0:  # Blanc avance vers le bas (dy positif)
            return False
        step_y = 1

    # Vérifie chemin libre
    y = y1 + step_y
    while y != y2:
        if plateau[y][x1][0] != "":
            return False
        y += step_y

    # Vérifie capture
    piece_cible, joueur_cible, _ = plateau[y2][x2]
    if joueur_cible == joueur:
        return False

    # Déplacement
    plateau[y2][x2] = plateau[y1][x1]
    plateau[y1][x1] = ("", None, False)

    return True

def deplacercavalier(x1, y1, x2, y2, joueur):
    dx = x2 - x1
    dy = y2 - y1

    # Déplacement spécifique au cavalier de shogi
    if joueur == "Gote":
        # Gote avance vers le haut (dy = -2)
        if dy != -2 or abs(dx) != 1:
            return False
    else:  # blanc
        # Blanc avance vers le bas (dy = +2)
        if dy != 2 or abs(dx) != 1:
            return False

    # Vérifie capture
    piece_cible, joueur_cible, _ = plateau[y2][x2]
    if joueur_cible == joueur:
        return False

    # Déplacement (le cavalier saute, pas besoin de vérifier le chemin)
    plateau[y2][x2] = plateau[y1][x1]
    plateau[y1][x1] = ("", None, False)

    return True

def deplacerGeneralargent(x1, y1, x2, y2, joueur):  
    dx = x2 - x1
    dy = y2 - y1

    # Le général d'argent se déplace d'une seule case
    if abs(dx) > 1 or abs(dy) > 1:
        return False

    # Interdiction de rester sur place
    if dx == 0 and dy == 0:
        return False

    if joueur == "Gote":
        # Gote avance vers le haut (dy négatif)
        mouvements_valides = [
            (-1, -1), (0, -1), (1, -1),   # avant + diagonales avant
            (-1, 1), (1, 1)               # diagonales arrière
        ]
    else:
        # Blanc avance vers le bas (dy positif)
        mouvements_valides = [
            (-1, 1), (0, 1), (1, 1),      # avant + diagonales avant
            (-1, -1), (1, -1)             # diagonales arrière
        ]

    if (dx, dy) not in mouvements_valides:
        return False

    # Vérifie capture
    piece_cible, joueur_cible, _ = plateau[y2][x2]
    if joueur_cible == joueur:
        return False

    # Déplacement
    plateau[y2][x2] = plateau[y1][x1]
    plateau[y1][x1] = ("", None, False)

    return True
def deplacerGeneralor(x1, y1, x2, y2, joueur):
    dx = x2 - x1
    dy = y2 - y1

    # Une seule case maximum
    if abs(dx) > 1 or abs(dy) > 1:
        return False

    if dx == 0 and dy == 0:
        return False

    if joueur == "Gote":
        # Gote avance vers le haut (dy négatif)
        mouvements_valides = [
            (-1, -1), (0, -1), (1, -1),  # avant + diagonales avant
            (-1, 0), (1, 0),             # gauche / droite
            (0, 1)                      # arrière vertical
        ]
    else:
        # Blanc avance vers le bas (dy positif)
        mouvements_valides = [
            (-1, 1), (0, 1), (1, 1),     # avant + diagonales avant
            (-1, 0), (1, 0),             # gauche / droite
            (0, -1)                     # arrière vertical
        ]

    if (dx, dy) not in mouvements_valides:
        return False

    # Vérifie capture
    piece_cible, joueur_cible, _ = plateau[y2][x2]
    if joueur_cible == joueur:
        return False

    # Déplacement
    plateau[y2][x2] = plateau[y1][x1]
    plateau[y1][x1] = ("", None, False)

    return True

def deplacerRoi(x1, y1, x2, y2, joueur):
    dx = x2 - x1
    dy = y2 - y1

    # Le roi se déplace d'une seule case maximum
    if abs(dx) > 1 or abs(dy) > 1:
        return False

    # Interdiction de rester sur place
    if dx == 0 and dy == 0:
        return False    

    # Déplacement
    plateau[y2][x2] = plateau[y1][x1]
    plateau[y1][x1] = ("", None, False)

    return True
     