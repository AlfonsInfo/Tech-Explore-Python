import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
#! Sebuah program berada dalam 1 loop sampai di close.
window.configure(bg="white")
window.geometry("500x500")
window.resizable(False,False)
window.title("Sapa Dia!?")

# Frame Input
input_frame = ttk.Frame(window)
#Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x", expand=True)
#-Komponen-komponen
# 1. Label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan")
nama_depan_label.pack(padx=10,pady=10,fill="x", expand=True)
# 2. entry nama depan
NAMA_DEPAN = tk.StringVar()
nama_depan_entry =ttk.Entry(input_frame,textvariable = NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x", expand=True)
# 3. Label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama Belakang")
nama_belakang_label.pack(padx=10,pady=10,fill="x", expand=True)
# 4. entry nama belakang
NAMA_BELAKANG = tk.StringVar()
nama_belakang_entry =ttk.Entry(input_frame,textvariable = NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)

# 5. Tombol
def tombol_click():
    print(NAMA_DEPAN.get())
    print(NAMA_BELAKANG.get())
    showinfo(title="wazzup",message="1 Nasi Padang")

tombol_sapa = ttk.Button(input_frame, text="Sapa!",command=tombol_click)
tombol_sapa.pack(fill='x',expand=True,padx=10,pady=10)
# * Dibawah Konfigurasi dari GUI APP
window.mainloop()

#! INSTALL LIBRARY -PACKAGE INDEX -> PIP