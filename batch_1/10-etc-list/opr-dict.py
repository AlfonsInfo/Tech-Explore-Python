data_dict ={
    'cup' : "ucup surucup",
    "tong" : "otong surotong",
    "mbang" : "bambang surambang"
}
#panjang dictionary -> bbrp python nyaranin huruf besar
LENDICT = len(data_dict) #!huruf besar langsung konstan
# LENDICT = 2 #? tapi kok bisa di reassignment?
print(f"panjang dictionary {LENDICT}")

KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data dict: {CHECKKEY}")
print(data_dict["cup"]) #! bisa return NaN
#! print(data_dict["cm"]) #! bisa return NaN
print(data_dict.get("cx","key tidak ditemukan"))
data_dict.update({"cup":"cupppp sicucucp"})
print(data_dict)
del data_dict["cup"]
print(data_dict)
data_dict.update({"new":"data baru"}) #* jika key tidak ada otomatis ditambahkan
data_dict["waw"] = "data baru juga" #* jika key tidak ada otomatis ditambahkans
print(data_dict)