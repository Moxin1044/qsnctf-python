# 其他CTF能力
# 2023年1月1日
# 末心
import os
import execjs  # PyExecJS
from qsnctf.auxiliary import js_from_file
import urllib.parse
import re


# 社会主义核心价值观编码
# 需要将Python目录下>lib>subprocess.py的765行附近的encoding的默认None值修改为utf-8即可。


def Chinese_socialism_encode(string):
    # 社会主义核心价值观编码
    package_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(package_path, 'plugin', 'js', 'cvencode.js')
    content = execjs.compile(js_from_file(file_path))
    result = content.call('encode', string)
    return str(result)


def Chinese_socialism_decode(string):
    # 社会主义核心价值观解码
    package_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(package_path, 'plugin', 'js', 'cvencode.js')
    content = execjs.compile(js_from_file(file_path))
    result = content.call('decode', string)
    return str(result)


def string_reverse(string):
    # 字符串逆向
    return string[::-1]


def url_encode(string):
    # url编码
    return urllib.parse.quote(string)


def url_decode(string):
    # url解码
    return urllib.parse.unquote(string)


def xor_decrypt(list):
    # 按位异或
    # 由于位异或算法在逆向题中不一定是怎么样的运算，只放个典型
    decrypted = ""
    for i in range(len(list)):
        decrypted += chr(list[i] ^ i)
    return decrypted


def xor_decrypt_1(list):
    # 按位异或 +1
    decrypted = ""
    for i in range(len(list)):
        decrypted += chr(list[i] ^ i + 1)
    return decrypted

