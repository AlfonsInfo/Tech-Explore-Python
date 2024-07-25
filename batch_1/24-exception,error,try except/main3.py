try:
    with open("data.txt",'r') as file:
        print(file.read())
except:
    print("file data.txt tidak ditemukan , membuat file")
    with open("data.txt",'w',encoding="utf-8") as file:
            file.write("file baru")
print("akhir dari program 2")
