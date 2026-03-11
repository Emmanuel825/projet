import vue
import model

selection = None

root, canvas = vue.creer_fenetre()

def clic(event):
    global selection
    print(event.x)
    if((event.x > vue.PADDING_X and event.x < vue.PADDING_X+vue.LARGEUR)and(event.y > vue.PADDING_Y and event.y < vue.PADDING_Y+vue.HAUTEUR)):
        x = (event.x-vue.PADDING_X) // vue.TAILLE_CASE
        y = (event.y-vue.PADDING_Y) // vue.TAILLE_CASE
        if selection is None:
            piece = model.getPiece(x, y)
            if piece != "":
                selection = (x, y)
                print("Sélection :", piece)
        else:
            x1, y1 = selection
            model.deplacerPiece(x1, y1, x, y)
            selection = None
            vue.rafraichir(canvas)
    elif((event.x > vue.PRISES_HAUT_X and event.x < vue.PADDING_X)and(event.y > vue.PRISES_HAUT_Y and event.y < vue.PRISES_HAUT_Y+200)):
        x = event.x - vue.PRISES_HAUT_X
        y = event.y - vue.PRISES_HAUT_Y
        piece = ((y//(200//vue.PRISES_COLS))*vue.PRISES_COLS)+(x//(200//vue.PRISES_COLS))
        model.getParachutage(piece, "Sente")
        selection = None
    elif((event.x > vue.PRISES_BAS_X and event.x < vue.PRISES_BAS_X+200)and(event.y > vue.PRISES_BAS_Y and event.y < vue.PRISES_BAS_Y+200)):
        x = event.x - vue.PRISES_BAS_X
        y = event.y - vue.PRISES_BAS_Y
        piece = ((y//(200//vue.PRISES_COLS))*vue.PRISES_COLS)+(x//(200//vue.PRISES_COLS))
        print(piece)
        selection = None
    else:
        selection = None

canvas.bind("<Button-1>", clic)

root.mainloop()