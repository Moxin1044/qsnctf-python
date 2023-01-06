import re


def js_from_file(file_name):
    # 读文件
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()
        return result


def read_file_to_list(file_name):
    # 读入文件，并以换行符分割
    lines = []
    with open(file_name, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def is_http_or_https_url(url):
    # 检测是否是http或https地址
    pattern = r'^https?:\/\/'
    return re.match(pattern, url) is not None


def normalize_url(url):
    # 去掉末尾的/
    return url.rstrip('/')