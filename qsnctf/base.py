# Base编码解码功能
# 2023年1月1日
# 末心
import base64


def base64_encode(text):
    code = (base64.b64encode(text.encode('utf-8'))).decode('utf-8')
    return code


def base64_decode(text):
    code = (base64.b64decode(text.encode('utf-8')))
    return code.decode('utf-8')


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
