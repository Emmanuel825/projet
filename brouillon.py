import tkinter as tk
from PIL import Image,ImageTk
import model 
root = tk.Tk()
""""
bg_fond = Image.open("fond1.webp")
bg_test = bg_fond.resize((1900,1000),Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(bg_test)
back = tk.Label(root, image=bg_image)
back.place(x=0,y=0)

promotion
pion "歩"=> と(tokin = pion d'or) deplacement cercle - diagonales du bas en une case
fou  "角"=> 竜(Gogaku = dragon cheval) cercle + diagonales
tour "飛"=>馬(ryûma = dragon roi) même deplacement+ diagonale en une case
lance "香"=> 香 (kyôsha = )comme un pion d'or
cavalier "桂" =>圭 comme un pion d'or
général d'argent "銀'=> 金(général d'or)même deplacement d'un générale d'or


✅ Si tu veux gérer la promotion (龍王 / Ryūō)

En shogi, quand la tour est promue, elle peut aussi se déplacer d’une case en diagonale (comme un roi).

Tu pourrais ajouter :

piece, joueur_piece, promue = plateau[y1][x1]

# Si la tour est promue → peut aussi faire 1 case diagonale
if promue:
    if abs(dx) == 1 and abs(dy) == 1:
        piece_cible, joueur_cible, _ = plateau[y2][x2]
        if joueur_cible != joueur:
            plateau[y2][x2] = plateau[y1][x1]
            plateau[y1][x1] = ("", None, False)
            return True
"""


