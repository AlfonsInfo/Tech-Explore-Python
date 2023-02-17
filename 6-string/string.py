# Cara membuat string

data = "Ini adalah string"
print(data)
print(type(data))

"""
    1.Cara membuat string dengan single quote
    2.Double quote
"""
data = 'Menggunakan single quote'
print(data)
data = "Menggunakan dobule quote"
print(data)
data = "'Bisa dikombinasikan seperti ini dan sebaliknya'"
print(data)

"""
    Menggunakan tanda ' menjadi string
"""
print("test menggunakan backslash jum\'at")

# backslash
print("C:\\user\\Ucup")
# tab
print("ucup\t\t\t otong, semakin jauhan")
# backspace
print("ucup \botong")
# newline
print("baris pertama \nbaris kedua") #LF -> Line Feed -> line food, unix ,macos, linux
print("baris pertama \rbaris kedua") #CR -> Carriage Return -> carriage return  ->
print("baris pertama \r\nbaris kedua") #CR -> Carriage Retur
# Mendeteksi end of line

# String literal atau raw
# hati-hati
#print('C:\newfolder') #akan salah pathnya

# Menggunakan row string
print(r'C:\new folder\nn')

print("""
    Multiline woyyyy
    test
""")