class Constants:
    PI = 3.14159
    GRAVITY = 9.81

# Akses konstanta
print(Constants.PI)
print(Constants.GRAVITY)

# Mencegah perubahan konstanta
def set_const(name, value):
    raise TypeError(f"Cannot rebind constant {name}")

Constants.__setattr__ = set_const

# Mencoba mengubah konstanta akan menghasilkan error
# Constants.PI = 3.14  # TypeError: Cannot rebind constant PI
