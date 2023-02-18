# Import
# Fungsinya untuk mengambil program dari file external .py

#*1. untuk menyambung program
import program_print
import program_ucup
print("ini main.py")

#* import dengan data
import variable
import kucuy
#! data ada di namespace variable
# print(data)
print(variable.data)
print(kucuy.data)

#* import dengan fungsi
import matematika as mt
hasil_hitung = mt.hitungJumlah(2,3,4,5)
print(hasil_hitung)