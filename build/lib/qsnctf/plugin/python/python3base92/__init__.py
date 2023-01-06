# THE BEERWARE LICENSE (Revision 42):
# <thenoviceoof> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you
# think this stuff is worth it, you can buy me a beer in return
# - Nathan Hwang (thenoviceoof)

# 起因：CTF及一些问题中需要用到base92做加解码，苦于未找到python3版本，因此基于python2版本做代码兼容，仅做学习交流，请支持原作者
# 增加：支持python3
# 在原作者的基础上修改部分代码使其支持python3的运行
# 已知BUG：部分不可见字符及中文无法通过样例，暂时无做进一步修正打算，因为base92使用场景中大多数情况可以满足
# 如果有更好提议欢迎提出
# By Gu-f

'''
base92: a library for encoding byte strings

>>> x = encode('hello world')
>>> x
'Fc_$aOTdKnsM*k'
>>> decode(x)
'hello world'

>>> y = encode('^\xb6;\xbb\xe0\x1e\xee\xd0\x93\xcb"\xbb\x8fZ\xcd\xc3')
>>> y
"C=i.w6'IvB/viUpRAwco"
>>> decode(y)
'^\\xb6;\\xbb\\xe0\\x1e\\xee\\xd0\\x93\\xcb"\\xbb\\x8fZ\\xcd\\xc3'

this is a regression test
>>> decode(encode('aoeuaoeuaoeu'))
'aoeuaoeuaoeu'
'''

import math

__version__ = (1, 0, '3-1')


def base92_chr(val):
    '''
    Map an integer value <91 to a char

    >>> base92_chr(0)
    '!'
    >>> base92_chr(1)
    '#'
    >>> base92_chr(61)
    '_'
    >>> base92_chr(62)
    'a'
    >>> base92_chr(90)
    '}'
    >>> base92_chr(91)
    Traceback (most recent call last):
        ...
    ValueError: val must be in [0, 91)
    '''
    if val < 0 or val >= 91:
        raise ValueError('val must be in [0, 91)')
    if val == 0:
        return '!'
    elif val <= 61:
        return chr(ord('#') + val - 1)
    else:
        return chr(ord('a') + val - 62)


def base92_ord(val):
    '''
    Map a char to an integer

    >>> base92_ord('!')
    0
    >>> base92_ord('#')
    1
    >>> base92_ord('_')
    61
    >>> base92_ord('a')
    62
    >>> base92_ord('}')
    90
    >>> base92_ord(' ')
    Traceback (most recent call last):
        ...
    ValueError: val is not a base92 character
    '''
    num = ord(val)
    if val == '!':
        return 0
    elif ord('#') <= num and num <= ord('_'):
        return num - ord('#') + 1
    elif ord('a') <= num and num <= ord('}'):
        return num - ord('a') + 62
    else:
        raise ValueError('val is not a base92 character')


def base92_encode(bytstr):
    '''
    Take a byte-string, and encode it in base 91

    >>> base92_encode("")
    '~'
    >>> base92_encode("\\x00")
    '!!'
    >>> base92_encode("\x01")
    '!B'
    >>> base92_encode("\xff")
    '|_'
    >>> base92_encode("aa")
    'D8*'
    >>> base92_encode("aaaaaaaaaaaaa")
    'D81RPya.)hgNA(%s'
    >>> base92_encode([16,32,48])
    "'_$,"
    '''
    # always encode *something*, in case we need to avoid empty strings
    if not bytstr:
        return '~'
    # make sure we have a bytstr
    # if (not isinstance(bytstr, str)) or (not isinstance(bytstr, bytes)):
    if not isinstance(bytstr, str):
        # we'll assume it's a sequence of ints
        bytstr = ''.join([chr(b) for b in bytstr])
    # prime the pump
    bitstr = ''
    while len(bitstr) < 13 and bytstr:
        bitstr += '{:08b}'.format(ord(bytstr[0]))
        bytstr = bytstr[1:]
    resstr = ''
    while len(bitstr) > 13 or bytstr:
        i = int(bitstr[:13], 2)
        resstr += base92_chr(i // 91)
        resstr += base92_chr(i % 91)
        bitstr = bitstr[13:]
        while len(bitstr) < 13 and bytstr:
            bitstr += '{:08b}'.format(ord(bytstr[0]))
            bytstr = bytstr[1:]
    if bitstr:
        if len(bitstr) < 7:
            bitstr += '0' * (6 - len(bitstr))
            resstr += base92_chr(int(bitstr, 2))
        else:
            bitstr += '0' * (13 - len(bitstr))
            i = int(bitstr, 2)
            resstr += base92_chr(i // 91)
            resstr += base92_chr(i % 91)
    return resstr.replace('\\', '\\\\')


def base92_decode(bstr):
    '''
    Take a base92 encoded string, convert it back to a byte-string

    >>> base92_decode("")
    ''
    >>> base92_decode("~")
    ''
    >>> base92_decode("!!")
    '\\x00'
    >>> base92_decode("!B")
    '\\x01'
    >>> base92_decode("|_")
    '\\xff'
    >>> base92_decode("D8*")
    'aa'
    >>> base92_decode("D81RPya.)hgNA(%s")
    'aaaaaaaaaaaaa'
    '''
    bitstr = ''
    resstr = ''
    if bstr == '~':
        return ''
    # we always have pairs of characters
    for i in range(len(bstr) // 2):
        x = base92_ord(bstr[2 * i]) * 91 + base92_ord(bstr[2 * i + 1])
        bitstr += '{:013b}'.format(x)
        while 8 <= len(bitstr):
            resstr += chr(int(bitstr[0:8], 2))
            bitstr = bitstr[8:]
    # if we have an extra char, check for extras
    if len(bstr) % 2 == 1:
        x = base92_ord(bstr[-1])
        bitstr += '{:06b}'.format(x)
        while 8 <= len(bitstr):
            resstr += chr(int(bitstr[0:8], 2))
            bitstr = bitstr[8:]
    return resstr


encode = base92_encode
b92encode = base92_encode

decode = base92_decode
b92decode = base92_decode

##该样例通过率100%
if __name__ == '__main__':
    import random

    sum = 0
    for i in range(10000):
        randoms = random.randint(0, 92)
        strs = ''.join(random.sample(
            [' ', '!', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5',
             '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', '{', '|', '}'], randoms))
        # print(type(strs))
        result = encode(strs)
        # print(result)
        result2 = base92_decode(result.replace('\\\\', '\\'))
        # print(result2)
        if strs == result2:
            # print("pass")
            sum += 1
    print("testNum:10000, pass:" + str(sum))

##该样例通过率约为8%
# if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
#
#    ## more correctness tests
#    import hashlib
#    import random
#    def gen_bytes(s):
#        return hashlib.sha512(s).digest()[:random.randint(1,64)]
#    sum=0
#    for i in range(10000):
#        s = gen_bytes(str(random.random()).encode())
#        if type(s)==type(b'aa'):
#            result=encode(s)
#            #print(result)
#            result2=base92_decode(result.replace('\\\\','\\'))
#            #print(result2)
#            if s!=result2.encode():
#                #print("error")
#                sum+=1
#        else:
#            result=encode(s)
#            #print(result)
#            result2=base92_decode(result.replace('\\\\','\\'))
#            #print(result2)
#            if s!=result2:
#                #print("error")
#                sum+=1
#    print(sum)
