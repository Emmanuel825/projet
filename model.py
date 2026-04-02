NB_CASES = 9

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
currentPlayer = "Sente"
indexPara = 0
check = []
echec = [False, ""]
mat = [False, ""]
echec_attaquant = None
dernierJoueur = ""
promotion_en_attente = None


def _adversaire(joueur):
    if joueur == "Sente":
        return "Gote"
    return "Sente"


def _find_roi(joueur):
    for y in range(NB_CASES):
        for x in range(NB_CASES):
            if plateau[y][x][0] == "王" and plateau[y][x][1] == joueur:
                return (x, y)
    return None


def _piece_moves(x, y):
    global check
    piece, joueur, _ = plateau[y][x]
    if piece == "":
        return []

    save_check = check
    check = []

    if plateau[y][x][2] == False:
        if piece == "歩":
            checkPion(x, y, joueur)
        elif piece == "香":
            checkLance(x, y, joueur)
        elif piece == "桂":
            checkCavalier(x, y, joueur)
        elif piece == "銀":
            checkGeneralargent(x, y, joueur)

    if piece == "金" or (plateau[y][x][2] == True and piece != "飛" and piece != "角" and piece != "王"):
        checkGeneralor(x, y, joueur)
    elif piece == "王":
        checkRoi(x, y, joueur)
    elif piece == "角":
        checkFou(x, y, joueur)

    if piece == "飛":
        checkTour(x, y, joueur)

    moves = list(check)
    check = save_check
    return moves


def _roi_en_echec(joueur):
    roi = _find_roi(joueur)
    if roi is None:
        return (False, None)

    roi_x, roi_y = roi
    attaquant = _adversaire(joueur)

    for y in range(NB_CASES):
        for x in range(NB_CASES):
            if plateau[y][x][1] == attaquant:
                moves = _piece_moves(x, y)
                if (roi_y, roi_x) in moves:
                    return (True, (y, x))
    return (False, None)


def _a_un_coup_de_sauvetage(joueur):
    for y1 in range(NB_CASES):
        for x1 in range(NB_CASES):
            if plateau[y1][x1][1] != joueur:
                continue

            moves = _piece_moves(x1, y1)
            for y2, x2 in moves:
                source = plateau[y1][x1]
                cible = plateau[y2][x2]

                plateau[y2][x2] = source
                plateau[y1][x1] = ["", None, False]

                en_echec, _ = _roi_en_echec(joueur)

                plateau[y1][x1] = source
                plateau[y2][x2] = cible

                if not en_echec:
                    return True
    return False


def _peut_promouvoir(piece):
    return piece in ["歩", "香", "桂", "銀", "角", "飛"]


def _promotion_obligatoire(piece, joueur, y):
    if piece == "歩" or piece == "香":
        return (joueur == "Sente" and y == NB_CASES - 1) or (joueur == "Gote" and y == 0)
    if piece == "桂":
        return (joueur == "Sente" and y >= NB_CASES - 2) or (joueur == "Gote" and y <= 1)
    return False


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
    global currentPlayer
    global dernierJoueur
    if checkParachutage(piece, x, y, joueur):
        if plateau[y][x][0]=="":
            plateau[y][x]=[piece, joueur, False]
            en_echec_apres, _ = _roi_en_echec(joueur)
            if en_echec_apres:
                plateau[y][x]=["",None,False]
                indexPara=0
                return
            if(joueur == "Gote"):
                for i in range(7):
                    if priseGote[i][0] == piece:
                        priseGote[i][1]-=1
            else:
                for i in range(7):
                    if priseSente[i][0] == piece:
                        priseSente[i][1]-=1
            dernierJoueur = joueur
            currentPlayer = _adversaire(joueur)
            verifEchecMat(currentPlayer)
    indexPara=0
        
