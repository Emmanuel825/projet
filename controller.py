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
    else:
        selection = None

canvas.bind("<Button-1>", clic)

root.mainloop()