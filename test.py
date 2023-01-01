import qsnctf
# import json


# a = qsnctf.crypto.caesar_decrypt_cracking("oqlard")
# jsona = json.loads(a)
# print(jsona['1'])
import qsnctf

a = qsnctf.base.base62_encode(34441886726)
print(a)
b = qsnctf.base.base62_decode("base62")
print(b)

a = qsnctf.base.base100_encode("base100_encode")
print(a)
a = qsnctf.base.base100_decode("👙👘👪👜🐨🐧🐧👖👜👥👚👦👛👜")
print(a)