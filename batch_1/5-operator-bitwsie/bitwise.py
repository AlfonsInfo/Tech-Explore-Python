# Operasi bilangan biner
a = 9
b = 5
# bitwise OR(|)
c = a|b
print("\n============OR=============")
print("Nilai : ",a,' binary : ', format(a,'08b'))
print("Nilai : ",b,' binary : ', format(b,'08b'))
print('------------------------------------- !')
print("Nilai : ",c,' binary : ', format(c,'08b'))
c = a & b
print("\n============OR=============")
print("Nilai : ",a,' binary : ', format(a,'08b'))
print("Nilai : ",b,' binary : ', format(b,'08b'))
print('------------------------------------- &')
print("Nilai : ",c,' binary : ', format(c,'08b'))
c = a ^ b
print("\n============OR=============")
print("Nilai : ",b,' binary : ', format(b,'08b'))
print('------------------------------------- &')
c = ~a
print("Nilai : ",a,' binary : ', format(a,'08b'))
print("Nilai : ",c,' binary : ', format(c,'08b'))