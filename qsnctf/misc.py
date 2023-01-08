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
import html
import zipfile
import uuid
from qsnctf.auxiliary import read_file_to_list, is_http_or_https_url, normalize_url


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
    pattern = r'(' + flag_prefix + ')\{.+\}'
    match = re.search(pattern, text)
    if match:
        result = match.group(0)
        return result
    else:
        return False


def baijiaxing_encode(source_text):
    CODE = {
        "赵": "0", "钱": "1", "孙": "2", "李": "3", "周": "4", "吴": "5", "郑": "6", "王": "7", "冯": "8",
        "陈": "9",
        "褚": "a", "卫": "b", "蒋": "c", "沈": "d", "韩": "e", "杨": "f", "朱": "g", "秦": "h", "尤": "i",
        "许": "j",
        "何": "k", "吕": "l", "施": "m", "张": "n", "孔": "o", "曹": "p", "严": "q", "华": "r", "金": "s",
        "魏": "t",
        "陶": "u", "姜": "v", "戚": "w", "谢": "x", "邹": "y", "喻": "z", "福": "A", "水": "B", "窦": "C",
        "章": "D",
        "云": "E", "苏": "F", "潘": "G", "葛": "H", "奚": "I", "范": "J", "彭": "K", "郎": "L", "鲁": "M",
        "韦": "N",
        "昌": "O", "马": "P", "苗": "Q", "凤": "R", "花": "S", "方": "T", "俞": "U", "任": "V", "袁": "W",
        "柳": "X",
        "唐": "Y", "罗": "Z", "薛": ".", "伍": "-", "余": "_", "米": "+", "贝": "=", "姚": "/", "孟": "?",
        "顾": "#",
        "尹": "%", "江": "&", "钟": "*"
    }
    source_text = re.sub('[\u4e00-\u9fa5]', '', source_text)
    # source_text = source_text.replace( r"/ ^\s\s * /", '').replace( r"/\s\s *$ /", '')
    CODE = dict((value, key) for key, value in CODE.items())
    cc = [CODE[i] for i in source_text]
    dd = ''.join(cc)
    return dd


def baijiaxing_decode(source_text):
    CODE = {
        "赵": "0", "钱": "1", "孙": "2", "李": "3", "周": "4", "吴": "5", "郑": "6", "王": "7", "冯": "8",
        "陈": "9",
        "褚": "a", "卫": "b", "蒋": "c", "沈": "d", "韩": "e", "杨": "f", "朱": "g", "秦": "h", "尤": "i",
        "许": "j",
        "何": "k", "吕": "l", "施": "m", "张": "n", "孔": "o", "曹": "p", "严": "q", "华": "r", "金": "s",
        "魏": "t",
        "陶": "u", "姜": "v", "戚": "w", "谢": "x", "邹": "y", "喻": "z", "福": "A", "水": "B", "窦": "C",
        "章": "D",
        "云": "E", "苏": "F", "潘": "G", "葛": "H", "奚": "I", "范": "J", "彭": "K", "郎": "L", "鲁": "M",
        "韦": "N",
        "昌": "O", "马": "P", "苗": "Q", "凤": "R", "花": "S", "方": "T", "俞": "U", "任": "V", "袁": "W",
        "柳": "X",
        "唐": "Y", "罗": "Z", "薛": ".", "伍": "-", "余": "_", "米": "+", "贝": "=", "姚": "/", "孟": "?",
        "顾": "#",
        "尹": "%", "江": "&", "钟": "*"
    }
    source_text = re.sub('[^\u4e00-\u9fa5]+', '', source_text)
    # source_text = source_text.replace( r"/ ^\s\s * /", '').replace( r"/\s\s *$ /", '')
    cc = [CODE[i] for i in source_text]
    dd = ''.join(cc)
    if dd:
        return dd
    else:
        return '解码失败'


