import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    l = float(txtlebar.get())
    p = float(txtpanjang.get())
    t = float(txttinggi.get())

    L = round((2*p*l)+(2*p*t)+(2*l*t))

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_volume():
    l = float(txtlebar.get())
    p = float(txtpanjang.get())
    t = float(txttinggi.get())

    v = round(p*l*t)
    
    txtvolume.delete(0,END)
    txtvolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Menghitung Luas dan Volume Balok")

# windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="MUHAMMAD HIDAYAT 220511088")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Nama
nama = Label(frame, text="MENGHITUNG LUAS DAN VOLUME BALOK")
nama.grid(row=1, column=0, sticky=W, padx=5, pady=5)

panjang = Label(frame, text="Panjang")
panjang.grid(row=2, column=0, sticky=W, padx=5, pady=5)

lebar = Label(frame, text="Lebar")
lebar.grid(row=3, column=0, sticky=W, padx=5, pady=5)

tinggi = Label(frame, text="Tinggi")
tinggi.grid(row=4, column=0, sticky=W, padx=5, pady=5)

txtpanjang = Entry(frame)
txtpanjang.grid(row=2, column=1)

txtlebar = Entry(frame)
txtlebar.grid(row=3, column=1)

txttinggi = Entry(frame)
txttinggi.grid(row=4, column=1)

hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas : ")
luas.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output label Volume
volume = Label(frame, text="Volume : ")
volume.grid(row=7, column=0, sticky=W, padx=5, pady=5)

txtLuas = Entry(frame)
txtLuas.grid(row=6, column=1, sticky=W, padx=5, pady=5)

txtvolume = Entry(frame)
txtvolume.grid(row=7, column=1, sticky=W, padx=5, pady=5)

app.mainloop()