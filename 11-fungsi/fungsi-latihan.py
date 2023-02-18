"""Latihan Fungsi"""

import os

#program menghitung luas dan keliling persegi panjang

#Membuat Header program

def header_app():
    os.system("cls")
    #* Header Aplikasi
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print("-"*40)

def input_user():
    lebar = int(input("Masukan nilai Lebar : "))
    panjang = int(input("Masukan nilai Panjang : "))
    return lebar,panjang

def hitung_luas(lebar,panjang):
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    return 2*(lebar+panjang)

def display(message, value):
    print(f"Hasil perhitungan {message} = {value}")

while True:
    header_app()
    LEBAR, PANJANG = input_user()
    #!ubah menjadi ada opsi misalnya, lebih mudah maintain
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)
    display('LUAS', LUAS)
    display('KELILING', KELILING)
    isContinue = input("apakah lanjut (y/n) ?")
    if isContinue == "n":
        break
print("Program selesai, terima kasih")
#*Input User



