NB_CASES = 9

plateau = [
    [("香","Sente"),("桂","Sente"),("銀","Sente"),("金","Sente"),("王","Sente"),("金","Sente"),("銀","Sente"),("桂","Sente"),("香","Sente")],
    [("",None),("飛","Sente"),("",None),("",None),("",None),("",None),("",None),("角","Sente"),("",None)],
    [("歩","Sente"),("歩","Sente"),("歩","Sente"),("歩","Sente"),("歩","Sente"),("歩","Sente"),("歩","Sente"),("歩","Sente"),("歩","Sente")],
    [("",None)]*9,
    [("",None)]*9,
    [("",None)]*9,
    [("歩","Gote"),("歩","Gote"),("歩","Gote"),("歩","Gote"),("歩","Gote"),("歩","Gote"),("歩","Gote"),("歩","Gote"),("歩","Gote")],
    [("",None),("角","Gote"),("",None),("",None),("",None),("",None),("",None),("飛","Gote"),("",None)],
    [("香","Gote"),("桂","Gote"),("銀","Gote"),("金","Gote"),("玉","Gote"),("金","Gote"),("銀","Gote"),("桂","Gote"),("香","Gote")],
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
                        plateau[y1][x1] = ("",None)
        
             