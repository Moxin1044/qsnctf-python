import qsnctf
import os

a = qsnctf.caesar_encrypt("qsnctf", 3)
print(a)
a = qsnctf.caesar_decrypt("tvqfwi", 3)
print(a)

a = qsnctf.crypto.caesar_decrypt_cracking("tvqfwi")
for i in a:
    print(i)