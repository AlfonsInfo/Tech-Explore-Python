while(True):
    angka = int(input("masukan angka pembagi: "))
    try:
        hasil = 10/angka
        print(f"hasil = {hasil}")
        is_done = input("lanjutan (y/n)")
        if is_done == "n":
            break
    except:
        print("pembagi nol, silahkan masukan input lagi")
print("Akhir dari program")