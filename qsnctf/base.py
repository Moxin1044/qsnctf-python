# Base编码解码功能
# 2023年1月1日
# 末心
import base64
import python3base92
import struct
import base62
import pybase100
# python3base92: https://github.com/Moxin1044/Python3Base92


def base100_encode(text):
    pass


def base100_encode(text, encoding="utf-8"):
    return pybase100.encode(text, encoding)


def base100_decode(text, encoding="utf-8"):
    return pybase100.decode(text, encoding)

def base92_encode(data):
    return python3base92.b92encode(data)


def base92_decode(data):
    return python3base92.b92decode(data)


def base91_encode(data):
    data = data.encode()
    base91_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                       '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$',
                       '%', '&', '(', ')', '*', '+', ',', '.', '/', ':', ';', '<', '=',
                       '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '"']

    decode_table = dict((v, k) for k, v in enumerate(base91_alphabet))
    b = 0
    n = 0
    out = ''
    for count in range(len(data)):
        byte = data[count:count + 1]
        b |= struct.unpack('B', byte)[0] << n
        n += 8
        if n > 13:
            v = b & 8191
            if v > 88:
                b >>= 13
                n -= 13
            else:
                v = b & 16383
                b >>= 14
                n -= 14
            out += base91_alphabet[v % 91] + base91_alphabet[v // 91]
    if n:
        out += base91_alphabet[b % 91]
        if n > 7 or b > 90:
            out += base91_alphabet[b // 91]
    return out


def base91_decode(data):
    base91_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                       '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$',
                       '%', '&', '(', ')', '*', '+', ',', '.', '/', ':', ';', '<', '=',
                       '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', '"']
    decode_table = dict((v, k) for k, v in enumerate(base91_alphabet))
    v = -1
    b = 0
    n = 0
    out = bytearray()
    for strletter in data:
        if not strletter in decode_table:
            continue
        c = decode_table[strletter]
        if v < 0:
            v = c
        else:
            v += c * 91
            b |= v << n
            n += 13 if (v & 8191) > 88 else 14
            while True:
                out += struct.pack('B', b & 255)
                b >>= 8
                n -= 8
                if not n > 7:
                    break
            v = -1
    if v + 1:
        out += struct.pack('B', (b | v << n) & 255)

    return out.decode()


def base64_encode(text):
    code = (base64.b64encode(text.encode('utf-8'))).decode('utf-8')
    return code


def base64_decode(text):
    code = (base64.b64decode(text.encode('utf-8')))
    return code.decode('utf-8')


def base62_encode(text):
    return base62.encode(text)


def base62_decode(text):
    return base62.decode(text)


def base32_encode(text):
    code = (base64.b32encode(text.encode('utf-8'))).decode('utf-8')
    return code


def base32_decode(text):
    code = (base64.b32decode(text.encode('utf-8')))
    return code.decode('utf-8')


def base16_encode(text):
    code = (base64.b16encode(text.encode('utf-8'))).decode('utf-8')
    return code


def base16_decode(text):
    code = (base64.b16decode(text.encode('utf-8')))
    return code.decode('utf-8')


def base85_encode(text):
    code = (base64.b85encode(text.encode('utf-8'))).decode('utf-8')
    return code


def base85_decode(text):
    code = (base64.b85decode(text.encode('utf-8')))
    return code.decode('utf-8')


