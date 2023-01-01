import qsnctf
# import json


# a = qsnctf.crypto.caesar_decrypt_cracking("oqlard")
# jsona = json.loads(a)
# print(jsona['1'])

a = qsnctf.base91_encode("qsnctf")
print(a)
b = qsnctf.base91_decode("#2U==[WC")
print(b)