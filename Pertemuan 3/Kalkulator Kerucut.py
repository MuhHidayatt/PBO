import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    r = float(txtjari_jari.get())
    t  = float(txttinggi.get())
    s = float(txtgaris_pelukis.get())

    from math import pi

    L = round(pi * r * s + pi * r **2)

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    r = float(txtjari_jari.get())
    t = float(txttinggi.get())
    s = float(txtgaris_pelukis.get())

    from math import pi

    v = round((1/3) * pi * r ** 2 * t)
    
    txtvolume.delete(0,END)
    txtvolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Menghitung Luas Permukaan dan Volume Kerucut")

# windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="MUHAMMAD HIDAYAT 220511088")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Nama
nama = Label(frame, text="PROGRAM KERUCUT")
nama.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Jari-Jari
jari_jari = Label(frame, text="Jari-Jari")
jari_jari.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi
tinggi = Label(frame, text="Tinggi")
tinggi.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Label garis pelukis
garis_pelukis = Label(frame, text="Garis pelukis")
garis_pelukis.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Textbox Jari-Jari
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=2, column=1)

# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=3, column=1)

# Textbox Selimut
txtgaris_pelukis = Entry(frame)
txtgaris_pelukis.grid(row=4, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas Permukaan: ")
luas.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label(frame, text="Volume: ")
volume.grid(row=7, column=0, sticky=W, padx=5, pady=5)


# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling
txtvolume = Entry(frame)
txtvolume.grid(row=7, column=1, sticky=W, padx=5, pady=5)

app.mainloop()