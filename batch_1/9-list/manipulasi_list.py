## Operasi pada List

# index 0 , 1, 2 | index -1 , -2 -> jika dicek dari belakang

data = ["ucup","Otong","Dudung"]
print(f"data pertama (index 0) = {data[0]}")
print(f"data terakhir (index -1) = {data[-1]}")

#Mengambil info jumlah data dalam list
panjang_data = len(data)
print(panjang_data)

#Menambahkan Item pada list sesuai posisi
print(f"data sebelum ditambah = {data}")
dataw.insert(1,"Asepp")
print(f"data setelah ditambah = {data}")
#Menambah diakhir list
data.append("Jajang")
print(f"data setelah ditambah = {data}")
#Menambahkan list dan list
data_baru = ["Ujang","Usep","Dadang","ucup"] #! data bisa sama !!
data.extend(data_baru)
print(f"data setelah ditambah = {data}")
#Mengubah Data
data[-1] = "michael"
print(f"data setelah diubah = {data}")
data.remove("Ujang") #! akan error jika huruf tidak sesuai (case sensitive)
print(f"data setelah diremove = {data}")
data_akhir = data.pop() #! menghapus data paling belakang
print(f"data setelah diremove = {data}")
print(data_akhir)