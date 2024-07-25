#* format string
#* contoh generic
nama = "marlen"
str = "hello " + nama
print(str)

format_str = f"hello {nama}"
print(format_str)

#* angka
angka =2005.5
format_str = f"angka = {angka}"
print(format_str)
angka =15
format_str = f"bilangan bulat = {angka:d}" #! harus integer
print(format_str)
angka =15000000
format_str = f"bilangan bulat = {angka:,}" #* otomatis koma
print(format_str)
angka =2005.54321
format_str = f"angka = {angka:.0f}" #! nentuin berapa dibelakang koma
print(format_str)
# Menampilkan leading zero
angka =2005.54321
format_str = f"angka = {angka:1.0f}" 
print(format_str)

#! minus selalu kelaur sedangkan plus {angka_plus:+.2f}
#! format persen
persentase = 0.045
format_persen =f"persen = {persentase:.2%}"
print(format_persen)
harga = 10000
jumlah = 5
format_string = f"harga total = {harga*jumlah:,}"
print(format_string)

#* boolean
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)