from qsnctf import *

a = html_encode('<script>')
print(a)
b = html_decode('&lt;script&gt;')
print(b)