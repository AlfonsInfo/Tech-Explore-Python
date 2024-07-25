import datetime

# modules.class.method
data_waktu = datetime.datetime.now()
print(f"data_waktu : {data_waktu.strftime('%A %m %Y')}")

from collections import Counter

data = ["a", "b", "c", "d", "a", "e","a"]

data_count = Counter(data)

print (f"data count = {data_count}")
print (f"data count a = {data_count['a']}")

import io
file = io.open("file_text.txt", "r")
print(file.read())

#! Graphical User Interface tkinter