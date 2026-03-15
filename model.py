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
check = []


def checkParachutage(piece, x, y, joueur):
    if piece == '香' or piece == "歩":
        if (joueur == "Sente" and (y+1 >= NB_CASES or plateau[y+1][x][1]=="Sente"))or(joueur=="Gote"and(y-1 < 0 or plateau[y-1][x][1]=="Gote")):
            return False
        elif piece == "歩":
                for i in range(NB_CASES):
                    if ((joueur == "Sente" and plateau[i][x]==["歩", "Sente", False]) or (joueur == "Gote" and plateau[i][x]==["歩", "Gote", False])) and(i!=y):
                        return False
    elif piece == '桂':
        if (joueur == "Sente" and y+2 >= NB_CASES)or(joueur=="Gote"and y-2 < 0):
            return False    
    return True

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
    if checkParachutage(piece, x, y, joueur):
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
        
def getPiece(x1, y1):
    global check
    if plateau[y1][x1][2]==False:
        if(plateau[y1][x1][0]=="歩"):
            check=[]
            checkPion(x1, y1, plateau[y1][x1][1])
            print(check)
            # reussiteDep = checkFou(x1, y1, x2, y2, plateau[y1][x1][1])

        if(plateau[y1][x1][0]=="香"):
            check=[]
            checkLance(x1, y1, plateau[y1][x1][1])
            print(check)
            # if (y2,x2) in check:
            #     plateau[y2][x2]=plateau[y1][x1]
            #     plateau[y1][x1]=["",None,False]
            #     reussiteDep=True

        if(plateau[y1][x1][0]=="桂"):
            check=[]
            checkCavalier(x1, y1, plateau[y1][x1][1])
            print(check)
            # if (y2,x2) in check:
            #     plateau[y2][x2]=plateau[y1][x1]
            #     plateau[y1][x1]=["",None,False]
            #     reussiteDep=True

        if(plateau[y1][x1][0]=="銀"):
            check=[]
            checkGeneralargent(x1, y1, plateau[y1][x1][1])
            print(check)
            # if (y2,x2) in check:
            #     plateau[y2][x2]=plateau[y1][x1]
            #     plateau[y1][x1]=["",None,False]
            #     reussiteDep=True


    if(plateau[y1][x1][0]=="金" or (plateau[y1][x1][2] == True and (plateau[y1][x1]!="飛" and plateau[y1][x1][0]!="角" and plateau[y1][x1]!="王"))):
        check=[]
        checkGeneralor(x1, y1, plateau[y1][x1][1])
        print(check)
        # if (y2,x2) in check:
        #     plateau[y2][x2]=plateau[y1][x1]
        #     plateau[y1][x1]=["",None,False]
        #     reussiteDep=True
        #     reussiteDep = True

    # elif(plateau[y1][x1][0]=="王"):
    #     reussiteDep = checkRoi(x1, y1, x2, y2, plateau[y1][x1][1])
    
    elif(plateau[y1][x1][0]=="角"):
        check=[]
        checkFou(x1, y1, plateau[y1][x1][1])
        print(check)
        # if (y2,x2) in check:
        #     plateau[y2][x2]=plateau[y1][x1]
        #     plateau[y1][x1]=["",None,False]
        #     reussiteDep=True

    if(plateau[y1][x1][0]=="飛"):
        check=[]
        checkTour(x1, y1, plateau[y1][x1][1])
        print(check)
        # if (y2,x2) in check:
        #     plateau[y2][x2]=plateau[y1][x1]
        #     plateau[y1][x1]=["",None,False]
        #     reussiteDep=True
    print("check ",check)
    return (plateau[y1][x1][0], check)

def deplacerPiece(x1, y1, x2, y2):
    reussiteDep = False
    global check
    prise = plateau[y2][x2][0]
    if(plateau[y1][x1][1] != plateau[y2][x2][1]):

        if (y2,x2) in check:
            plateau[y2][x2]=plateau[y1][x1]
            plateau[y1][x1]=["",None,False]
            reussiteDep=True

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
        
def checkPion(x1, y1, joueur):
    global check
    if((joueur == "Sente" and plateau[y1+1][x1][1]!="Sente")):
        check.append((y1+1, x1))                       
        return True
    elif(joueur == "Gote" and plateau[y1-1][x1][1]!="Gote"):
        check.append((y1-1, x1))
        return True
    return False

