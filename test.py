from qsnctf import *
a=caesar_encrypt("Hello world",12)
print(a)
b=a
a=caesar_decrypt(a,12)
print(a)
print(caesar_decrypt_cracking(b))


a = rot13('qsnctf')
print(a)