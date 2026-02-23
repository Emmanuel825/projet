NB_CASES = 9

plateau = [
    [("香","haut"),("桂","haut"),("銀","haut"),("金","haut"),("王","haut"),("金","haut"),("銀","haut"),("桂","haut"),("香","haut")],
    [("",None),("飛","haut"),("",None),("",None),("",None),("",None),("",None),("角","haut"),("",None)],
    [("歩","haut"),("歩","haut"),("歩","haut"),("歩","haut"),("歩","haut"),("歩","haut"),("歩","haut"),("歩","haut"),("歩","haut")],
    [("",None)]*9,
    [("",None)]*9,
    [("",None)]*9,
    [("歩","bas"),("歩","bas"),("歩","bas"),("歩","bas"),("歩","bas"),("歩","bas"),("歩","bas"),("歩","bas"),("歩","bas")],
    [("",None),("角","bas"),("",None),("",None),("",None),("",None),("",None),("飛","bas"),("",None)],
    [("香","bas"),("桂","bas"),("銀","bas"),("金","bas"),("玉","bas"),("金","bas"),("銀","bas"),("桂","bas"),("香","bas")],
]

def getPiece(x, y):
    return plateau[y][x][0]

def deplacerPiece(x1, y1, x2, y2):
    if(x1 != x2 and y1 != y2):
        plateau[y2][x2] = plateau[y1][x1]
        plateau[y1][x1] = ("", None)