"""file init"""

# print("Hello, Program Init dijalankan!!")

from . import matematika
from . import fisika

# from .matematika.basic import tambah #! bisa dichaining importnya agar lebih elegan :)
# from .matematika import kali #! jadi error karena matematika dianggap folder

#! hanya dijalankan jika kita mengunakan import * from sains import *
#! __all__ tidak disarankan penggunaannya :)
__all__ = [
    'matematika',
    'fisika'
]