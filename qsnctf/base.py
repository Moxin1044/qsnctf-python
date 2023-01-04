# Base编码解码功能
# 2023年1月1日
# 末心
import base64
import qsnctf.plugin.python.python3base92
import struct
import base62
import base58


# python3base92: https://github.com/Moxin1044/Python3Base92


def base100_encode(text, encoding="utf-8", decoding="utf-8"):
    if isinstance(text, str):
        data = text.encode(encoding)
    out = [240, 159, 0, 0]*len(data)
    for i, b in enumerate(data):
        out[4*i+2] = (b + 55) // 64 + 143
        out[4*i+3] = (b + 55) % 64 + 128
    return bytes(out).decode(decoding)


def base100_decode(text, encoding="utf-8", decoding="utf-8"):
    if isinstance(text, str):
        data = text.encode(encoding)
    if len(data) % 4 != 0:
        raise Exception('Length of string should be divisible by 4')
    tmp = 0
    out = [None] * (len(data) // 4)
    for i, b in enumerate(data):
        if i % 4 == 2:
            tmp = ((b - 143) * 64) % 256
        elif i % 4 == 3:
            out[i // 4] = (b - 128 + tmp - 55) & 0xff
    return bytes(out).decode(decoding)


def base92_encode(data):
    return qsnctf.plugin.python.python3base92.b92encode(data)


def base92_decode(data):
    return qsnctf.plugin.python.python3base92.b92decode(data)


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
    b, n = 0, 0
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
    v, b, n = -1, 0, 0
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


def base85_encode(text, encoding="utf-8", decoding="utf-8"):
    code = (base64.b85encode(text.encode(encoding))).decode(decoding)
    return code


def base85_decode(text, encoding="utf-8", decoding="utf-8"):
    code = (base64.b85decode(text.encode(encoding)))
    return code.decode(decoding)


def base64_encode(text, encoding="utf-8", decoding="utf-8"):
    code = (base64.b64encode(text.encode(encoding))).decode(decoding)
    return code


def base64_decode(text, encoding="utf-8", decoding="utf-8"):
    code = (base64.b64decode(text.encode(encoding))).decode(decoding)
    return code


def base62_encode(ints):
    return base62.encode(ints)


def base62_decode(text):
    return base62.decode(text)


def base58_encode(text, encoding="utf-8", decoding="utf-8"):
    return base58.b58encode(text.encode(encoding)).decode(decoding)


def base58_decode(text, encoding="utf-8", decoding="utf-8"):
    return base58.b58decode(text.encode(encoding)).decode(decoding)


def base36_encode(number):
    charset = "0123456789abcdefghijklmnopqrstuvwxyz"
    encoded = ""
    while number > 0:
        encoded = charset[number % 36] + encoded
        number //= 36
    if encoded == "":
        encoded = "0"
    return encoded


def base36_decode(encoded):
    charset = "0123456789abcdefghijklmnopqrstuvwxyz"
    number = 0
    for i, ch in enumerate(encoded[::-1]):
        number += charset.index(ch) * (36 ** i)
    return number


def base32_encode(text, encoding="utf-8", decoding="utf-8"):
    code = (base64.b32encode(text.encode(encoding))).decode(decoding)
    return code


def base32_decode(text, encoding="utf-8", decoding="utf-8"):
    code = (base64.b32decode(text.encode(encoding)))
    return code.decode(decoding)


def base16_encode(text, encoding="utf-8", decoding="utf-8"):
    code = (base64.b16encode(text.encode(encoding))).decode(decoding)
    return code


def base16_decode(text, encoding="utf-8", decoding="utf-8"):
    code = (base64.b16decode(text.encode(encoding)))
    return code.decode(decoding)