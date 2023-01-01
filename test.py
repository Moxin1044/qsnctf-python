import qsnctf
import os





encoded_string = qsnctf.crypto.bacon_encrypt('Hello, World!')
print(encoded_string)
# Output: AABBBAABAAABABBABABBABBBABABBAABBBABAAABABABBAAABB
decoded_string = qsnctf.crypto.bacon_decrypt(encoded_string)
print(decoded_string)
# Output: HELLOWORLD
