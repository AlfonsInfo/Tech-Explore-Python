kumpulan_angka  = [2,3,21,12,13,22]
for a in kumpulan_angka:
    print(f"angka : {a}")

nama_orang = ["bambang","memey","kekey"]

for nama in nama_orang:
    print(f"nama orang : {nama}")

#? cara lebih singkat ? list comprehension
data = ["ucup",2,3,True]
[print(f"data {i}") for i in data]

#? enumerate
for index,data in enumerate(data):
    print(f"index = {index}, datanya = {data}")


#! angka_kuadrat = [i**2 for i in angka]