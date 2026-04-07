import tkinter as tk
import vue
import model
import pygame
selection = None
parachutage = None

root, canvas, bouton_pause, bouton_play = vue.creer_fenetre()

def clic(event):
    global selection
    global parachutage

    # Partie terminée: on bloque toute interaction de jeu.
    if model.mat[0]:
        return

    if((event.x > vue.PADDING_X and event.x < vue.PADDING_X+vue.LARGEUR)and(event.y > vue.PADDING_Y and event.y < vue.PADDING_Y+vue.HAUTEUR)):
        x = (event.x-vue.PADDING_X) // vue.TAILLE_CASE
        y = (event.y-vue.PADDING_Y) // vue.TAILLE_CASE
        if selection is None:
            if parachutage is None:
                get = model.getPiece(x, y)
                if get:
                    piece, check = get
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
            if model.promotion_en_attente is not None:
                px, py = model.promotion_en_attente
                piece = model.plateau[py][px][0]
                joueur = model.plateau[py][px][1]
                promouvoir = vue.demander_promotion(piece, joueur)
                model.appliquerPromotion(promouvoir)
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


def reCommence():
    global root, canvas 
    global selection
    global parachutage
    selection = None
    parachutage = None
    model.reinitialise()
    vue.rafraichir(canvas, model.check)

rejouer = tk.Button(root, text="Rejouer", command=reCommence)
rejouer.place(x = 1.2*800, y = 220)

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def fermer_jeu() :
    pygame.mixer.music.stop()
    pygame.quit()
    root.destroy()

def changer_musique():
    vue.musique()

    
bouton_pause.config(command=pause_music)
bouton_pause.place(x=vue.PADDING_X+vue.LARGEUR,y=vue.PADDING_Y)
bouton_play.config(command=resume_music)
bouton_play.place(x=vue.PADDING_X+vue.LARGEUR,y=vue.PADDING_Y+30)
bouton_musique = tk.Button(root, text="Changer musique", command=changer_musique)
bouton_musique.place(x=vue.PADDING_X+vue.LARGEUR,y=vue.PADDING_Y+60)

def changer_volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)

slidervolume = tk.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",
    label="Volume",
    command=changer_volume
)
slidervolume.set(25)
slidervolume.place(x=vue.PADDING_X+vue.LARGEUR,y=vue.PADDING_Y+90)

root.mainloop()