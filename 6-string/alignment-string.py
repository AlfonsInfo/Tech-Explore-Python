# width dan multi line

#Data

data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

data_string =f"nama = {data_nama}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*data_string)

data_string =f"nama = {data_nama}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print(data_string)

#! multiline bisa menggunakan f""" """"
#! NAMA = {DATA_NAMA:>10}