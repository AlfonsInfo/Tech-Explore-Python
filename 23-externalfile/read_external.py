#membaca file external
print(3*"=", " Membaca file txt ", 3*"=")

file = open("data.txt",mode="r")
print(file)
print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")
# print(file.read()) #* baca seluruh file
print(file.readline(),end ="") #* baca baris per baris
# print(file.readline()) #* baca baris per baris

##baca semua baris sebagai list
print(file.readlines())

#! Setiap open kita harus tutup
print(f"apakah file sudah diclose ? {file.closed}")
file.close() #* harus ditutup dlu
print(f"apakah file sudah diclose ? {file.closed}")

## salah satu teknik membuka file di python
print(3*"=", " Membaca file txt ", 3*"=")

with open("data.txt",mode="r") as file:
    content =file.read()
    print(content) #end="a"
    # diluar ini otomatis tertutup
print(f"apakah file sudah diclose ? {file.closed}")


