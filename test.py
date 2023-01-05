from qsnctf import *


a = chr_list_to_ord_list(['a', 'b', 'c'])
print(a)  # ['97', '98', '99']
print(a)  # abc
a = ord_list_to_str_list(['97', '98', '99'])
print(a)  # ['a', 'b', 'c']


a = chr_str_to_ord_str("abc")
print(a)