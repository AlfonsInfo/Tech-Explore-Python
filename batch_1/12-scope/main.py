## global dan local scope

nama_global = "otong" # ini variable global

#*akses variable global dalam fungsi
def fungsi1():
    print(f"fungsi menampilkan nama {nama_global}")

fungsi1()

#* akses variable global dalam loop

for i in range(0,5):
    print(f"loop {i} - {nama_global}")

if True:
    print(f"if menampilkan {nama_global}")

#? Kenapa ada variable local

def fungsi2():
    nama_local = "Ucup"

fungsi2()
# print(nama_local) #! nama_local karena bersifat local scope  

## Contoh  1 penggunaan #*Python membaca code secara sekuensial
def say_otong():
    print(f"Hello {nama}")
nama = "Otong"
say_otong()

## Contoh 2 Merubah Variable Global
"""
angka = 0
def ubah_angka(nilai_baru):
    angka = nilai_baru
print(f"sebelum angka diubah = {angka}")
ubah_angka(3)
print(f"setelah angka diubah = {angka}")
"""
#! code diatas tidak bekerja, perubahan hanya berlaku didalam fungsi
angka = 0
def ubah_angka(nilai_baru):
    global angka
    angka = nilai_baru
print(f"sebelum angka diubah = {angka}")
ubah_angka(3)
print(f"setelah angka diubah = {angka}")

#!untuk for & if local variable bisa diakses