def checkFou(x1, y1, joueur): 
    global check

    step = 1 
    x = x1
    y = y1
    # Vérifie chemin libre
    while ((x+step < NB_CASES and y+step < NB_CASES)and(plateau[y+step][x+step][0]=="")):
        check.append((y+step,x+step))
        step+=1
    if((x+step < NB_CASES and y+step < NB_CASES)and((plateau[y+step][x+step][1] == "Sente" and joueur == "Gote")or(plateau[y+step][x+step][1] == "Gote" and joueur == "Sente"))):
        check.append((y+step,x+step))
    step = 1
    while ((x-step >= 0 and y-step >= 0)and(plateau[y-step][x-step][0]=="")):
        check.append((y-step,x-step))
        step+=1
    if((x-step >=0 and y-step >= 0)and((plateau[y-step][x-step][1] == "Sente" and joueur == "Gote")or(plateau[y-step][x-step][1] == "Gote" and joueur == "Sente"))):
        check.append((y-step,x-step))
    step = 1
    while ((x-step >= 0 and y+step < NB_CASES)and(plateau[y+step][x-step][0]=="")):
        check.append((y+step,x-step))
        step+=1
    if((x-step >=0  and y+step <NB_CASES)and((plateau[y+step][x-step][1] == "Sente" and joueur == "Gote")or(plateau[y+step][x-step][1] == "Gote" and joueur == "Sente"))):
        check.append((y+step,x-step))
    step = 1
    while ((x+step < NB_CASES and y-step >= 0)and(plateau[y-step][x+step][0]=="")):
        check.append((y-step,x+step))
        step+=1
    if((x+step < NB_CASES and y-step >= 0)and((plateau[y-step][x+step][1] == "Sente" and joueur == "Gote")or(plateau[y-step][x+step][1] == "Gote" and joueur == "Sente"))):
        check.append((y-step,x+step))

    if plateau[y1][x1][2]:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if((x1+i >= 0)and(x1+i < NB_CASES)and(y1+j>=0)and(y1+j<NB_CASES)and(plateau[y1+j][x1+i][1]!=joueur)):
                    if (y1+j, x1+i) not in check:
                        check.append((y1+j, x1+i))
    return True

def checkTour(x1, y1, joueur):
    global check
    i = y1-1
    while(i>=0 and plateau[i][x1][0]==""):
        check.append((i, x1))
        i-=1
    if(i>=0)and((joueur == "Sente" and plateau[i][x1][1]=="Gote")or(joueur == "Gote" and plateau[i][x1][1] == "Sente")):
        check.append((i, x1))
    i = y1+1
    while(i<NB_CASES and plateau[i][x1][0]==""):
        check.append((i, x1))
        i+=1
    if(i<NB_CASES)and((joueur == "Sente" and plateau[i][x1][1]=="Gote")or(joueur == "Gote" and plateau[i][x1][1] == "Sente")):
        check.append((i, x1))

    i = x1-1
    while(i>=0 and plateau[y1][i][0]==""):
        check.append((y1, i))
        i-=1
    if(i>=0)and((joueur == "Sente" and plateau[y1][i][1]=="Gote")or(joueur == "Gote" and plateau[y1][i][1] == "Sente")):
        check.append((y1, i))    
    i = x1+1
    while(i<NB_CASES and plateau[y1][i][0]==""):
        check.append((y1, i))
        i+=1
    if(i<NB_CASES)and((joueur == "Sente" and plateau[y1][i][1]=="Gote")or(joueur == "Gote" and plateau[y1][i][1] == "Sente")):
        check.append((y1, i))    
    
    if plateau[y1][x1][2]:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if((x1+i >= 0)and(x1+i < NB_CASES)and(y1+j>=0)and(y1+j<NB_CASES)and(plateau[y1+j][x1+i][1]!=joueur)):
                    if (y1+j, x1+i) not in check:
                        check.append((y1+j, x1+i))
        
    print(check)
    return True
    
def  checkLance(x1, y1, joueur):  
    global check
    i = y1+1
    while(i<NB_CASES and plateau[i][x1][0]==""):
        check.append((i, x1))
        i+=1
    if(i<NB_CASES)and((joueur == "Sente" and plateau[i][x1][1]=="Gote")or(joueur == "Gote" and plateau[i][x1][1] == "Sente")):
        check.append((i, x1))
    return True

