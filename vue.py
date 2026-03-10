import tkinter as tk
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
        piece_img_promu = sheet.crop((x1, y2, x2, y2*2))
        piece_img_promu = piece_img.resize((TAILLE_CASE, TAILLE_CASE), Image.LANCZOS)

        photo = ImageTk.PhotoImage(piece_img)
        photo_promu = ImageTk.PhotoImage(piece_img_promu)
        pieces_images[noms[col]] = photo
        pieces_images_promu[noms[col]] = photo_promu

        piece_flip = piece_img.rotate(180)
        piece_promu_flip = piece_img_promu.rotate(180)
        photo_flip = ImageTk.PhotoImage(piece_flip)
        photo_promu_flip = ImageTk.PhotoImage(piece_promu_flip)
        pieces_images_flip[noms[col]] = photo_flip
        pieces_images_flip[noms[col]] = photo_promu_flip


    pieces_images["玉"] = pieces_images["王"]
    pieces_images_flip["玉"] = pieces_images_flip["王"]


def dessiner_plateau(canvas):
    for i in range(NB_CASES + 1):
        canvas.create_line(PADDING_X, (i * TAILLE_CASE)+PADDING_Y, PADDING_X+LARGEUR, (i * TAILLE_CASE)+PADDING_Y, width=2)
        canvas.create_line((i * TAILLE_CASE)+PADDING_X, PADDING_Y, (i * TAILLE_CASE)+PADDING_X, PADDING_Y+HAUTEUR, width=2)
    image2 = Image.open("koi.png")
    image2 = image2.resize((200, 200), Image.LANCZOS)
    bg_image2 = ImageTk.PhotoImage(image2)

    canvas.bg_image2 = bg_image2
    
    canvas.create_image(PADDING_X-200,PADDING_Y, image=bg_image2, anchor="nw")
    image3 = Image.open("tree.png")
    image3 = image3.resize((200, 200), Image.LANCZOS)
    bg_image3 = ImageTk.PhotoImage(image3)

    canvas.bg_image3 = bg_image3
    
    canvas.create_image(PADDING_X*2+160,PADDING_Y*2+330, image=bg_image3, anchor="nw")
    


def dessiner_pieces(canvas):
    canvas.images = []
    
    for y in range(NB_CASES):
        for x in range(NB_CASES):
            #récupère les pièces et les joueurs auxquels elles appartiennent
            piece, joueur, promu = model.plateau[y][x]
            if piece != "" and piece in pieces_images:

                cx = (x * TAILLE_CASE)+PADDING_X
                cy = (y * TAILLE_CASE)+PADDING_Y

                if joueur == "Sente":
                    img = pieces_images_flip[piece]
                else:
                    img = pieces_images[piece]
                    
                canvas.create_image(cx, cy, image=img, anchor="nw")
                canvas.images.append(img)
        
#mettre l'option de promotion ainsi que l'option de non promotion
#promotion = ["玉","竜","馬","全","圭","杏","と"]
def rafraichir(canvas):
    canvas.delete("all")
    image0 = Image.open("fond1.webp")
    image0 = image0.resize((JEU_LARGEUR, 1000), Image.LANCZOS)
    bg_image0 = ImageTk.PhotoImage(image0)

    canvas.bg_image0 = bg_image0
    
    canvas.create_image(0,0, image=bg_image0, anchor="nw")
    canvas.create_image(PADDING_X, PADDING_Y, image=canvas.bg_image,anchor="nw")
    dessiner_plateau(canvas)
    dessiner_pieces(canvas)