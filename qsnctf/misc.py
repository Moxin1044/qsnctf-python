# 杂项功能
# 2023年1月1日
# 末心
# 社会主义核心价值观编码
# 需要将Python目录下>lib>subprocess.py的765行附近的encoding的默认None值修改为utf-8即可。
import os
import execjs  # PyExecJS
from qsnctf.auxiliary import js_from_file
import urllib.parse
import re
import uuid


def get_uuid():
    return str(uuid.uuid4())


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
    """
    直接逆向
    主要应用场合为文件的Hex的转换
    :param string: abc123
    :return: 321cba
    """
    return string[::-1]


def string_reverse_step(string, step):
    """
    步长为step的逆向(自定义步长)
    主要应用场合为文件的Hex的转换
    :param string: abc123
    :param step: 步长
    :return: ba1c32
    """
    lst = [c for c in string]
    result = ''
    for i in range(0, len(lst), step):
        result += ''.join(lst[i:i + step][::-1])
    return result


def string_reverse_step2(string):
    """
    步长为2的逆向
    主要应用场合为文件的Hex的转换
    :param string: abc123
    :return: ba1c32
    """
    string_reverse_step(string, 2)


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


def string_split(s):
    # 如果字符串中包含逗号，就按照逗号分割
    if ',' in s:
        return s.split(',')
    # 如果包含空格按照空格分割
    elif ' ' in s:
        return s.split()
    # 否则按照字符方式分割
    else:
        r_list = []
        for str in s:
            r_list.append(str)
        return r_list


def ord_to_str(ord):
    return chr(int(ord))


def ord_list_to_str_list(ord_list):
    r_list = []
    for ords in ord_list:
        r_list.append(ord_to_str(ords))
    return r_list


def ord_str_to_str(ord_str):
    r_text = ''
    ord_list = string_split(ord_str)
    for ords in ord_list:
        r_text += ','.join(ord_to_str(ords))
    return r_text


def chr_to_ord(char):
    return ord(char)


def chr_list_to_ord_list(chr_list):
    r_list = []
    for char in chr_list:
        r_list.append(chr_to_ord(char))
    return r_list


def chr_str_to_ord_str(chr_str):
    r_text = ''
    char = string_split(chr_str)
    for chars in char:
        r_text += str(chr_to_ord(chars)) + ","
    return r_text[:-1]


def search_flag(text, flag_prefix='flag|qsnctf|ctf'):
    """
    :param text: search string
    :param flag_prefix: flag prefix eg: flag|qsnctf|ctf
    :return: flag{xxxxxxx}
    """
    # pattern = f'({flag_prefix})' + r'\{[\w]+\}'
    pattern = r'(flag|qsnctf|ctf)\{.+\}'
    match = re.search(pattern, text)
    if match:
        result = match.group(0)
        return result
    else:
        return False