def checkCavalier(x1, y1, joueur):
    global check
    if joueur == "Sente" and y1+2 < NB_CASES:
        if x1-1 >= 0 and plateau[y1+2][x1-1][1]!=joueur:
            check.append((y1+2, x1-1))
        if x1+1 < NB_CASES and plateau[y1+2][x1+1][1]!=joueur:
            check.append((y1+2, x1+1))
    elif joueur == "Gote":
        if  y1-2 >= 0:
            if x1-1 >= 0 and plateau[y1-2][x1-1][1]!=joueur:
                check.append((y1-2, x1-1))
            if x1+1 < NB_CASES and plateau[y1-2][x1+1][1]!=joueur:
                check.append((y1-2, x1+1))

    return True

def checkGeneralargent(x1, y1, joueur):  
    global check
    if joueur == "Gote":
        if y1+1 < NB_CASES:
            if x1-1 >= 0 and plateau[y1+1][x1-1][1]!=joueur:
                check.append((y1+1, x1-1))
            if x1+1 < NB_CASES and plateau[y1+1][x1+1][1]!=joueur:
                check.append((y1+1, x1+1)) 
        if y1-1 >= 0:
            for i in range(-1, 2):
                if x1+i >= 0 and x1+i < NB_CASES and plateau[y1-1][x1+i][1]!=joueur:
                    check.append((y1-1, x1+i))
    elif joueur == "Sente":
        if y1-1 < NB_CASES:
            if x1-1 >= 0 and plateau[y1-1][x1-1][1]!=joueur:
                check.append((y1-1, x1-1))
            if x1+1 < NB_CASES and plateau[y1-1][x1+1][1]!=joueur:
                check.append((y1-1, x1+1)) 
        if y1+1 >= 0:
            for i in range(-1, 2):
                if x1+i >= 0 and x1+i < NB_CASES and plateau[y1+1][x1+i][1]!=joueur:
                    check.append((y1+1, x1+i))                       

    return True
def checkGeneralor(x1, y1, joueur):
    # dx = x2 - x1
    # dy = y2 - y1

    # # Une seule case maximum
    # if abs(dx) > 1 or abs(dy) > 1:
    #     return False

    # if dx == 0 and dy == 0:
    #     return False

    # if joueur == "Gote":
    #     # Gote avance vers le haut (dy négatif)
    #     mouvements_valides = [
    #         (-1, -1), (0, -1), (1, -1),  # avant + diagonales avant
    #         (-1, 0), (1, 0),             # gauche / droite
    #         (0, 1)                      # arrière vertical
    #     ]
    # else:
    #     # Blanc avance vers le bas (dy positif)
    #     mouvements_valides = [
    #         (-1, 1), (0, 1), (1, 1),     # avant + diagonales avant
    #         (-1, 0), (1, 0),             # gauche / droite
    #         (0, -1)                     # arrière vertical
    #     ]

    # if (dx, dy) not in mouvements_valides:
    #     return False

    # # Vérifie capture
    # piece_cible, joueur_cible, _ = plateau[y2][x2]
    # if joueur_cible == joueur:
    #     return False

    # # Déplacement
    # plateau[y2][x2] = plateau[y1][x1]
    # plateau[y1][x1] = ("", None, False)
    print("test or")
    if joueur == "Gote":
        if y1+1 < NB_CASES and plateau[y1+1][x1][1]!=joueur:
            check.append((y1+1, x1))
        for i in range(2):
            for j in range(-1, 2):
                if x1+j >= 0 and x1+j < NB_CASES and y1-i >=0 and y1-i < NB_CASES and plateau[y1-i][x1+j][1]!=joueur:
                    check.append((y1-i, x1+j))
    if joueur == "Sente":
        if y1-1 >= 0 and plateau[y1-1][x1][1]!=joueur:
            check.append((y1-1, x1))
        for i in range(2):
            for j in range(-1, 2):
                if x1+j >= 0 and x1+j < NB_CASES and y1+i >=0 and y1+i < NB_CASES and plateau[y1+i][x1+j][1]!=joueur:
                    check.append((y1+i, x1+j))
        
    return True

def checkRoi(x1, y1, x2, y2, joueur):
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
     