data_angka = [1,5,1,4,3,2,3,21,21,13,32,32]

print(f"data angka = {data_angka}")

#? Count data caranya bagaimana ?
jumlah_data_21  = data_angka.count(21)
print(f"Jumlah data 21 = {jumlah_data_21}")


#? Ambil posisi data

data = ["Ucup", "Otong", "Bambang", "Dodo"]

index_dodo  = data.index("Dodo") #! case sensitive
print(f"index dodo {index_dodo}")

print("data angka sebelum sorting!!")
print(f"data angka = {data_angka}")
print("data angka setelah sorting!!")
data_angka.sort() #! tidak memiliki nilai balikan
#! TIDAK BISA CHAINING
print(f"data angka = {data_angka}")
data_angka.reverse()
print(f"data angka = {data_angka}")