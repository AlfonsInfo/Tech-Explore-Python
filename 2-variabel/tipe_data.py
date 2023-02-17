data_integer = 1
print("data : ", data_integer) 
print( "bertipe : ", type(data_integer))

#float , double tidak ada
data_float = 1.5
print("data : ", data_float) 
print( "bertipe : ", type(data_float))

data_string = "ucup"
print("data : ", data_string) 
print( "bertipe : ", type(data_string))


data_bool = True
print("data : ", data_bool) 
print( "bertipe : ", type(data_bool))

# Tipe Data Comple
data_complex = complex(5,6)
print("data : ", data_complex) 
print( "bertipe : ", type(data_complex))

# Tipe Data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.5)
print("data : ", data_c_double) 
print( "bertipe : ", type(data_c_double))

