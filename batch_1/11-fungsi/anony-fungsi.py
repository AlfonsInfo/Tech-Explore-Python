# Lambda Function -> Simplifikasi aplikasi

def f_kuadrat(angka):
    return angka**2
print(f_kuadrat(3))

# * Fungsi Lambda
kuadrat = lambda angka:angka**2
print(f"hasil lambda kuadrat = {kuadrat(3)}")

pangkat = lambda num,pow : num**pow
print(f"hasil lambda pangkat  = {pangkat(2,3)}")

# ? Kegunaanyan apa bang ?
#! sorting list berdasarkan alphabet
data_list=['otong','ucup','dudung']
data_list.sort()
print(f"sorted lsit = {data_list}")

#! sorting berdasarkan panjang
data_list.sort(key=len)
print(f"Sorted list by len = {data_list}")
data_list=['otong','ucup','dudung']

data_list.sort(key= lambda nama:len(nama))
print(f"Sorted list by len using lambda = {data_list}")


# filter

data_angka = [1,2,32,32,3,2,1,5,5,52,3,23]

def kurang_dari_5(angka):
    return angka<5

data_angka_baru = list(filter(kurang_dari_5,data_angka))
print(data_angka_baru)
data_angka_baru2 = list(filter(lambda x:x<5,data_angka))
print(f"data angka baru {data_angka_baru2}")


# anonymous function
#  currying <- haskel curry

def pangkat(angka,n):
    hasil = angka ** n
    return hasil
data_hasil = pangkat(5,2)
print(f"hasil fungsi biasa = {data_hasil}")

def pangkat(nilai_pangkat):
    return lambda angka:angka**nilai_pangkat

pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(5)}")
print(f"pangkat3 {pangkat(nilai_pangkat=3)(angka=2)}")