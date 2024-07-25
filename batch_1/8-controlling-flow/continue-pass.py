# Continue, Pass, break

#pass berfungsi sebagai dummy -> tidak akan dieksekusi

angka = 0 

#? pass dan continue
while angka < 5 :
    angka+=1
    if angka ==3:
        # print("Waddap")
        pass #ini tidak akan dieksekusi , ada tetapi tidak ada implementasi
    if angka%2 ==0:
        continue #* Melompati literasi yang terjadi, code dibawah if ini tidak akan dieksekusi
    print(angka)
angka = 0

#? bagian break!
print("Bagian Breakkk")
while angka < 5:
    angka+=1
    if angka==3:
        print("break dijalankan!")
        break
    print(angka)