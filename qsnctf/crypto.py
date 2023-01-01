def caesar_encrypt(text, shift):
    # 凯撒加密 （重新写的）
    ciphertext = ''
    for p in text:
        if 'a' <= p <= 'z':
            ciphertext += chr(ord('a') + (ord(p) - ord('a') + shift) % 26)
        elif 'A' <= p <= 'Z':
            ciphertext += chr(ord('A') + (ord(p) - ord('Z') + shift) % 26)
        else:
            ciphertext += p
    return ciphertext


def caesar_decrypt(text, shift):
    # 凯撒解密 （一样，重新写的）
    ciphertext = ''
    for p in text:
        if 'a' <= p <= 'z':
            ciphertext += chr(ord('a') + (ord(p) - ord('a') - shift) % 26)
        elif 'A' <= p <= 'Z':
            ciphertext += chr(ord('A') + (ord(p) - ord('Z') - shift) % 26)
        else:
            ciphertext += p
    return ciphertext


def caesar_decrypt_cracking(ciphertext):
    # 凯撒解密爆破，返回值为列表
    results = []
    for i in range(1, 26):
        plaintext = caesar_decrypt(ciphertext,i)
        results.append("您的偏移量为{}，结果为{}".format(i, plaintext))
    return results

def caesar_encrypt_cracking(ciphertext):
    # 凯撒解密爆破，返回值为列表
    results = []
    for i in range(1, 26):
        plaintext = caesar_encrypt(ciphertext,i)
        results.append("您的偏移量为{}，结果为{}".format(i, plaintext))
    return results
