## --- LIST 000
#! di python array tidak ada, sama dengan dart namanya list !!
#* Number
data_angka = [1,2,3]
print(data_angka, type(data_angka))

#*String
data_string = ["ayam","anjing","harimau"]
print(data_string, type(data_string))

#*Boolean
data_bool = [True,False,True]
print(data_bool, type(data_bool))

#*Campuran
data_mix = [1, True ,"String"]
print(data_mix, type(data_mix))

#? Cara Alternatif membuat list

data_range = range(0,10,2) #?ini belum berbentuk list params -> start,stop,step
print(data_range)
data_list = list(data_range)
print(data_list)

list_for = [ i**10 for i in range(0,10,3)] #! list dari (i pangkat 10) yang dimana i nya itu range(0,10,3)
print(list_for)

list_for_if = [i for i in range(0,10) if i%2!=0]
print(list_for_if)