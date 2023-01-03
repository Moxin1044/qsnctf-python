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
    return str(content.call('encode', string))


def Chinese_socialism_decode(string):
    # 社会主义核心价值观解码
    package_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(package_path, 'plugin', 'js', 'cvencode.js')
    content = execjs.compile(js_from_file(file_path))
    return str(content.call('decode', string))


def string_reverse(string):
    # 字符串逆向
    return string[::-1]


def string_reverse_step2(s):
    # 步长为2的逆向
    # 输入abc123 得到ba1c32
    # 主要应用场合为文件的Hex的转换
    lst = [c for c in s]
    result = ''
    for i in range(0, len(lst), 2):
        result += ''.join(lst[i:i+2][::-1])
    return result


def url_encode(string):
    # url编码
    return urllib.parse.quote(string)


def url_decode(string):
    # url解码
    return urllib.parse.unquote(string)


def xor_list(lt_data, lt_root):
    # 异或 lt_root直接传列表过来，这样也可以字符串之间互相异或
    decrypted = ""
    for i in range(min(len(lt_data), len(lt_root))):
        decrypted += chr(ord(lt_data[i]) ^ ord(lt_root[i]))
    return decrypted

