# Operasi dan manipulasi string
# Concatenate string
nama_pertama = "ucup"
nama_tengah = "D"
nama_akhir = "Fame"
nama_lengkap = nama_pertama +" "+ nama_tengah +" " + nama_akhir
print(nama_lengkap)
# Panjang String
panjang = len(nama_lengkap)
print(panjang)
# Operator untuk string
d = "d"
status = d in nama_lengkap
print("string ", d ," ada di ", nama_lengkap,"=",str(status))
status = d not in nama_lengkap
print("string ", d ," tidak ada di ", nama_lengkap,"=",str(status))

# mengulang string
print("wk" * 10)

#indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-(-1) : " + nama_lengkap[-1]) # mulai dari belakang
print("index terakhir : " + nama_lengkap[len(nama_lengkap)-1])
print("index ke-0:3 : " + nama_lengkap[0:4]) # yang terakhir tidak diikuti parah beut python
print("index ke-[0,2,4,5,8,10] : " + nama_lengkap[0:11:2])
# item paling kecil
print("paling kecil : " + min(nama_lengkap))
print("paling besar : " + min(nama_lengkap))

# chr -> dari ascii ke char
# ord

# Operator dalam bentuk method
# Method nempel di string
data ="otong suroong pararotong"
jumlah = data.count('o')
print("jumlah o pada data = " + str(jumlah))
