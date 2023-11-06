import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W
from math import pi

def hitung_luas():
    r = float(txtjari_jari.get())
    t  = float(txttinggi.get())

    LS = round((2)*pi*r*t)

    LP = round(((2)*pi*r*t)+((2)*pi*r**2))

    txtLuasS.delete(0, END)
    txtLuasS.insert(END,LS)

    txtLuasP.delete(0, END)
    txtLuasP.insert(END,LP)

def hitung_volume():
    r = float(txtjari_jari.get())
    t = float(txttinggi.get())

    v = round(pi*r**2*t)
    
    txtvolume.delete(0,END)
    txtvolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Menghitung Luas Selimut, Luas Permukaan dan Volume Tabung")

# windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="MUHAMMAD HIDAYAT 220511088")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Nama
nama = Label(frame, text="Menghitung Luas dan Volume Tabung")
nama.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Jari-Jari
jari_jari = Label(frame, text="Jari-Jari")
jari_jari.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi
tinggi = Label(frame, text="Tinggi")
tinggi.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Jari-Jari
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=2, column=1)

# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=3, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Selimut
LuasS = Label(frame, text="Luas Selimut: ")
LuasS.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
LuasP = Label(frame, text="Luas Permukaan: ")
LuasP.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label(frame, text="Volume: ")
volume.grid(row=7, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Selimut
txtLuasS = Entry(frame)
txtLuasS.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuasP = Entry(frame)
txtLuasP.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtvolume = Entry(frame)
txtvolume.grid(row=7, column=1, sticky=W, padx=5, pady=5)

app.mainloop()