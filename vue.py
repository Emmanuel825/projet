import tkinter as tk
from PIL import Image, ImageTk

# ----------------------------
# Configuration
# ----------------------------
NB_CASES = 9
TAILLE_CASE = 60
COULEUR_FOND = "#d8c8a8"

LARGEUR_PLATEAU = NB_CASES * TAILLE_CASE
HAUTEUR_PLATEAU = NB_CASES * TAILLE_CASE

LARGEUR_FENETRE = 1400
HAUTEUR_FENETRE = 1000

# ----------------------------
# Calcul centrage automatique
# ----------------------------
X_PLATEAU = (LARGEUR_FENETRE - LARGEUR_PLATEAU) // 2
Y_PLATEAU = (HAUTEUR_FENETRE - HAUTEUR_PLATEAU) // 2

# ----------------------------
# Fenêtre
# ----------------------------
root = tk.Tk()
root.title("Plateau Shogi")

canvas = tk.Canvas(
    root,
    width=LARGEUR_FENETRE,
    height=HAUTEUR_FENETRE,
    bg=COULEUR_FOND,
    highlightthickness=0
)
canvas.pack()

# ----------------------------
# Image redimensionnée exactement à la taille du plateau
# ----------------------------
image_originale = Image.open("plateau.png")

image_redimensionnee = image_originale.resize(
    (LARGEUR_PLATEAU+60, HAUTEUR_PLATEAU+60),
    Image.Resampling.LANCZOS
)

texture = ImageTk.PhotoImage(image_redimensionnee)

canvas.create_image(X_PLATEAU-30, Y_PLATEAU-30, anchor="nw", image=texture)

# ----------------------------
# Grille
# ----------------------------
for i in range(NB_CASES + 1):
    # Lignes verticales
    x = X_PLATEAU + i * TAILLE_CASE
    canvas.create_line(x, Y_PLATEAU, x, Y_PLATEAU + HAUTEUR_PLATEAU, width=2)

    # Lignes horizontales
    y = Y_PLATEAU + i * TAILLE_CASE
    canvas.create_line(X_PLATEAU, y, X_PLATEAU + LARGEUR_PLATEAU, y, width=2)

# ----------------------------
# Index colonnes (9 → 1)
# ----------------------------
for col in range(NB_CASES):
    numero = NB_CASES - col
    x = X_PLATEAU + col * TAILLE_CASE + TAILLE_CASE / 2
    y = Y_PLATEAU - 20

    canvas.create_text(
        x,
        y,
        text=str(numero),
        font=("Arial", 14, "bold")
    )

# ----------------------------
# Index lignes (1 → 9)
# ----------------------------
for row in range(NB_CASES):
    numero = row + 1
    x = X_PLATEAU + LARGEUR_PLATEAU + 20
    y = Y_PLATEAU + row * TAILLE_CASE + TAILLE_CASE / 2

    canvas.create_text(
        x,
        y,
        text=str(numero),
        font=("Arial", 14, "bold")
    )

root.mainloop()
