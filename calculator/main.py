import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Weather App")
root.geometry("900x600")
img = Image.open('bg.png')
img = img.resize((900, 600), Image.ANTIALIAS)
img_photo = ImageTk.PhotoImage(img)

bg_lbl = tk.Label(root, image_photo)
bg_lbl.place(x=0, y=0, width=900, height=500)

root.mainloop()
