"""
def fungsi(parameter):
    hasil = parameter*2

fungsi (1)
# fungsi ("ucup") #!akan menjadi masalah 
# fungsi (True) #! akan menjadi masalah
#? Solusinya ? Gunaka Type hints
"""
import string 
def fungsi_dengan_hints(argument:int):
    return  10**argument

def display(argument:string):
    print(f"ini argument : {argument}")

hasil = fungsi_dengan_hints(3)
print(hasil)

display()