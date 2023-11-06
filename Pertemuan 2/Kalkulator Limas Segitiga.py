import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    Alas = float(txtAlas.get())
    TL = float(txtTinggi_limas.get())
    TS = float(txttinggi_segitiga.get())

    luas = (Alas * TL)/ 2 + 3 * (0.5 * Alas * TS)
    
    txtluas.delete(0,END)
    txtluas.insert(END,luas)

def hitung_volume():
    Alas = float(txtAlas.get())
    TL = float(txtTinggi_limas.get())
    TS = float(txttinggi_segitiga.get())

    volume = (Alas ** 2 * TS) / 6

    txtvolume.delete(0,END)
    txtvolume.insert(END,volume)

def hitung():
    hitung_luas()
    hitung_volume()

app = tk.Tk()
app.title (" Kalkulator Limas Segitiga")

frame = Frame(app)
frame.pack(padx=20, pady=20)

#label
Alas = Label(frame, text="Alas:")
Alas.grid(row=0, column=0,sticky=W, padx=5, pady=5)

Tinggi_limas = Label(frame, text="Tinggi Limas:")
Tinggi_limas.grid(row=1, column=0, sticky=W, padx=5, pady=5)

Tinggi_segitiga = Label(frame, text="Tinggi Segitiga:")
Tinggi_segitiga.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#outputlabel
txtAlas = Entry(frame)
txtAlas.grid(row=0, column=1, sticky=W, padx=5, pady=5)

txtTinggi_limas = Entry(frame)
txtTinggi_limas.grid(row=1, column=1, sticky=W, padx=5, pady=5)

txttinggi_segitiga = Entry(frame)
txttinggi_segitiga.grid(row=2, column=1, sticky=W, padx=5, pady=5)

#button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=0, sticky=W, padx=5, pady=5)

#label output
luas = Label (frame, text="luas:")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

volume = Label (frame, text="volume:")
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

#txt output

txtluas = Entry(frame)
txtluas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

txtvolume = Entry(frame)
txtvolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()