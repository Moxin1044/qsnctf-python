# 其他CTF能力
# 2023年1月1日
# 末心

import execjs  # PyExecJS
# 社会主义核心价值观编码
# 需要将Python目录下>lib>subprocess.py的765行附近的encoding的默认None值修改为utf-8即可。


def js_from_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()
        return result


def Chinese_socialism_encode(data):
    content = execjs.compile(js_from_file('qsnctf/plugin/js/cvencode.js'))
    result = content.call('encode', data)
    result = str(result)
    return result

def Chinese_socialism_decode(data):
    content = execjs.compile(js_from_file('qsnctf/plugin/js/cvencode.js'))
    result = content.call('decode', data)
    result = str(result)
    return result

