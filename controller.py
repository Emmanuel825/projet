import vue
import model

selection = None

root, canvas = vue.creer_fenetre()

def clic(event):
    global selection
    print(event.x)
    x = event.x // vue.TAILLE_CASE
    y = event.y // vue.TAILLE_CASE

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

canvas.bind("<Button-1>", clic)

root.mainloop()