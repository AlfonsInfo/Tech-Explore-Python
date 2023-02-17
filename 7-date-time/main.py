# Date and Time ( Latihan )

import datetime as dt #! import datetime as dt

hari_ini = dt.date.today()
# tanggal = dt.date(2002,5,21)
# print(f"{hari_ini:%A}")
# print(tanggal)

print("Silahkan Masukan Tanggal, Bulan dan Tahun Lari Anda \n")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Harinya adalah  : {tanggal_lahir:%A}")

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari //365
umur_bulan_sisa = umur_hari % 365
print(f"umur anda adalah {umur_tahun.days} tahun") #! .days agar cuman ngambil angka