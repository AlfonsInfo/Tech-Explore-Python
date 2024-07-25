""""kwargs"""

def fungsi(**kwargs):
    print(kwargs) #* argumentnya berupa dictionary asalkan di argument yang didefinisikan bersamaan dengan keynya
    # print(kwargs['nama']) #* argumentnya berupa dictionary asalkan di argument yang didefinisikan bersamaan dengan keynya
    nama = kwargs['nama']
    umur = kwargs['umur']
    asal = kwargs['asal']
    print(f"{nama} punya umur {umur} dan asal {asal}")

fungsi(nama = 'ucup', umur='20', asal='pekanbaru')

#? STUDI KASUS ?

def math(*args,**kwargs):
    output = 0
    print(kwargs)
    if kwargs["option"] == "tambah":
        for angka in args:
            output+= angka
    elif kwargs['option'] == "kali":
        output = 1
        for angka in args:
            output*= angka
    else:
        print("tidak ada operasi")
    return output
hasil = math(2,3,3,2,32,23,32,option ='kali')
print(f"hasilnya adalah {hasil}")

hasil = math(2,3,3,2,32,23,32,option ='tambah')
print(f"hasilnya adalah {hasil}")

#!skenario seperti ini banyak di framework python !! :)
