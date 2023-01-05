from qsnctf import *

a = eight_diagrams_encrypt('qsnctf')
print(a)  # 正巽震~正巽兑~正离巽~正艮兑~正巽艮~正艮巽~
a = eight_diagrams_decrypt('正巽震~正巽兑~正离巽~正艮兑~正巽艮~正艮巽~')
print(a)  # qsnctf
