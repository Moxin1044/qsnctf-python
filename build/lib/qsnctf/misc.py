# 其他CTF能力
# 2023年1月1日
# 末心
import os
import execjs  # PyExecJS
from qsnctf.auxiliary import js_from_file
# 社会主义核心价值观编码
# 需要将Python目录下>lib>subprocess.py的765行附近的encoding的默认None值修改为utf-8即可。


def Chinese_socialism_encode(data):
    # 社会主义核心价值观编码
    package_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(package_path, 'plugin', 'js', 'cvencode.js')
    content = execjs.compile(js_from_file(file_path))
    result = content.call('encode', data)
    result = str(result)
    return result


def Chinese_socialism_decode(data):
    # 社会主义核心价值观解码
    package_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(package_path, 'plugin', 'js', 'cvencode.js')
    content = execjs.compile(js_from_file(file_path))
    result = content.call('decode', data)
    result = str(result)
    return result


def string_reverse(string):
    # 字符串逆向
    return string[::-1]