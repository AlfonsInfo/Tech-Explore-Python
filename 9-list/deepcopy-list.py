
from copy import deepcopy
data_0 = [1,2]
data_1 = [3,4]

data_2d = [data_0,data_1]
data_2d_copy =data_2d.copy()
data_2d_deep = deepcopy(data_2d) #! ada yang harus diimport
print(f"data asli= {data_2d} address {hex(id(data_2d))}") 
print(f"data copy= {data_2d_copy} address {hex(id(data_2d_copy))}") 
print(f"data asli index 0 = {data_2d} address {hex(id(data_2d[0]))}") #! addressnya sama
print(f"data copy index 0 = {data_2d_copy} address {hex(id(data_2d_copy[0]))}") #!addressnya sama
print(f"data copy deep 0 = {data_2d_deep} address {hex(id(data_2d_deep[0]))}") #!addressnya sama
print(f"data asli index 0 = {data_2d} address {hex(id(data_2d[0][0]))}") #!addressnya sama
print(f"data copy index 0 = {data_2d_copy} address {hex(id(data_2d_copy[0][0]))}") #!addressnya sama
print(f"data copy deep 0 = {data_2d_deep} address {hex(id(data_2d_deep[0][0]))}") #!addressnya sama

data_2d[0][1]= 10
data_2d_deep[0][1]= 9
print(data_2d)
print(data_2d_copy)
print(data_2d_deep)