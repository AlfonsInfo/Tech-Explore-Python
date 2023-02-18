teman_teman = {
    "cup" : "ucup-surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung",
    "sep" : "asep si kasyep",
    "cuy" : "ucuy surucuy"
}
friends = teman_teman.copy() #! dengan pake copy aman referencenya
print(f"teman_teman : {teman_teman}")
print(f"friends :{friends}")
friends["cup"] = "ucup sikweren"
print(f"teman_teman : {teman_teman}")
print(f"friends :{friends}")

# pop dictionary berdasarkan eky
dataAsep = friends.pop("sep")
print(f"data asep {dataAsep}")
print(f"friends {friends}")
# pop dictionary yang terakhir ajah ^_^
dataTerakhir = friends.popitem()
print(f"data asep {dataTerakhir}")
print(f"friends {friends}")