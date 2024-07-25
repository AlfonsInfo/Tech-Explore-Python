""" Fungsi dengan argument ( input )"""

def fungsi(input):
    #badan fungsi
    print(f"Hello {input[0]} !!")
    print(f"Hello {input[1]} !!")

fungsi(["ucup","bambang"])

def tambah(angka_1, angka_2):
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")
    #! jika list bisa mengubah data di luar fungsi oleh karena itu dicopy dan ditampung terlebih dahulu di fungsi local
    return hasil

hasil = tambah(2,4)
hasil = tambah(3,5)
print(hasil)