def qwerty_encode(source_text):
    str1 = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    str2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result_text = ""
    for s in source_text:
        if s in str1:
            if s != ' ':
                result_text = result_text + str1[str2.index(s)]
            else:
                result_text = result_text + ' '
        else:
            return 'Qwerty只能对字母编码!'
    return result_text


def qwerty_decode(source_text):
    try:
        letter = {
            'q': 'a', 'w': 'b', 'e': 'c', 'r': 'd', 't': 'e', 'y': 'f', 'u': 'g',
            'i': 'h', 'o': 'i', 'p': 'j', 'a': 'k', 's': 'l', 'd': 'm', 'f': 'n',
            'g': 'o', 'h': 'p', 'j': 'q', 'k': 'r', 'l': 's', 'z': 't',
            'x': 'u', 'c': 'v', 'v': 'w', 'b': 'x', 'n': 'y', 'm': 'z',
            'Q': 'A', 'W': 'B', 'E': 'C', 'R': 'D', 'T': 'E', 'Y': 'F', 'U': 'G',
            'I': 'H', 'O': 'I', 'P': 'J', 'A': 'K', 'S': 'L', 'D': 'M', 'F': 'N',
            'G': 'O', 'H': 'P', 'J': 'Q', 'K': 'R', 'L': 'S', 'Z': 'T',
            'X': 'U', 'C': 'V', 'V': 'W', 'B': 'X', 'N': 'Y', 'M': 'Z',
        }
        result_text = ''
        for i in range(0, len(source_text)):
            if source_text[i] != ' ':
                result_text = result_text + letter.get(source_text[i])
            else:
                result_text = result_text + ' '
    except Exception as e:
        return '解码失败'
    return result_text.strip()


def html_encode(string):
    return html.escape(string)


def html_decode(string):
    return html.unescape(string)


def jsfuck_encode(source_text):
    # jsfuck_encode
    package_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(package_path, 'plugin', 'js', 'jsfuck_encode.js')
    content = execjs.compile(js_from_file(file_path))
    return content.call("JSFuck", source_text)


def jsfuck_decode(source_text):
    # jsfuck_decode
    package_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(package_path, 'plugin', 'js', 'jsfuck_decode.js')
    content = execjs.compile(js_from_file(file_path))
    return content.call("decode", source_text)


def aaencode(source_text):
    # aaencode
    package_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(package_path, 'plugin', 'js', 'aaencode.js')
    content = execjs.compile(js_from_file(file_path))
    return content.call("aaencode", source_text)


def aadecode(source_text):
    # aadecode
    package_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(package_path, 'plugin', 'js', 'aaencode.js')
    content = execjs.compile(js_from_file(file_path))
    return content.call("aadecode", source_text)


def str_to_hex(string, encoding='utf-8', byteorder='big'):
    b = string.encode(encoding)
    b = int.from_bytes(b, byteorder)
    x = hex(b)
    return x


def hex_to_str(hex_int, decoding='utf-8'):
    if type(hex_int) == str:
        hex_int = int(hex_int, 16)  # 防呆（防止输入了个字符串）
    h = hex(hex_int)
    if '0x' in str(h):
        return bytes.fromhex(h[2:]).decode(decoding)
    return bytes.fromhex(h).decode(decoding)


class ZipPasswordCracking:
    def __init__(self, zip_file, pass_list):
        self.zip_file = zip_file
        self.pass_list = pass_list

    def read_pass(self):
        if self.pass_list:
            pass  # 如果使用自定义的pass_list,这里不用读取
        else:
            package_path = os.path.abspath(os.path.dirname(__file__))
            file_path = os.path.join(package_path, 'plugin', 'txt', 'dirs.txt')
            self.pass_list = read_file_to_list(file_path)

    def check_zip_is_passed(self):
        if zipfile.is_zipfile(self.zip_file):
            with zipfile.ZipFile(self.zip_file) as zip_file:
                try:
                    zip_file.printdir()
                except Exception as e:
                    if isinstance(e, zipfile.BadZipfile):
                        print("Zip file is password protected")

    def crack_password(self, password):
        pass


