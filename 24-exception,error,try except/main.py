# Handle Error Runtime

#? Runtime -> run saat program dijalankan
#? syntak error -> saat di compile
#?------------------------------------
#? saat runtime error kita ingin program tetap jalan 
#! exception akan terjadi saat program mengalami error saat runtime

# coba sederhana untuk menangkap exception
from math import nan
input_user = int(input("masukan angka : "))
hasil = nan

try:
    hasil = 10/input_user
    print(f"hasil = {hasil}")
except:
    print("Input tidak boleh 0")