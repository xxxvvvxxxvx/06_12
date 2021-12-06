import tkinter as tk
window = tk.Tk()


lbl_sveiki = tk.Label(text = “Hello,world!”)
lbl_sveiki.pack()

window.mainloop()

lbl_sveiki = tk.Label(
text = "Sveika, Pasaule!",
foreground="white", # Teksta krāsa - balta
background="black" # Fona krāsa - melna
)

lbl_citads = tk.Label(
text = "Jāpamēģina!",
background="#34A2FE",
width=10, #Platums
height=10 #Augstums
)
lbl_citads.pack()


btn_poga = tk.Button(
text="Noklikšķini!",
width=26,
height=6,
bg="red", #saīsinājums background
fg="yellow", #saīsinājums foreground
)

btn_poga.pack()

lbl_sveiki.pack(fill=tk.X)
lbl_citads.pack(side=tk.LEFT)

def noklikskina(event):
print("Noklikšķināja!")

btn_poga.bind("<Button-1>", noklikskina)
noklikskina_lab

