## Teknik menduplikasi list

a = ["ucup","otong","bambang"]
print(f"a = {a}")

b = a.copy()  #! List b disi dengan data dari data dengan alamat a OLEH KARENA ITU GUNAKAN .copy
print(f"b = {b}")

#! Mengubah a akan mengubah b , b akan mengubah a 
a[1] = "Michael"
b.sort()
print(f"a = {a} addres {hex(id(a))}")
print(f"b = {b} addres {hex(id(b))}")