def getPiece(x, y):
    global currentPlayer
    global check
    print(currentPlayer)
    if currentPlayer == plateau[y][x][1]:
        if plateau[y][x][2]==False:
            if(plateau[y][x][0]=="歩"):
                checkPion(x, y, plateau[y][x][1])
                # reussiteDep = checkFou(x, y, x2, y2, plateau[y][x][1])

            if(plateau[y][x][0]=="香"):
                
                checkLance(x, y, plateau[y][x][1])
                # if (y2,x2) in check:
                #     plateau[y2][x2]=plateau[y][x]
                #     plateau[y][x]=["",None,False]
                #     reussiteDep=True

            if(plateau[y][x][0]=="桂"):
                
                checkCavalier(x, y, plateau[y][x][1])
                # if (y2,x2) in check:
                #     plateau[y2][x2]=plateau[y][x]
                #     plateau[y][x]=["",None,False]
                #     reussiteDep=True

            if(plateau[y][x][0]=="銀"):
                
                checkGeneralargent(x, y, plateau[y][x][1])
                # if (y2,x2) in check:
                #     plateau[y2][x2]=plateau[y][x]
                #     plateau[y][x]=["",None,False]
                #     reussiteDep=True


        if(plateau[y][x][0]=="金" or (plateau[y][x][2] == True and (plateau[y][x]!="飛" and plateau[y][x][0]!="角" and plateau[y][x]!="王"))):
            
            checkGeneralor(x, y, plateau[y][x][1])
            # if (y2,x2) in check:
            #     plateau[y2][x2]=plateau[y][x]
            #     plateau[y][x]=["",None,False]
            #     reussiteDep=True
            #     reussiteDep = True

        elif(plateau[y][x][0]=="王"):
            check = []
            checkRoi(x, y, plateau[y][x][1])
        
        elif(plateau[y][x][0]=="角"):
            
            checkFou(x, y, plateau[y][x][1])
            # if (y2,x2) in check:
            #     plateau[y2][x2]=plateau[y][x]
            #     plateau[y][x]=["",None,False]
            #     reussiteDep=True

        if(plateau[y][x][0]=="飛"):
            
            checkTour(x, y, plateau[y][x][1])
            # if (y2,x2) in check:
            #     plateau[y2][x2]=plateau[y][x]
            #     plateau[y][x]=["",None,False]
            #     reussiteDep=True
        return (plateau[y][x][0], check)
    return False

def deplacerPiece(x1, y1, x2, y2):
    reussiteDep = False
    global check
    global currentPlayer
    global dernierJoueur
    global promotion_en_attente
    prise = plateau[y2][x2][0]
    promotion_en_attente = None
    if(plateau[y1][x1][1] != plateau[y2][x2][1]):

        if (y2,x2) in check:
            joueur = plateau[y1][x1][1]
            source = plateau[y1][x1]
            cible = plateau[y2][x2]

            plateau[y2][x2]=source
            plateau[y1][x1]=["",None,False]

            en_echec_apres, _ = _roi_en_echec(joueur)
            if en_echec_apres:
                plateau[y1][x1]=source
                plateau[y2][x2]=cible
            else:
                reussiteDep=True

        if reussiteDep == True :
            if ((plateau[y2][x2][1] == "Gote")):
                piece_deplacee = plateau[y2][x2][0]
                if y2 <=2 and _peut_promouvoir(piece_deplacee) and not plateau[y2][x2][2]:
                    if _promotion_obligatoire(piece_deplacee, "Gote", y2):
                        plateau[y2][x2][2] = True
                    else:
                        promotion_en_attente = (x2, y2)
                if prise != "":
                    for piece in priseGote:
                        if piece[0]==prise:
                            piece[1]+=1
            elif (plateau[y2][x2][1] == "Sente"):
                piece_deplacee = plateau[y2][x2][0]
                if y2 >=6 and _peut_promouvoir(piece_deplacee) and not plateau[y2][x2][2]:
                    if _promotion_obligatoire(piece_deplacee, "Sente", y2):
                        plateau[y2][x2][2] = True
                    else:
                        promotion_en_attente = (x2, y2)
                if prise != "":
                    for piece in priseSente:
                        if piece[0] == prise:
                            piece[1]+=1
    if reussiteDep:
        dernierJoueur = plateau[y2][x2][1]
        currentPlayer = _adversaire(currentPlayer)
        verifEchecMat(currentPlayer)
    check = []


