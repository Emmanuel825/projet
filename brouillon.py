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

si desous un exemle de jeu d'échec 
"""
from tkinter import *
root = Tk()
can = Canvas(root, width=2000, height=2000, background='ivory')
can.pack()
echecs = Frame(can, borderwidth=10, padx=100, pady=50)
echecs.pack(side=LEFT)
Colonnes = [-1,1,2,3,4,5,6,7,8,-1]
Lignes = [-1,1,2,3,4,5,6,7,8,-1]
tour_blanc = PhotoImage(file='tour.blanc.png')
tour_noir = PhotoImage(file='tour.noir.png')
cavalier_blanc = PhotoImage(file='cavalier.blanc.png')
cavalier_noir = PhotoImage(file='cavalier.noir.png')
fou_blanc = PhotoImage(file='fou.blanc.png')
fou_noir = PhotoImage(file='fou.noir.png')
roi_blanc = PhotoImage(file='roi.blanc.png')
roi_noir = PhotoImage(file='roi.noir.png')
reine_blanc = PhotoImage(file='reine.blanc.png')
reine_noir = PhotoImage(file='reine.noir.png')
pion_blanc = PhotoImage(file='pion.blanc.png')
pion_noir = PhotoImage(file='pion.noir.png')
color_red = ['red', 'blue']
color2=['black','white']
color1=['white','black']
j=1
i=1
c=1
cases=[]
def tbs(tb) :
	tb.grid(column=1, row=5, sticky='nesw')
while j < 9 :
	while i < 9 : 
		if (j == 1 or j == 8) and (i == 1 or i == 8):
			if i == 1 :
				tb = Button(echecs, image=tour_blanc, text= str(i)+str(j), bg='black', fg='white', relief=FLAT)
				a1=Button(echecs, text= str(i)+str(j), borderwidth=1, height=7, width=14, bg=color1[c], fg=color2[c], relief=SUNKEN, command=tbs(tb))
				a1.grid(column=Colonnes[j], row=Lignes[i])
 
			else :
				Button(echecs, text= str(i)+str(j), borderwidth=1, height=7, width=14, bg=color1[c], fg=color2[c], relief=SUNKEN).grid(column=Colonnes[j], row=Lignes[i])
				Button(echecs, image=tour_noir, bg=color1[c], fg=color2[c], relief=FLAT).grid(column=Colonnes[j], row=Lignes[i])
			c=1-c
			i+=1
		elif (j == 2 or j == 7) and (i == 1 or i == 8):
			if i == 1 :
				Button(echecs, text= str(i)+str(j), borderwidth=1, height=7, width=14, bg=color1[c], fg=color2[c], relief=SUNKEN).grid(column=Colonnes[j], row=Lignes[i])
				Button(echecs, image=cavalier_blanc, bg=color1[c], fg=color2[c], relief=FLAT).grid(column=Colonnes[j], row=Lignes[i])
			else :
				Button(echecs, text= str(i)+str(j), borderwidth=1, height=7, width=14, bg=color1[c], fg=color2[c], relief=SUNKEN).grid(column=Colonnes[j], row=Lignes[i])
				Button(echecs, image=cavalier_noir, bg=color1[c], fg=color2[c], relief=FLAT).grid(column=Colonnes[j], row=Lignes[i])
			c=1-c
			i+=1
		elif (j == 3 or j == 6) and (i == 1 or i == 8):
			if i == 1 :
				Button(echecs, text= str(i)+str(j), borderwidth=1, height=7, width=14, bg=color1[c], fg=color2[c], relief=SUNKEN).grid(column=Colonnes[j], row=Lignes[i])
				Button(echecs, image=fou_blanc, bg=color1[c], fg=color2[c], relief=FLAT).grid(column=Colonnes[j], row=Lignes[i])
			else :
				Button(echecs, text= str(i)+str(j), borderwidth=1, height=7, width=14, bg=color1[c], fg=color2[c], relief=SUNKEN).grid(column=Colonnes[j], row=Lignes[i])
				Button(echecs, image=fou_noir, bg=color1[c], fg=color2[c], relief=FLAT).grid(column=Colonnes[j], row=Lignes[i])
			c=1-c
			i+=1
		elif j == 4 and (i == 1 or i == 8):
			if i == 1 :
				Button(echecs, text= str(i)+str(j), borderwidth=1, height=7, width=14, bg=color1[c], fg=color2[c], relief=SUNKEN).grid(column=Colonnes[j], row=Lignes[i])
				Button(echecs, image=roi_blanc, bg=color1[c], fg=color2[c], relief=FLAT).grid(column=Colonnes[j], row=Lignes[i])
			else :
				Button(echecs, text= str(i)+str(j), borderwidth=1, height=7, width=14, bg=color1[c], fg=color2[c], relief=SUNKEN).grid(column=Colonnes[j], row=Lignes[i])
				Button(echecs, image=roi_noir, bg=color1[c], fg=color2[c], relief=FLAT).grid(column=Colonnes[j], row=Lignes[i])
			c=1-c
			i+=1
		elif j == 5 and (i == 1 or i == 8):
			if i == 1 :
				Button(echecs, text= str(i)+str(j), borderwidth=1, height=7, width=14, bg=color1[c], fg=color2[c], relief=SUNKEN).grid(column=Colonnes[j], row=Lignes[i])
				Button(echecs, image=reine_blanc, bg=color1[c], fg=color2[c], relief=FLAT).grid(column=Colonnes[j], row=Lignes[i])
			else :
				Button(echecs, text= str(i)+str(j), borderwidth=1, height=7, width=14, bg=color1[c], fg=color2[c], relief=SUNKEN).grid(column=Colonnes[j], row=Lignes[i])
				Button(echecs, image=reine_noir, bg=color1[c], fg=color2[c], relief=FLAT).grid(column=Colonnes[j], row=Lignes[i])
			c=1-c
			i+=1
		elif i == 2 or i == 7 :
			if i == 2 :
				Button(echecs, text= str(i)+str(j), borderwidth=1, height=7, width=14, bg=color1[c], fg=color2[c], relief=SUNKEN).grid(column=Colonnes[j], row=Lignes[i])
				Button(echecs, image=pion_blanc, bg=color1[c], fg=color2[c], relief=FLAT).grid(column=Colonnes[j], row=Lignes[i])
			else :
				Button(echecs, text= str(i)+str(j), borderwidth=1, height=7, width=14, bg=color1[c], fg=color2[c], relief=SUNKEN).grid(column=Colonnes[j], row=Lignes[i])
				Button(echecs, image=pion_noir, bg=color1[c], fg=color2[c], relief=FLAT).grid(column=Colonnes[j], row=Lignes[i])
			c=1-c
			i+=1
		else :
			Button(echecs, text= str(i)+str(j), borderwidth=1, height=7, width=14, bg=color1[c], fg=color2[c], relief=SUNKEN).grid(column=Colonnes[j], row=Lignes[i])
			c=1-c
			i+=1
	i=1
	j+=1
	c=1-c
print(echecs.grid_slaves(column=1, row= 5))
#tb.grid_remove()
#tb.grid()
root.mainloop()

