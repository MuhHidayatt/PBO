import tkinter as tk 
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_luas():
    r = float(txtrusuk.get())

    L = round(6*(r**2))

    txtLuas.delete(0, END)
    txtLuas.insert(END,L)

def hitung_keliling():
    r = float(txtrusuk.get())

    k = round(r**3)
    
    txtkeliling.delete(0,END)
    txtkeliling.insert(END,k)

def hitung():
    hitung_luas()
    hitung_keliling()

# Create tkinter object app = tk.Tk()
app = tk.Tk()

# Tambahkan judul
app.title("Menghitung Luas dan Keliling Kubus")

# windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama = Label(frame, text="MUHAMMAD HIDAYAT 220511088")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Nama
nama = Label(frame, text="Menghitung Luas Dan Keliling Kubus")
nama.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Rusuk
rusuk = Label(frame, text="Rusuk")
rusuk.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Textbox Rusuk
txtrusuk = Entry(frame)
txtrusuk.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas Kubus: ")
luas.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output label Keliling
keliling = Label(frame, text="Kelilig Kubus: ")
keliling.grid(row=7, column=0, sticky=W, padx=5, pady=5)


# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=6, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Keliling
txtkeliling = Entry(frame)
txtkeliling.grid(row=7, column=1, sticky=W, padx=5, pady=5)

app.mainloop()