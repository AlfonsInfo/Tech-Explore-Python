# Komparasi membandingkan nilai
# Output Komparasi = boolean

#   > , < >= , <= != == is, is not
# Lebih dari
a = 4
b = 2
print('lebih dari')
hasil = a >3
print(a , '>', b, '=',hasil)
hasil = b>2
print(b , '>', 2, '=',hasil)

b= 2.1
print('kurang dari')
hasil = a<3
print(a , '<', b, '=',hasil)
hasil = b<2
print(b , '<', 2, '=',hasil)

# 'is' sebagai komparasi object identity
x = 5 # ini adalah assignment membuat object
y = 5
# type() id() -> cek addressnya
print(x is y)
print("nilai x : ",x, "id: ", hex(id(x)))
print("nilai y : ",y, "id: ", hex(id(y)))
y = 6
print("nilai y : ",y, "id: ", hex(id(y)))
# Python jika memiliki nilai yang sama akan ditaruh di memory
# yang sama. java/c++ -> ditaruh di memory yang terpisah
# Java memory yang sama system literal