def appliquerPromotion(promouvoir):
    global promotion_en_attente
    if promotion_en_attente is None:
        return

    x, y = promotion_en_attente
    if promouvoir:
        plateau[y][x][2] = True

    promotion_en_attente = None
    verifEchecMat(currentPlayer)
        
def checkPion(x, y, joueur):
    global check
    if((joueur == "Sente" and plateau[y+1][x][1]!="Sente")):
        check.append((y+1, x))                       
        return True
    elif(joueur == "Gote" and plateau[y-1][x][1]!="Gote"):
        check.append((y-1, x))
        return True
    return False

def checkFou(x, y, joueur): 
    global check

    step = 1 
    x = x
    y = y
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

    if plateau[y][x][2]:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if((x+i >= 0)and(x+i < NB_CASES)and(y+j>=0)and(y+j<NB_CASES)and(plateau[y+j][x+i][1]!=joueur)):
                    if (y+j, x+i) not in check:
                        check.append((y+j, x+i))
    return True

def checkTour(x, y, joueur):
    global check
    i = y-1
    while(i>=0 and plateau[i][x][0]==""):
        check.append((i, x))
        i-=1
    if(i>=0)and((joueur == "Sente" and plateau[i][x][1]=="Gote")or(joueur == "Gote" and plateau[i][x][1] == "Sente")):
        check.append((i, x))
    i = y+1
    while(i<NB_CASES and plateau[i][x][0]==""):
        check.append((i, x))
        i+=1
    if(i<NB_CASES)and((joueur == "Sente" and plateau[i][x][1]=="Gote")or(joueur == "Gote" and plateau[i][x][1] == "Sente")):
        check.append((i, x))

    i = x-1
    while(i>=0 and plateau[y][i][0]==""):
        check.append((y, i))
        i-=1
    if(i>=0)and((joueur == "Sente" and plateau[y][i][1]=="Gote")or(joueur == "Gote" and plateau[y][i][1] == "Sente")):
        check.append((y, i))    
    i = x+1
    while(i<NB_CASES and plateau[y][i][0]==""):
        check.append((y, i))
        i+=1
    if(i<NB_CASES)and((joueur == "Sente" and plateau[y][i][1]=="Gote")or(joueur == "Gote" and plateau[y][i][1] == "Sente")):
        check.append((y, i))    
    
    if plateau[y][x][2]:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if((x+i >= 0)and(x+i < NB_CASES)and(y+j>=0)and(y+j<NB_CASES)and(plateau[y+j][x+i][1]!=joueur)):
                    if (y+j, x+i) not in check:
                        check.append((y+j, x+i))
    return True
    
def  checkLance(x, y, joueur):  
    global check
    if joueur == "Sente":
        i = y+1
        while(i<NB_CASES and plateau[i][x][0]==""):
            check.append((i, x))
            i+=1
        if(i<NB_CASES)and(plateau[i][x][1]=="Gote"):
            check.append((i, x))
    else:
        i = y-1
        while(i>=0 and plateau[i][x][0]==""):
            check.append((i, x))
            i-=1
        if(i>=0)and(joueur == "Gote" and plateau[i][x][1] == "Sente"):
            check.append((i, x))
    print(check)
    return True

def checkCavalier(x, y, joueur):
    global check
    if joueur == "Sente" and y+2 < NB_CASES:
        if x-1 >= 0 and plateau[y+2][x-1][1]!=joueur:
            check.append((y+2, x-1))
        if x+1 < NB_CASES and plateau[y+2][x+1][1]!=joueur:
            check.append((y+2, x+1))
    elif joueur == "Gote":
        if  y-2 >= 0:
            if x-1 >= 0 and plateau[y-2][x-1][1]!=joueur:
                check.append((y-2, x-1))
            if x+1 < NB_CASES and plateau[y-2][x+1][1]!=joueur:
                check.append((y-2, x+1))

    return True

