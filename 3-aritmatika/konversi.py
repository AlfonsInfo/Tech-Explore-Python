"""
Celcius Reamur:4/5C Farenheit:9/5+32 Kelvin :C+273
Reamur 5/4 9/4+32 5/4+273
Fahrenheit 5/9(F-32) , 4/9(F-32)
Kelvin K-273, 4/5(K-273)
"""
# Program Konversi Celcius Ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR\n")
celcius = float(input('Masukan suhu dalam celcius '))
print('suhu adalah ',celcius,'celcius')
# Reamur
reamur = (4/5) * celcius #dikurung biar aman
print('suhu adalah ',reamur,'reamur')
# Fahrenheit
fahrenheit = ((9/5) * celcius ) + 32
print('suhu adalah ',fahrenheit,'fahrenheit')
# Kelvin
kelvin = celcius + 273 
print('suhu adalah ',kelvin,'kelvin')

# Kelvin ke Fahrenheit
kelvin = float(input('Masukan suhu dalam kelvin '))
fahrenheit = (9/5)*(kelvin-273)+32
print('suhu adalah ',fahrenheit,'fahrenheit')

# Fahrenheit ke Kelvin
fahrenheit = float(input('Masukan suhu dalam fahrenheit '))
kelvin = (5/9)*(fahrenheit-32)+273
print('suhu adalah ',kelvin,'kelvin')
