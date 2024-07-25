teman_teman = {
    "cup" : "ucup surucup",
    "tong" : "tong tongsurotong",
    "mbang" : "bambang sibambang",
}

#! looping first yang keluar adalah keynya
for teman in teman_teman:
    print(teman) 
#!------------------ diatas contoh yang salah -------------------

keys = teman_teman.keys()
print(keys)

for keys in teman_teman:
    print(teman_teman.get(keys))

values = teman_teman.values()
print(values)

for values in teman_teman.values():
    print(f"valuesnya diiterableskan {values}")

items = teman_teman.items()
print(items)

for keys,values in teman_teman.items():
    print(f"keynya : {keys} , valuesnya :{values}")