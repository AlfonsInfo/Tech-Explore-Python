data = input("Masukan data : ")

# data yang dimasukkan selalu string oleh karena itu butuh casting
print("data : ", data ,"tipe datanya :", type(data))
data = int(input("Masukan data : "))
print("data : ", data ,"tipe datanya :", type(data))

# Bagaimana dengan boolean ? 
# kalo dimasukin false -> datanya tetap true, karena dia false hanya ketika string kosong
data = bool(int(input("Masukan data boolean : ")))
print("data : ", data ,"tipe datanya :", type(data))
# bisa menggunakan if then 
