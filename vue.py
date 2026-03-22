import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import model

TAILLE_CASE = 60
NB_CASES = 9
JEU_HAUTEUR = 1100
JEU_LARGEUR = 1300
LARGEUR = TAILLE_CASE * NB_CASES
HAUTEUR = TAILLE_CASE * NB_CASES
PADDING_X = (JEU_LARGEUR//2)-(LARGEUR//2)
PADDING_Y = (JEU_HAUTEUR//2)-(HAUTEUR)

pieces_images = {}
pieces_images_flip = {}
pieces_images_promu = {}
pieces_images_promu_flip = {}


PRISES_HAUT_X = PADDING_X - 200
PRISES_HAUT_Y = PADDING_Y
# PRISES_BAS_X = (PADDING_X * 2) + 170
PRISES_BAS_X = PADDING_X+LARGEUR
# PRISES_BAS_Y = (PADDING_Y * 2) + 345
PRISES_BAS_Y = PADDING_Y+HAUTEUR-200
PRISES_COLS = 4
PRISES_CASE = 45

def creer_fenetre():
    root = tk.Tk()
    root.title("Shogi")

    canvas = tk.Canvas(root, width=JEU_LARGEUR, height=JEU_HAUTEUR)
    canvas.pack()



    # Fond
    image0 = Image.open("fond1.webp")
    image0 = image0.resize((JEU_LARGEUR, 1000), Image.LANCZOS)
    bg_image0 = ImageTk.PhotoImage(image0)

    canvas.bg_image0 = bg_image0
    
    canvas.create_image(0,0, image=bg_image0, anchor="nw")
    image = Image.open("plateau.png")
    image = image.resize((LARGEUR, HAUTEUR), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)

    canvas.bg_image = bg_image
    
    canvas.create_image(PADDING_X, PADDING_Y, image=bg_image, anchor="nw")

    charger_images()

    dessiner_plateau(canvas, [])
    dessiner_pieces(canvas)

    return root, canvas


def charger_images():
    global pieces_images, pieces_images_flip

    sheet = Image.open("pieces.png")
    largeur_piece = sheet.width // 8
    hauteur_piece = sheet.height // 4

    noms = ["王","飛","角","金","銀","桂","香","歩"]
    for col in range(8):
        x1 = col * largeur_piece
        y1 = 0
        x2 = x1 + largeur_piece
        y2 = hauteur_piece

        piece_img = sheet.crop((x1, y1, x2, y2))
        piece_img = piece_img.resize((TAILLE_CASE, TAILLE_CASE), Image.LANCZOS)
        piece_img_promu = sheet.crop((x1, y2, x2, y2*2))
        piece_img_promu = piece_img_promu.resize((TAILLE_CASE, TAILLE_CASE), Image.LANCZOS)

        photo = ImageTk.PhotoImage(piece_img)
        photo_promu = ImageTk.PhotoImage(piece_img_promu)
        pieces_images[noms[col]] = photo
        pieces_images_promu[noms[col]] = photo_promu

        piece_flip = piece_img.rotate(180)
        piece_promu_flip = piece_img_promu.rotate(180)
        photo_flip = ImageTk.PhotoImage(piece_flip)
        photo_promu_flip = ImageTk.PhotoImage(piece_promu_flip)
        pieces_images_flip[noms[col]] = photo_flip
        pieces_images_promu_flip[noms[col]] = photo_promu_flip


    pieces_images["玉"] = pieces_images["王"]
    pieces_images_flip["玉"] = pieces_images_flip["王"]


def dessiner_plateau(canvas, check):
    for i in range(NB_CASES + 1):
        canvas.create_line(PADDING_X, (i * TAILLE_CASE)+PADDING_Y, PADDING_X+LARGEUR, (i * TAILLE_CASE)+PADDING_Y, width=2)
        canvas.create_line((i * TAILLE_CASE)+PADDING_X, PADDING_Y, (i * TAILLE_CASE)+PADDING_X, PADDING_Y+HAUTEUR, width=2)
    r = (TAILLE_CASE//2)-5
    for row in range(NB_CASES):
        for col in range(NB_CASES):
            cx = PADDING_X + col * TAILLE_CASE + TAILLE_CASE // 2
            cy = PADDING_Y + row * TAILLE_CASE + TAILLE_CASE // 2
            if (row, col) in check:
                if model.plateau[row][col][0]!="":
                    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill="red", outline="")
                else:
                    canvas.create_oval(cx - r, cy - r, cx + r, cy + r-5, fill="green", outline="")

    if model.echec[0] and model.echec_attaquant is not None:
        att_row, att_col = model.echec_attaquant
        cx = PADDING_X + att_col * TAILLE_CASE + TAILLE_CASE // 2
        cy = PADDING_Y + att_row * TAILLE_CASE + TAILLE_CASE // 2
        canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill="red", outline="")
    image2 = Image.open("koi.png")
    image2 = image2.resize((200, 200), Image.LANCZOS)
    bg_image2 = ImageTk.PhotoImage(image2)

    canvas.bg_image2 = bg_image2
    
    canvas.create_image(PRISES_HAUT_X,PRISES_HAUT_Y, image=bg_image2, anchor="nw")
    image3 = Image.open("tree.png")
    image3 = image3.resize((200, 200), Image.LANCZOS)
    bg_image3 = ImageTk.PhotoImage(image3)

    canvas.bg_image3 = bg_image3
    
    canvas.create_image(PRISES_BAS_X,PRISES_BAS_Y, image=bg_image3, anchor="nw")
    canvas.create_rectangle(PADDING_X, PADDING_Y, PADDING_X+LARGEUR, PADDING_Y+(3*TAILLE_CASE), outline="red")
    canvas.create_rectangle(PADDING_X, PADDING_Y+HAUTEUR-(3*TAILLE_CASE), PADDING_X+LARGEUR, PADDING_Y+HAUTEUR, outline="blue")
    playerColor = ""
    if model.currentPlayer == "Sente":
        playerColor = "red"
    else:
        playerColor = "blue"
    
    canvas.create_text(PRISES_HAUT_X, (PADDING_Y+HAUTEUR)/2, text=model.currentPlayer, fill=playerColor, font=("Arial", 32), anchor="nw")
    if model.mat[0] and model.dernierJoueur != "":
        canvas.create_text(
            PRISES_HAUT_X,
            (PADDING_Y+HAUTEUR)/2 + 45,
            text=model.dernierJoueur,
            fill="black",
            font=("Arial", 24),
            anchor="nw"
        )
        canvas.create_text(
            PRISES_HAUT_X,
            (PADDING_Y+HAUTEUR)/2 + 80,
            text="défaite",
            fill="red",
            font=("Arial", 28, "bold"),
            anchor="nw"
        )
    

def dessiner_pieces(canvas):
    canvas.images = []
    
    for y in range(NB_CASES):
        for x in range(NB_CASES):
            #récupère les pièces et les joueurs auxquels elles appartiennent
            piece, joueur, promu = model.plateau[y][x]
            if piece != "" and piece in pieces_images:

                cx = (x * TAILLE_CASE)+PADDING_X
                cy = (y * TAILLE_CASE)+PADDING_Y

                if joueur == "Sente" :
                    if promu == True:
                        img = pieces_images_promu_flip[piece]
                    else:
                        img = pieces_images_flip[piece]
                else:
                    if promu == True:
                        img = pieces_images_promu[piece]
                    else:
                        img = pieces_images[piece]
                    
                canvas.create_image(cx, cy, image=img, anchor="nw")
                canvas.images.append(img)

    dessiner_prises(canvas)


def dessiner_prises(canvas):
    # Petit plateau du haut: prises du Sente
    dessiner_liste_prises(canvas, model.priseSente, PRISES_HAUT_X, PRISES_HAUT_Y, "Sente")
    # Petit plateau du bas: prises du Gote
    dessiner_liste_prises(canvas, model.priseGote, PRISES_BAS_X, PRISES_BAS_Y, "Gote")


def dessiner_liste_prises(canvas, prises, x0, y0, joueur):
    index = 0
    for piece, quantite in prises:
        if quantite <= 0:
            continue

        col = index % PRISES_COLS
        lig = index // PRISES_COLS
        cx = x0 + (col * PRISES_CASE)
        cy = y0 + (lig * PRISES_CASE)

        if joueur == "Sente":
            img = pieces_images_flip.get(piece)
        else:
            img = pieces_images.get(piece)

        if img is None:
            continue

        canvas.create_image(cx, cy, image=img, anchor="nw")
        canvas.images.append(img)
        index += 1
        
def rafraichir(canvas, check):
    canvas.delete("all")
    image0 = Image.open("fond1.webp")
    image0 = image0.resize((JEU_LARGEUR, 1000), Image.LANCZOS)
    bg_image0 = ImageTk.PhotoImage(image0)

    canvas.bg_image0 = bg_image0
    
    canvas.create_image(0,0, image=bg_image0, anchor="nw")
    canvas.create_image(PADDING_X, PADDING_Y, image=canvas.bg_image,anchor="nw")
    dessiner_plateau(canvas, check)
    dessiner_pieces(canvas)


def demander_promotion(piece, joueur):
    texte_joueur = "Sente" if joueur == "Sente" else "Gote"
    return messagebox.askyesno("Promotion", f"{texte_joueur}: promouvoir la piece {piece} ?")

