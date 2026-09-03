# -*- coding: utf-8 -*-
"""JSFuck 编码纯 Python 实现 (jsfuck_encode.js 0.4.0 算法移植)

输出与 JS 版语义一致 (可被 JS eval 还原原文), 不需要 JS 引擎。
"""
import re

_USE_CHAR_CODE = "USE_CHAR_CODE"

_JSFUCK_SIMPLE = {
    'false': '![]',
    'true': '!![]',
    'undefined': '[][[]]',
    'NaN': '+[![]]',
    'Infinity': '+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]+[+!+[]]+[+[]]+[+[]]+[+[]])',
}

_JSFUCK_CONSTRUCTORS = {
    'Array': '[]',
    'Number': '(+[])',
    'String': '([]+[])',
    'Boolean': '(![])',
    'Function': '[]["fill"]',
    'RegExp': 'Function("return/"+false+"/")()',
}

_JSFUCK_MAPPING = {
    'a': '(false+"")[1]', 'b': '([]["entries"]()+"")[2]', 'c': '([]["fill"]+"")[3]',
    'd': '(undefined+"")[2]', 'e': '(true+"")[3]', 'f': '(false+"")[0]',
    'g': '(false+[0]+String)[20]', 'h': '(+(101))["to"+String["name"]](21)[1]',
    'i': '([false]+undefined)[10]', 'j': '([]["entries"]()+"")[3]',
    'k': '(+(20))["to"+String["name"]](21)', 'l': '(false+"")[2]',
    'm': '(Number+"")[11]', 'n': '(undefined+"")[1]', 'o': '(true+[]["fill"])[10]',
    'p': '(+(211))["to"+String["name"]](31)[1]', 'q': '(+(212))["to"+String["name"]](31)[1]',
    'r': '(true+"")[1]', 's': '(false+"")[3]', 't': '(true+"")[0]',
    'u': '(undefined+"")[0]', 'v': '(+(31))["to"+String["name"]](32)',
    'w': '(+(32))["to"+String["name"]](33)', 'x': '(+(101))["to"+String["name"]](34)[1]',
    'y': '(NaN+[Infinity])[10]', 'z': '(+(35))["to"+String["name"]](36)',
    'A': '(+[]+Array)[10]', 'B': '(+[]+Boolean)[10]',
    'C': 'Function("return escape")()(("")["italics"]())[2]',
    'D': 'Function("return escape")()([]["fill"])["slice"]("-1")',
    'E': '(RegExp+"")[12]', 'F': '(+[]+Function)[10]',
    'G': '(false+Function("return Date")()())[30]',
    'H': _USE_CHAR_CODE, 'I': '(Infinity+"")[0]',
    'J': _USE_CHAR_CODE, 'K': _USE_CHAR_CODE, 'L': _USE_CHAR_CODE,
    'M': '(true+Function("return Date")()())[30]', 'N': '(NaN+"")[0]',
    'O': '(NaN+Function("return{}")())[11]',
    'P': _USE_CHAR_CODE, 'Q': _USE_CHAR_CODE, 'R': '(+[]+RegExp)[10]',
    'S': '(+[]+String)[10]', 'T': '(NaN+Function("return Date")()())[30]',
    'U': '(NaN+Function("return{}")()["to"+String["name"]]["call"]())[11]',
    'V': _USE_CHAR_CODE, 'W': _USE_CHAR_CODE, 'X': _USE_CHAR_CODE,
    'Y': _USE_CHAR_CODE, 'Z': _USE_CHAR_CODE,
    ' ': '(NaN+[]["fill"])[11]', '!': _USE_CHAR_CODE,
    '"': '("")["fontcolor"]()[12]', '#': _USE_CHAR_CODE, '$': _USE_CHAR_CODE,
    '%': 'Function("return escape")()([]["fill"])[21]',
    '&': '("")["link"](0+")[10]', "'": _USE_CHAR_CODE,
    '(': '(undefined+[]["fill"])[22]', ')': '([0]+false+[]["fill"])[20]',
    '*': _USE_CHAR_CODE,
    '+': '(+(+!+[]+(!+[]+[])[!+[]+!+[]+!+[]]+[+!+[]]+[+[]]+[+[]])+[])[2]',
    ',': '([]["slice"]["call"](false+"")+"")[1]',
    '-': '(+(.+[0000000001])+"")[2]',
    '.': '(+(+!+[]+[+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+[!+[]+!+[]]+[+[]])+[])[+!+[]]',
    '/': '(false+[0])["italics"]()[10]', ':': '(RegExp()+"")[3]',
    ';': '("")["link"](")[14]', '<': '("")["italics"]()[0]',
    '=': '("")["fontcolor"]()[11]', '>': '("")["italics"]()[2]',
    '?': '(RegExp()+"")[2]', '@': _USE_CHAR_CODE,
    '[': '([]["entries"]()+"")[0]', '\\': _USE_CHAR_CODE,
    ']': '([]["entries"]()+"")[22]', '^': _USE_CHAR_CODE,
    '_': _USE_CHAR_CODE, '`': _USE_CHAR_CODE,
    '{': '(true+[]["fill"])[20]', '|': _USE_CHAR_CODE,
    '}': '([]["fill"]+"")["slice"]("-1")', '~': _USE_CHAR_CODE,
}

_GLOBAL = 'Function("return this")()'


def _fill_missing_chars(mapping):
    for key in mapping:
        if mapping[key] == _USE_CHAR_CODE:
            h = hex(ord(key))[2:]
            replaced = re.sub(r'(\d+)', lambda m: '+(%s)+"' % m.group(1), h)
            mapping[key] = 'Function("return unescape")()("%"' + replaced + '")'


