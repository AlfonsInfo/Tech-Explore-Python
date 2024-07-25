"""args"""


#memasukan data/argument

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
fungsi("ucup", 170,40)
# override #! ribet yak 
def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
fungsi(["otong", 160,30])


def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")
fungsi("dudung", "120", 45)
    
#? Studi kasus untuk tambah
#! untuk arguments dinamic ?
def tambah(*data):
    # data tipenya tuple
    output = 0
    for angka in data:
        output+=angka

    return output

hasil_tambah = tambah(2,3,4,5,5,5,2,2,2,32,13,12)
print(hasil_tambah)