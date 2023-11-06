import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    Alas = float(txtAlas.get())
    TL = float(txttinggi_limas.get())
    TS = float(txttinggi_segitiga.get())
    
    luas = (Alas ** 2) + 2 * Alas * (TS + TS)
    txtLuas.delete(0, END)
    txtLuas.insert(END,luas)

def hitung_volume():
    Alas = float(txtAlas.get())
    TL = float(txttinggi_limas.get())
    TS = float(txttinggi_segitiga.get())

    Volume = (Alas ** 2 * TS) / 3

    txtVolume.delete(0,END)
    txtVolume.insert(END, Volume)

def hitung():
    hitung_luas()
    hitung_volume()

app = tk.Tk()

app.title ("Kalkulator Limas Segi Empat")

frame = Frame (app)
frame.pack(padx=20, pady=20)

#La
Alas =Label(frame, text="Alas:")
Alas.grid(row=0, column=0, sticky=W, padx=5, pady=5)
#ls
tinggi_limas = Label(frame, text="Tinggi Limas:")
tinggi_limas.grid(row=1, column=0,sticky=W, padx=5, pady=5)
#t
tinggi_segitiga = Label(frame, text="Tinggi Segitiga:")
tinggi_segitiga.grid(row=2, column=0,sticky=W, padx=5, pady=5)

txtAlas = Entry(frame)
txtAlas.grid(row=0, column=1,  sticky=W, padx=5, pady=5)

txttinggi_limas = Entry(frame)
txttinggi_limas.grid(row=1, column=1, sticky=W, padx=5, pady=5)

txttinggi_segitiga = Entry(frame)
txttinggi_segitiga.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas
luas= Label(frame, text="Luas: ")
luas.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# output label volume
volume = Label (frame, text="volume: ")
volume.grid(row=5, column=0, stick=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling
txtVolume = Entry (frame)
txtVolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

app.mainloop()