from qsnctf import *


a="adb"
b="123"
tmp=xor_list(a,b)
print(tmp)
c=[]
for i in range(3):
    c.append(chr(i))
print(c)
tmp=xor_list(a,c)
print(tmp)