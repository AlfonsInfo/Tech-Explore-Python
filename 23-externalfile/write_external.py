#1/ mode write #* python otomatis membuat file baru jika tidak ada
with open("data_1.txt","w",encoding="utf-8") as file:
    file.write("john si jhonny")
# override 
with open("data_1.txt","w",encoding="utf-8") as file:
    file.write("ucup surucup")
with open("data_1.txt","w",encoding="utf-8") as file:
    file.write("ketimpa ga tu ?")

with open("data_2.txt","w",encoding="utf-8") as file:
    file.write("ucup surucup\n")
with open("data_2.txt","a",encoding="utf-8") as file:
    file.write("ketimpa ga tu ?")
#3. mode r+
with open ("data_3.txt", 'w', encoding='utf8') as file:
    file.write("data ke 3\n")
with open("data_3.txt", 'r+',encoding="utf-8") as file:
    file.write("menambah dengan r+") #* menimpa isi text sesuai dengan panjang data
    data = file.read()
    print(data)