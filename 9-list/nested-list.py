data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]

list_2D = [data_0,data_1]
print(f"list 2D = {list_2D}")

peserta_0 = ["ucup",25,"laki-laki"]
peserta_1 = ["otong",21,"laki-laki"]
peserta_2 = ["bambang",35,"laki-laki"]
list_peserta = [peserta_0,peserta_1,peserta_2]
print(f"list_peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"nama : {peserta[0]}")
    print(f"umur : {peserta[1]}")
    print(f"jenis kelamin : {peserta[2]}")

#!Ada masalah dengan reference copy()diluar tidak berpengaruh pada nested list
list_copy = list_peserta.copy()
print(f"list_peserta = {list_copy}")
peserta_0[0] = "micahel"
print(f"list_peserta = {list_peserta}")
print(f"list_peserta = {list_copy}")