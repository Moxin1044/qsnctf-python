import re
import random
import argparse
from urllib.parse import quote, unquote

VALUES = '富强民主文明和谐自由平等公正法治爱国敬业诚信友善'


def str2utf8(s: str) -> str:
    pattern = re.compile(r'[A-Za-z0-9\-_.!~*\'()]')

    def replace(match):
        return f'{ord(match.group()):02X}'

    encoded = pattern.sub(replace, s)
    return quote(encoded, safe='').upper().replace('%', '')


def utf82str(hex_str: str) -> str:
    if len(hex_str) % 2 != 0:
        raise ValueError('Invalid hex length')

    percent_encoded = '%'.join([hex_str[i:i + 2] for i in range(0, len(hex_str), 2)])
    return unquote(f'%{percent_encoded}')


def hex2duo(hex_str: str) -> list:
    duo = []
    for c in hex_str:
        n = int(c, 16)
        if n < 10:
            duo.append(n)
        else:
            if random.choice([True, False]):
                duo.extend([10, n - 10])
            else:
                duo.extend([11, n - 6])
    return duo


def duo2hex(duo: list) -> str:
    hex_digits = []
    i = 0
    while i < len(duo):
        if duo[i] < 10:
            hex_digits.append(str(duo[i]))
            i += 1
        else:
            if duo[i] == 10:
                hex_digits.append(f'{duo[i + 1] + 10:X}')
            else:
                hex_digits.append(f'{duo[i + 1] + 6:X}')
            i += 2
    return ''.join(hex_digits)


def encode(text: str) -> str:
    hex_str = str2utf8(text)
    duo = hex2duo(hex_str)
    return ''.join([VALUES[2 * d] + VALUES[2 * d + 1] for d in duo])


def decode(encoded: str) -> str:
    duo = []
    for c in encoded:
        idx = VALUES.find(c)
        if idx != -1 and idx % 2 == 0:
            duo.append(idx // 2)
    hex_str = duo2hex(duo)
    return utf82str(hex_str)


def interactive_mode():
    modes = {
        '1': ('加密', encode),
        '2': ('解密', decode),
    }

    while True:
        print('\n=== 社会主义核心价值观编解码 ===')
        print('1. 加密\n2. 解密\n3. 退出')
        choice = input('请选择操作: ').strip()

        if choice == '3':
            break

        if choice not in modes:
            print('无效选择')
            continue

        mode_name, func = modes[choice]

        text = input(f'输入待{mode_name}文本: ')
        try:
            result = func(text)
            print(f'\n{mode_name}结果:\n{result}')
        except Exception as e:
            print(f'错误: {e}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='社会主义核心价值观编解码工具')
    parser.add_argument('-m', '--mode', choices=['encode', 'decode'], help='编码或解码模式')
    parser.add_argument('-t', '--text', help='直接处理的文本')
    parser.add_argument('-o', '--output', help='输出文件路径')

    args = parser.parse_args()

    if args.text:
        try:
            if args.mode == 'encode':
                result = encode(args.text)
            elif args.mode == 'decode':
                result = decode(args.text)
            else:
                raise ValueError('请指定模式参数 --mode')

            if args.output:
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write(result)
                print(f'结果已保存至 {args.output}')
            else:
                print(result)
        except Exception as e:
            print(f'处理错误: {e}')
    else:
        interactive_mode()