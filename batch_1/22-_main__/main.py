# __main__ -> adalah top level code environment

#__name__ =="__""__"

## __name__ pada file program utama
print(f"nilai__main__ pada main.py = {__name__}")
##__name__ saat kita run sebagai program utama nilainya akan berubah menjadi __main__ (#! terjadi pada program utama)
##__name__ pada file program eksternal
import fungsi

##contoh penggunaan main __main__

#deklarasi
def fungsi_tambah(a:int,b:int)->int:
    return a+b
    # a:int ini hint, ->int nilai balikan
#fungsi utama
if __name__ =="__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(5,10)
    print(f"hasil tambah = {hasil}")

# main akan dipanggil saat kita panggil package