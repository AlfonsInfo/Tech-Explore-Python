def kuadrat(input_angka): #* kita punya input
    output_kuadrat = input_angka**2
    return output_kuadrat #*output

y1 = kuadrat(3)
y2 = kuadrat(5)
print(y1)
print(y2)
print(kuadrat(7))

# fungsi tambah

def tambah(input_angka1,input_angka2):
    return input_angka1 + input_angka2
print(tambah(3,4))

def operasi_matematika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 + angka_2

    return tambah,kurang,kali,bagi

k,l,m,n = operasi_matematika(3,4)
print(f"hasil tambah {k}")
print(f"hasil kurang {l}")
print(f"hasil kali {m}")
print(f"hasil bagi {n}")