def checkGeneralargent(x, y, joueur):  
    global check
    if joueur == "Gote":
        if y+1 < NB_CASES:
            if x-1 >= 0 and plateau[y+1][x-1][1]!=joueur:
                check.append((y+1, x-1))
            if x+1 < NB_CASES and plateau[y+1][x+1][1]!=joueur:
                check.append((y+1, x+1)) 
        if y-1 >= 0:
            for i in range(-1, 2):
                if x+i >= 0 and x+i < NB_CASES and plateau[y-1][x+i][1]!=joueur:
                    check.append((y-1, x+i))
    elif joueur == "Sente":
        if y-1 < NB_CASES:
            if x-1 >= 0 and plateau[y-1][x-1][1]!=joueur:
                check.append((y-1, x-1))
            if x+1 < NB_CASES and plateau[y-1][x+1][1]!=joueur:
                check.append((y-1, x+1)) 
        if y+1 >= 0:
            for i in range(-1, 2):
                if x+i >= 0 and x+i < NB_CASES and plateau[y+1][x+i][1]!=joueur:
                    check.append((y+1, x+i))                       

    return True
def checkGeneralor(x, y, joueur):
    if joueur == "Gote":
        if y+1 < NB_CASES and plateau[y+1][x][1]!=joueur:
            check.append((y+1, x))
        for i in range(2):
            for j in range(-1, 2):
                if x+j >= 0 and x+j < NB_CASES and y-i >=0 and y-i < NB_CASES and plateau[y-i][x+j][1]!=joueur:
                    check.append((y-i, x+j))
    if joueur == "Sente":
        if y-1 >= 0 and plateau[y-1][x][1]!=joueur:
            check.append((y-1, x))
        for i in range(2):
            for j in range(-1, 2):
                if x+j >= 0 and x+j < NB_CASES and y+i >=0 and y+i < NB_CASES and plateau[y+i][x+j][1]!=joueur:
                    check.append((y+i, x+j))
        
    return True

def checkRoi(x, y, joueur):
    global check
    saveCheck = []
    saveCheck2 = []
    cases_attaquees = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if((x+i >= 0)and(x+i < NB_CASES)and(y+j>=0)and(y+j<NB_CASES)and(plateau[y+j][x+i][1]!=joueur)):
                if (y+j, x+i) not in saveCheck:
                    saveCheck.append((y+j, x+i))
    for i in range(NB_CASES):
        for j in range(NB_CASES):
            if(plateau[i][j][1]!=joueur and plateau[i][j][0]!="" and plateau[i][j][0]!="王"):
                cases_attaquees.extend(_piece_moves(j, i))

    # On filtre les doublons pour des comparaisons stables
    cases_attaquees = list(dict.fromkeys(cases_attaquees))

    for k in saveCheck:
        if k not in cases_attaquees:
            saveCheck2.append(k)
            
    check = saveCheck2
    return True

def reinitialise():
    global plateau
    global priseSente
    global priseGote
    global indexPara
    global check
    global currentPlayer
    global echec
    global mat
    global echec_attaquant
    global dernierJoueur
    global promotion_en_attente

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
    currentPlayer = "Sente"
    echec = [False, ""]
    mat = [False, ""]
    echec_attaquant = None
    dernierJoueur = ""
    promotion_en_attente = None

def verifEchecMat(joueur):
    global echec
    global mat
    global echec_attaquant

    mat[0] = False
    mat[1] = ""

    en_echec, attaquant = _roi_en_echec(joueur)
    echec[0] = en_echec
    echec[1] = joueur if en_echec else ""
    echec_attaquant = attaquant

    if not en_echec:
        return

    if not _a_un_coup_de_sauvetage(joueur):
        mat[0] = True
        mat[1] = joueur