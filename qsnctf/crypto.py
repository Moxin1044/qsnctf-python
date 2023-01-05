import json


def caesar_encrypt(text, shift):
    # 凯撒加密 （重新写的）
    ciphertext, shift = '', int(shift)
    for p in text:
        if p.islower():
            ciphertext += chr(97 + (ord(p) - 97 + shift) % 26)
        elif p.isupper():
            ciphertext += chr(65 + (ord(p) - 65 + shift) % 26)
        else:
            ciphertext += p
    return ciphertext


def caesar_decrypt(text, shift):
    shift = int(shift)
    return caesar_encrypt(text, -shift)


def caesar_decrypt_cracking(ciphertext):
    # 凯撒解密爆破，返回值为json
    results = {}
    for i in range(1, 26):
        results[str(i)] = caesar_decrypt(ciphertext, i)
    return json.dumps(results)


def caesar_encrypt_cracking(ciphertext):
    # 凯撒加密爆破，返回值为json
    results = {}
    for i in range(1, 26):
        results[str(i)] = caesar_encrypt(ciphertext, i)
    return json.dumps(results)


def bacon_encrypt(string):
    # 培根密码加密
    bacon = {'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB',
             'E': 'AABAA', 'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB',
             'I': 'ABAAA', 'J': 'ABAAB', 'K': 'ABABA', 'L': 'ABABB',
             'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA', 'P': 'ABBBB',
             'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
             'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB',
             'Y': 'BBAAA', 'Z': 'BBAAB', 'a': 'AAAAA', 'b': 'AAAAB',
             'c': 'AAABA', 'd': 'AAABB', 'e': 'AABAA', 'f': 'AABAB',
             'g': 'AABBA', 'h': 'AABBB', 'i': 'ABAAA', 'j': 'ABAAB',
             'k': 'ABABA', 'l': 'ABABB', 'm': 'ABBAA', 'n': 'ABBAB',
             'o': 'ABBBA', 'p': 'ABBBB', 'q': 'BAAAA', 'r': 'BAAAB',
             's': 'BAABA', 't': 'BAABB', 'u': 'BABAA', 'v': 'BABAB',
             'w': 'BABBA', 'x': 'BABBB', 'y': 'BBAAA', 'z': 'BBAAB'}
    encoded_string = ''
    for char in string:
        char = char.upper()
        if char in bacon:
            encoded_string += bacon[char]
    return encoded_string


def bacon_decrypt(string):
    bacon = {'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D',
             'AABAA': 'E', 'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H',
             'ABAAA': 'I', 'ABAAB': 'J', 'ABABA': 'K', 'ABABB': 'L',
             'ABBAA': 'M', 'ABBAB': 'N', 'ABBBA': 'O', 'ABBBB': 'P',
             'BAAAA': 'Q', 'BAAAB': 'R', 'BAABA': 'S', 'BAABB': 'T',
             'BABAA': 'U', 'BABAB': 'V', 'BABBA': 'W', 'BABBB': 'X',
             'BBAAA': 'Y', 'BBAAB': 'Z'}
    decoded_string = ''
    for i in range(0, len(string), 5):
        chunk = string[i:i + 5]
        if chunk in bacon:
            decoded_string += bacon[chunk]
    return decoded_string


def rot13(text):
    # ROT13 加密即解密
    # 还有一种写法是 凯撒，偏移量13
    mapping = {
        'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R',
        'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W',
        'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B',
        'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G',
        'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L',
        'Z': 'M'
    }
    # 加/解密文本
    encrypted_text = ''
    for char in text:
        if char.upper() in mapping:
            if char.isupper():
                encrypted_text += mapping[char]
            else:
                encrypted_text += mapping[char.upper()].lower()
        else:
            encrypted_text += char

    return encrypted_text


def rot5(text):
    # ROT5 加密即解密
    mapping = {
        '0': '5', '1': '6', '2': '7', '3': '8', '4': '9',
        '5': '0', '6': '1', '7': '2', '8': '3', '9': '4',
    }
    # 加/解密文本
    encrypted_text = ''
    for char in text:
        if char in mapping:
            encrypted_text += mapping[char]
        else:
            encrypted_text += char

    return encrypted_text


def rot18(text):
    # ROT18 加密即解密
    mapping = {
        '0': '5', '1': '6', '2': '7', '3': '8', '4': '9',
        '5': '0', '6': '1', '7': '2', '8': '3', '9': '4',
        'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R',
        'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W',
        'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B',
        'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G',
        'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L',
        'Z': 'M'
    }
    # 加/解密文本
    encrypted_text = ''
    for char in text:
        if char.upper() in mapping:
            if char.isupper():
                encrypted_text += mapping[char]
            else:
                encrypted_text += mapping[char.upper()].lower()
        else:
            encrypted_text += char

    return encrypted_text


def eight_diagrams_encrypt(text):
    # 八卦加密 仅支持ASCII码支持的字符
    codelist = []
    fuxi = ['坤', '震', '坎', '兑', '艮', '离', '巽', '乾']
    strlist = text
    for character in strlist:
        if len(bin(ord(character)).replace('0b', '')) == 7:
            codelist.append(str(bin(ord(character)).replace('0b', '')))
        else:
            codelist.append('0' + str(bin(ord(character)).replace('0b', '')))
    r = ''
    for code in codelist:
        code3 = []
        code2 = list(code)
        if code2[0] == '0':
            cncode0 = '逆'
        else:
            cncode0 = '正'
        cncode1 = str(fuxi[int(str(code2[1] + code2[2] + code2[3]), 2)])
        cncode2 = str(fuxi[int(str(code2[4] + code2[5] + code2[6]), 2)])
        cncode = cncode0 + cncode1 + cncode2
        r += cncode + "~"
    return r

def eight_diagrams_decrypt(text):
    fuxi = ['坤', '震', '坎', '兑', '艮', '离', '巽', '乾']
    string = text
    cncodelist = string.split('~')
    del cncodelist[-1]
    r = ''
    for cncode in cncodelist:
        cncodesplit = list(cncode)
        if cncodesplit[0] == '逆':
            code1 = '0'
        else:
            code1 = '1'
        if len(str(bin(fuxi.index(cncodesplit[1])).replace('0b', ''))) == 3:
            code2 = str(bin(fuxi.index(cncodesplit[1])).replace('0b', ''))
        elif len(str(bin(fuxi.index(cncodesplit[1])).replace('0b', ''))) == 2:
            code2 = '0' + str(bin(fuxi.index(cncodesplit[1])).replace('0b', ''))
        else:
            code2 = '00' + str(bin(fuxi.index(cncodesplit[1])).replace('0b', ''))
        if len(str(bin(fuxi.index(cncodesplit[2])).replace('0b', ''))) == 3:
            code3 = str(bin(fuxi.index(cncodesplit[2])).replace('0b', ''))
        elif len(str(bin(fuxi.index(cncodesplit[2])).replace('0b', ''))) == 2:
            code3 = '0' + str(bin(fuxi.index(cncodesplit[2])).replace('0b', ''))
        else:
            code3 = '00' + str(bin(fuxi.index(cncodesplit[2])).replace('0b', ''))
        code = code1 + code2 + code3
        character = chr(int(code, 2))
        r += character
    return r


# def vigenere_encrypt(text,key):
#     return vigenere.encrypt(text, key, base64=False)
#
#
# def vigenere_decrypt(text,key):
#     return vigenere.decrypt(text, key)

