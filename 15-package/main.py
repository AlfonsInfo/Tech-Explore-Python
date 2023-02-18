# package tempat menaruh module
# import sains #! import package

import time
t_start = time.time()
import sains.matematika
#* from sains import gaya
#* from sains.fisika import gaya as Force
#! saat di compile otomatis python membuat __pycache__ agar saat di run kembali kita tidak perlu membmuat
#! file ulang tetapi tinggal ngambil dari bytecodenya !!
#! pycache -> mempercepat eksekusi :)
hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"hasil tambah dari package adalah = {hasil_tambah}")
t_end = time.time()

print(f"waktu eksekusi adlaah = {t_end - t_start}")
