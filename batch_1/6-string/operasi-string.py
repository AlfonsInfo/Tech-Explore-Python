# Operator dalam bentuk methods
# merubah case dari string
salam = "bro!"
print(salam.capitalize()) # huruf depan doang
print(salam.upper()) #semuanya

# merubah kelower case
alay = "Aku Kece AbiEzzzZzzzzz"
print(alay.lower())

# pengecekan case
salam = "sist"
apakah_lower = salam.islower()
print(str(apakah_lower))
apakah_upper = salam.isupper()
print(str(apakah_upper))

#* isalpha() -> untuk mengecek semua huruf
#* isalnum() -> untuk ngecek alpha number
#* isdecimal ->
#* isspace
#* istitle() -> semua kata dimulai dengan huruf besar

judul = "It's Okay Not Be Orkay" #! Judul tidak boleh menggunakan kutip" an
print(judul.istitle())

##ngecek komponen startwith endwith
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim") #* bisa cek kata akhir dengan endwith
print("sangjangnim " + str(cek_start))

pisah = ['aku', 'sayang', 'kamu'] #* Ini list
print(pisah)
gabungan = ', '.join(pisah) 
print(gabungan)
gabungan = ' '.join(pisah) 
print(gabungan)
gabungan = ' ehm '.join(pisah) 
print(gabungan)
gabungan = gabungan.split(" ehm ")
print(gabungan)

print(5*"=" + "data" + 5*"=")
# alokasi karakter rjust , ljust, cente
tengah = "tengah".center(20, "=")

# ! masih banyak method-method lainnya