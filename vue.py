import tkinter as tk
from PIL import Image, ImageTk
import model

TAILLE_CASE = 60
NB_CASES = 9
LARGEUR = TAILLE_CASE * NB_CASES
HAUTEUR = TAILLE_CASE * NB_CASES

pieces_images = {}
pieces_images_flip = {}

def creer_fenetre():
    root = tk.Tk()
    root.title("Shogi")

    canvas = tk.Canvas(root, width=LARGEUR, height=HAUTEUR)
    canvas.pack()

    # Fond
    image = Image.open("plateau.png")
    image = image.resize((LARGEUR, HAUTEUR), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)

    canvas.bg_image = bg_image
    canvas.create_image(0, 0, image=bg_image, anchor="nw")

    charger_images()

    dessiner_plateau(canvas)
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

        photo = ImageTk.PhotoImage(piece_img)
        pieces_images[noms[col]] = photo

        piece_flip = piece_img.rotate(180)
        photo_flip = ImageTk.PhotoImage(piece_flip)
        pieces_images_flip[noms[col]] = photo_flip

    pieces_images["玉"] = pieces_images["王"]
    pieces_images_flip["玉"] = pieces_images_flip["王"]


def dessiner_plateau(canvas):
    for i in range(NB_CASES + 1):
        canvas.create_line(0, i * TAILLE_CASE, LARGEUR, i * TAILLE_CASE, width=2)
        canvas.create_line(i * TAILLE_CASE, 0, i * TAILLE_CASE, HAUTEUR, width=2)


def dessiner_pieces(canvas):
    canvas.images = []

    for y in range(NB_CASES):
        for x in range(NB_CASES):

            piece, joueur = model.plateau[y][x]

            if piece != "" and piece in pieces_images:

                cx = x * TAILLE_CASE
                cy = y * TAILLE_CASE

                if joueur == "haut":
                    img = pieces_images_flip[piece]
                else:
                    img = pieces_images[piece]

                canvas.create_image(cx, cy, image=img, anchor="nw")
                canvas.images.append(img)


def rafraichir(canvas):
    canvas.delete("all")
    canvas.create_image(0, 0, image=canvas.bg_image, anchor="nw")
    dessiner_plateau(canvas)
    dessiner_pieces(canvas)