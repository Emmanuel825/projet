import tkinter as tk
import vue
import model

selection = None
parachutage = None

root, canvas = vue.creer_fenetre()

def clic(event):
    global selection
    global parachutage
    if((event.x > vue.PADDING_X and event.x < vue.PADDING_X+vue.LARGEUR)and(event.y > vue.PADDING_Y and event.y < vue.PADDING_Y+vue.HAUTEUR)):
        x = (event.x-vue.PADDING_X) // vue.TAILLE_CASE
        y = (event.y-vue.PADDING_Y) // vue.TAILLE_CASE
        if selection is None:
            if parachutage is None:
                piece, check = model.getPiece(x, y)
                if piece != "":
                    selection = (x, y)
                    vue.rafraichir(canvas, check)
            else:
                model.parachutage(parachutage[1], x, y, parachutage[0])
                selection = None
                parachutage = None
                vue.rafraichir(canvas, [])

        else:
            x1, y1 = selection
            model.deplacerPiece(x1, y1, x, y)
            selection = None
            vue.rafraichir(canvas, [])
    elif((event.x > vue.PRISES_HAUT_X and event.x < vue.PADDING_X)and(event.y > vue.PRISES_HAUT_Y and event.y < vue.PRISES_HAUT_Y+200)):
        x = event.x - vue.PRISES_HAUT_X
        y = event.y - vue.PRISES_HAUT_Y
        piece = ((y//(200//vue.PRISES_COLS))*vue.PRISES_COLS)+(x//(200//vue.PRISES_COLS))
        parachutage=model.getParachutage(piece, "Sente")
        selection = None
    elif((event.x > vue.PRISES_BAS_X and event.x < vue.PRISES_BAS_X+200)and(event.y > vue.PRISES_BAS_Y and event.y < vue.PRISES_BAS_Y+200)):
        x = event.x - vue.PRISES_BAS_X
        y = event.y - vue.PRISES_BAS_Y
        piece = ((y//(200//vue.PRISES_COLS))*vue.PRISES_COLS)+(x//(200//vue.PRISES_COLS))
        parachutage=model.getParachutage(piece, "Gote")
        selection = None
    else:
        selection = None

canvas.bind("<Button-1>", clic)
def reInitialise():
    global root, canvas 
    global selection
    global parachutage
    model.plateau = [
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
    model.priseSente = [["角",0],["飛",0],["金",0],["銀",0],["桂",0],["香",0],["歩",0]]
    model.priseGote = [["角",0],["飛",0],["金",0],["銀",0],["桂",0],["香",0],["歩",0]]
    model.indexPara = 0
    model.check = []
    selection = None
    parachutage = None
    vue.rafraichir(canvas, model.check)

def reCommence():
    reInitialise()

rejouer = tk.Button(root, text="Rejouer", command=reCommence)
rejouer.place(x = 1.2*800, y = 220)

root.mainloop()