import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W
from math import pi

def hitung_luas():
    r = float(txtjari_jari.get())

    L = round(4*pi*r**2)

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    r = float(txtjari_jari.get())
    
    v = round((4/3)*pi*r**3)
    
    txtvolume.delete(0,END)
    txtvolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Menghitung Luas dan Volume Bola")

# windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

nama = Label(frame, text="MUHAMMAD HIDAYAT 220511088")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

nama = Label(frame, text="MENGHITUNG LUAS DAN VOLUME BOLA")
nama.grid(row=1, column=0, sticky=W, padx=5, pady=5)

jari_jari = Label(frame, text="Jari-Jari")
jari_jari.grid(row=2, column=0, sticky=W, padx=5, pady=5)

txtjari_jari = Entry(frame)
txtjari_jari.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas : ")
luas.grid(row=6, column=0, sticky=W, padx=5, pady=5)

volume = Label(frame, text="Volume : ")
volume.grid(row=7, column=0, sticky=W, padx=5, pady=5)

txtLuas = Entry(frame)
txtLuas.grid(row=6, column=1, sticky=W, padx=5, pady=5)

txtvolume = Entry(frame)
txtvolume.grid(row=7, column=1, sticky=W, padx=5, pady=5)

app.mainloop()