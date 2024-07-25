"""
Numpy package populer untuk operasi matematika aka matriks
Hati-hati dengan penamaan file jangan sampai meng override suatu library
"""
import numpy as np
list_a  = [1,2,3,4]
vector_a = np.array([1,2,3,4]) #* ini array

print(f"list_a ={list_a}")
# print(f"list_a**2 ={list_a**2}") #! tidak bisa
print(f"vector_a ={vector_a}")
print(f"vector_a dipangkatin 2={vector_a**2}")
print(f"vector_a dikali 2 ={vector_a*2}")

matrix_b = np.array([(1,2),(2,3)])
print(f"matrik b = \n{matrix_b}")

matrix_zeros = np.zeros([2,2])
print(f"zero = \n{matrix_zeros}")
matrix_ones = np.ones([2,2])
print(f"one = \n{matrix_ones}")