def _fill_missing_digits(mapping):
    for number in range(10):
        output = "+[]"
        if number > 0:
            output = "+!" + output
        for _i in range(1, number):
            output = "+!+[]" + output
        if number > 1:
            output = output[1:]
        mapping[str(number)] = "[" + output + "]"


def _jsfuck_replace_map(mapping):
    """replaceMap(): 把 value 里的构造器/关键字/数字替换为 JSFuck 片段"""
    def repl(pattern, replacement, value):
        return re.sub(pattern, replacement, value, flags=re.I)

    def digit_replacer(m):
        return mapping[m.group(1)]

    def number_replacer(m):
        y = m.group(0)
        values = list(y)
        head = int(values.pop(0))
        output = "+[]"
        if head > 0:
            output = "+!" + output
        for _i in range(1, head):
            output = "+!+[]" + output
        if head > 1:
            output = output[1:]
        joined = "+".join([output] + values)
        return re.sub(r'(\d)', digit_replacer, joined)

    for i in range(32, 127):
        character = chr(i)
        value = mapping.get(character)
        if not value:
            continue
        for key, constr in _JSFUCK_CONSTRUCTORS.items():
            value = repl(r'\b' + key, constr + '["constructor"]', value)
        for key, simple in _JSFUCK_SIMPLE.items():
            value = repl(key, simple, value)
        value = repl(r'(\d\d+)', number_replacer, value)
        value = repl(r'\((\d)\)', digit_replacer, value)
        value = repl(r'\[(\d)\]', digit_replacer, value)
        value = repl("GLOBAL", _GLOBAL, value)
        value = repl(r'\+""', "+[]", value)
        value = repl('""', "[]+[]", value)
        mapping[character] = value


def _jsfuck_replace_strings(mapping):
    """replaceStrings(): 展开引号字符串为字符拼接"""
    reg_ex = re.compile(r'[^\[\]\(\)\!\+]{1}')

    def mapping_replacer(m):
        # JS: mappingReplacer(a, b) -> b.split('').join('+'), b 为捕获组1(引号内容)
        return "+".join(m.group(1))

    def find_missing():
        nonlocal_missing = {}
        done = False
        for k, v in mapping.items():
            if reg_ex.search(v):
                nonlocal_missing[k] = v
                done = True
        return done, nonlocal_missing

    count = 126 - 32
    # 先展开所有 "..." 引号字符串
    for key in mapping:
        mapping[key] = re.sub(r'"([^"]+)"', mapping_replacer, mapping[key], flags=re.I)

    while True:
        found, missing = find_missing()
        if not found:
            break
        for k in missing:
            value = mapping[k]
            value = reg_ex.sub(lambda m: mapping.get(m.group(0), m.group(0)), value)
            mapping[k] = value
            missing[k] = value
        count -= 1
        if count == 0:
            break


def _jsfuck_encode_char(c, mapping):
    if c in mapping:
        return mapping[c]
    return _jsfuck_encode_input(c, mapping, False)


def _handle_char(c, mapping):
    """单字符 → JSFuck 表达式"""
    if c in mapping:
        return mapping[c]
    # 递归构造: ([]+[])["constructor"]["fromCharCode"](code)
    replacement = (
        "([]+[])[" + _jsfuck_encode_input("constructor", mapping, False) + "]"
        "[" + _jsfuck_encode_input("fromCharCode", mapping, False) + "]"
        "(" + _jsfuck_encode_input(str(ord(c)), mapping, False) + ")"
    )
    mapping[c] = replacement
    return replacement


def _jsfuck_encode_input(input_str, mapping, wrap_with_eval=True):
    """encode(): 主编码函数 (递归)"""
    if not input_str:
        return ""
    output = []
    # SIMPLE 词 (true/false/undefined/NaN/Infinity) 和 '.' 整体匹配
    pattern = "|".join(re.escape(k) for k in _JSFUCK_SIMPLE) + r"|\."
    pos = 0
    for m in re.finditer(pattern, input_str):
        if m.start() > pos:
            for c in input_str[pos:m.start()]:
                output.append(_handle_char(c, mapping))
        word = m.group(0)
        if word in _JSFUCK_SIMPLE:
            output.append("[" + _JSFUCK_SIMPLE[word] + "]+[]")
        else:  # '.'
            output.append(_handle_char(".", mapping))
        pos = m.end()
    if pos < len(input_str):
        for c in input_str[pos:]:
            output.append(_handle_char(c, mapping))

    out = "+".join(output)

    if re.fullmatch(r'\d', input_str or ""):
        out += "+[]"

    if wrap_with_eval:
        # JS 原版 (runInParentScope=false 分支):
        #   []["<fill>"]["<constructor>"](<code字符串>)  => new Function(code)
        # eval 后得到以 code 为函数体的 Function, 而非立即执行
        out = (
            "[][" + _jsfuck_encode_input("fill", mapping, False) + "]"
            "[" + _jsfuck_encode_input("constructor", mapping, False) + "]"
            "(" + out + ")"
        )
    return out


def jsfuck_encode(source_text: str) -> str:
    """JSFuck 编码 (输出与 jsfuck_encode.js 语义一致, 可被 JS eval 还原)"""
    mapping = dict(_JSFUCK_MAPPING)
    _fill_missing_digits(mapping)
    _fill_missing_chars(mapping)
    _jsfuck_replace_map(mapping)
    _jsfuck_replace_strings(mapping)
    return _jsfuck_encode_input(source_text, mapping, True)
