from numbers import Number

def tambah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):
        raise "Input harus angka"
    return a+b
print(tambah(5,6))
#! code dibawahnya tidak dieksekusi #!

angka = 0

try:
    hasil = 10/angka
except Exception as error_message:
    print(error_message)

try:
    hasil = 10/angka
except ZeroDivisionError as error_message:
    print(error_message)