def encryptCaesarCipher(text, shift):
    encrypted = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            encrypted += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            encrypted += chr((ord(char) + shift - 97) % 26 + 97)
    return encrypted

def decryptCaesarCipher(text, shift):
    decrypted = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            decrypted += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            decrypted += chr((ord(char) - shift - 97) % 26 + 97)
    return decrypted

text = input("Enter text: ")
shift = int(input("Enter shift: "))
encrypted = encryptCaesarCipher(text, shift)
print("Encrypted text: ", encrypted)
decrypted = decryptCaesarCipher(encrypted, shift)
print("Decrypted text: ", decrypted)
# 