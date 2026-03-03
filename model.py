NB_CASES = 9

#ajout du champ "promu" dans les tuples de la liste
plateau = [
    [("香","Sente", False),("桂","Sente", False),("銀","Sente", False),("金","Sente", False),("王","Sente", False),("金","Sente", False),("銀","Sente", False),("桂","Sente", False),("香","Sente", False)],
    [("",None, False),("飛","Sente", False),("",None, False),("",None, False),("",None, False),("",None, False),("",None, False),("角","Sente", False),("",None, False)],
    [("歩","Sente", False),("歩","Sente", False),("歩","Sente", False),("歩","Sente", False),("歩","Sente", False),("歩","Sente", False),("歩","Sente", False),("歩","Sente", False),("歩","Sente", False)],
    [("",None, False)]*9,
    [("",None, False)]*9,
    [("",None, False)]*9,
    [("歩","Gote", False),("歩","Gote", False),("歩","Gote", False),("歩","Gote", False),("歩","Gote", False),("歩","Gote", False),("歩","Gote", False),("歩","Gote", False),("歩","Gote", False)],
    [("",None, False),("角","Gote", False),("",None, False),("",None, False),("",None, False),("",None, False),("",None, False),("飛","Gote", False),("",None, False)],
    [("香","Gote", False),("桂","Gote", False),("銀","Gote", False),("金","Gote", False),("玉","Gote", False),("金","Gote", False),("銀","Gote", False),("桂","Gote", False),("香","Gote", False)],
]

def getPiece(x, y):
    return plateau[y][x][0]

def deplacerPiece(x1, y1, x2, y2):
    print("p : "+plateau[y1][x1][0]+" "+str(y1)+" "+str(x1))
    if(plateau[y1][x1][0]=="歩"):
        deplacerPion(x1, y1, x2, y2, plateau[y1][x1][1])

    if(plateau[y1][x1][0]=="角"):
        deplacerFou(x1, y1, x2, y2, plateau[y1][x1][1])

    if(plateau[y1][x1][0]=="飛"):
        deplacerTour(x1, y1, x2, y2, plateau[y1][x1][1])

    if(plateau[y1][x1][0]=="香"):
        deplacerLance(x1, y1, x2, y2, plateau[y1][x1][1])

    if(plateau[y1][x1][0]=="桂"):
        deplacercavalier(x1, y1, x2, y2, plateau[y1][x1][1])

    if(plateau[y1][x1][0]=="銀"):
        deplacerGeneralargent(x1, y1, x2, y2, plateau[y1][x1][1])

    if(plateau[y1][x1][0]=="金"):
        deplacerGeneralor(x1, y1, x2, y2, plateau[y1][x1][1])

    if(plateau[y1][x1][0]=="玉"):
        deplacerRoi(x1, y1, x2, y2, plateau[y1][x1][1])

def deplacerPion(x1, y1, x2, y2, joueur):
    print(str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2)+" "+joueur)
    print(y2 == y1-1)
    if(x1 == x2):
        if((y2 == y1+1 and joueur == "Sente")or(y2 == y1-1 and joueur == "Gote")):
                        print("test")
                        plateau[y2][x2] = plateau[y1][x1]
                        plateau[y1][x1] = ("",None, False)

def deplacerFou(x1, y1, x2, y2, joueur): 
    dx = x2 - x1
    dy = y2 - y1

    # Vérifie diagonale
    if abs(dx) != abs(dy):
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

    # Vérifie déplacement en ligne droite
    if dx != 0 and dy != 0:
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

    # Vérifie capture alliée
    piece_cible, joueur_cible, _ = plateau[y2][x2]
    if joueur_cible == joueur:
        return False

    # Déplacement
    plateau[y2][x2] = plateau[y1][x1]
    plateau[y1][x1] = ("", None, False)

    return True
     