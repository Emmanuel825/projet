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

def deplacerPion(x1, y1, x2, y2, joueur):
    print(str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2)+" "+joueur)
    print(y2 == y1-1)
    if(x1 == x2):
        if((y2 == y1+1 and joueur == "Sente")or(y2 == y1-1 and joueur == "Gote")):
                        print("test")
                        plateau[y2][x2] = plateau[y1][x1]
                        plateau[y1][x1] = ("",None, False)
        
             