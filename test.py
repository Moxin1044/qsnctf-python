from qsnctf import *

data = 'SGVsbG8sIFdvcmxkIQ=='
custom_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-'
a = base64_encode_custom(data, custom_table)
print(a)