import tkinter as tk
from PIL import Image,ImageTk
import model 
root = tk.Tk()
bg_fond = Image.open("fond1.webp")
bg_test = bg_fond.resize((1000,500),Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(bg_test)
back = tk.Label(root, image=bg_image)
back.place(x=0,y=0)
root.mainloop()
