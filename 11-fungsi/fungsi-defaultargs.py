""" Default Argument"""

def say_hello(nama = "Kamyuu"): #! ini default arguments
    print(f"Hallo {nama}")

say_hello()
say_hello("ucup")


def sapa_dia(pesan = '',nama="kamu"):
    print(f"hai {nama}, {pesan}")

sapa_dia('apa kabar ? ')
sapa_dia('apa kabar ? ', 'otong')


def hitung_pangkat(angka,pangkat):
    hasil=angka**pangkat
    return hasil

hasil = hitung_pangkat(angka=3,pangkat=3) #* nama parameternya bisa dituliskan juga!!
print(hasil) #!ini berguna untuk fungsi dengan argument yang banyak 🫡
