# 🤔What is QSNCTF？

[青少年CTF训练平台](https://www.qsnctf.com/)是一个公益、免费、供给全国青少年学习、训练的CTF在线平台。

[（本仓库）](https://github.com/Moxin1044/qsnctf-python)qsnctf is a Python package program written by the youth CTF training platform, which intends to quickly use some common CTF functions in Python to develop an open source package. There are many common CTF functions, such as Base encoding, hash encryption, and even the rare socialist core values encoding, quipqiup, etc. are among them.

## Installation

First download the project on GitHub, and once you have it, you can have a `setup.py` in the file

Open Terminal and enter

```bash
python setup.py install
```

Or you can also use pip directly to install**(since this Python library is still under development, pip may not be the latest version, if you have high needs, you can directly clone this repository to install)**

```bash
pip install qsnctf
```

You can also use the following command to update this library

```bash
pip install --upgrade qsnctf
```

A successful installation is displayed

`Successfully installed PyExecJS-1.5.1 qsnctf-0.0.4`

If you want to know exactly how to use this package to import, you can use `help(qsnctf)` to see how to use the library

```bash
>>> import qsnctf
>>> help(qsnctf)
Help on package qsnctf:

NAME
    qsnctf

PACKAGE CONTENTS
    base
    crypto
    hash
    main
    misc
    uuid

FILE
    c:\users\xiniyi\appdata\local\programs\python\python39\lib\site-packages\qsnctf-0.0.4-py3.9.egg\qsnctf\__init__.py
```

Then use `help(qsnctf. PACKAGE CONTENTS)` TO SEE HOW TO USE IT

## DEMO

See how to use `base`

```bash
>>> help(qsnctf.base)              
Help on module qsnctf.base in qsnct
                                   
NAME                               
    qsnctf.base                    
                                   
DESCRIPTION                        
    # Base编码解码功能                   
    # 2023年1月1日                    
    # 末心                           
                                   
FUNCTIONS                          
    base16_decode(text)            
                                   
    base16_encode(text)            
                                   
    base32_decode(text)            
                                   
    base32_encode(text)            
                                   
    base64_decode(text)            
                                   
    base64_encode(text)            
                                   
    base85_decode(text)
>>>
```


# List of features

### BASE

| base16 | base32 | base36 | base58 | base62  |
| :----: | :----: | :----: | :----: | :-----: |
| base64 | base85 | base91 | base92 | base100 |

### CRYPTO

| Caesar Code | Caesar blasts | Bacon password | ROT5 | ROT13 |
| :---------: | :-----------: | :------------: | :--: | :---: |
|    ROT18    |               |                |      |       |

### MD5

|   md5    |   sha1   |  sha224  |   sha256    |  sha384  |
| :------: | :------: | :------: | :---------: | :------: |
|  sha512  | shake128 | shake256 | HMAC-SHA256 | sha3-224 |
| sha3-256 | sha3-385 | sha3-512 |             |          |



### MISC

| Core values Encryption and decryption | Text reverses | URL encryption and decryption | Bit XOR |
| :-----------------------------------: | :-----------: | :---------------------------: | :-----: |

### UUID

| Get the UUID |
| :----------: |

### API

| Quipqiup word frequency analysis | Feishu Webhook|
| :--------------: | ----------- |
### WEB

| Directory scanning |
| -------- |



# Specific use

## Command line use

The first step is to import the `qsnctf` library

```python
import qsnctf
```

For example, `base64` encryption is required

```python
qsnctf.base.base64_encode("需要加密的")
```

Same if decryption is used with `base64`

```python
qsnctf.base.base64_decode("需要解密的")
```

**Other encryption encryption is similar**

------

## Compiler use

Here again base64 is used for demonstration

**Other encryption and decryption are similar.**

```python
import qsnctf

a=qsnctf.base.base64_encode("需要加密的")
print(a)
b=qsnctf.base.base64_decode("6ZyA6KaB5Yqg5a+G55qE")
print(b)
```

`Returns information`

```
6ZyA6KaB5Yqg5a+G55qE
需要加密的
```

**Hint: Bitwise or passing parameters need to be passed into a list, here is an example**

```python
import qsnctf
l=[0x71,0x72,0x6c,0x60,0x70,0x63,0x7d,0x4a,0x38,0x71,0x3b,0x65,0x53,0x41,0x61,0x79,0x75,0x4e,0x6b,0x7c,0x61,0x34,0x6b]
a=qsnctf.misc.xor_decrypt(l)
print(a)
```

Returns the results

```
qsnctf{M0X1n_Love_you!}
```

**Base62's encode value should be an integer! **

```python
import qsnctf

a = qsnctf.base.base62_encode(34441886726)
print(a)
b = qsnctf.base.base62_decode("base62")
print(b)
```

## Parameter passing method

Since there are many bases and various encryption methods, there are also many ways to pass parameters. Here is to write this document for you for easy reference, the following is the call example and parameter parameters description and precautions.

### quipqiup

#### class-quipqiup

##### quipqiup

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|        quipqiup        | string、json、list  |       api.py       | quipqiup word frequency analysis (internet connection required) |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|       ciphertext       |        False        |       string       |                       What is analyzed                       |
|         clues          |        True         |       string       |  Analysis clues, empty by default, For example G=R QVW=THE   |

**illustrate：This feature requires an internet connection, please pay attention to the rules of the contest to use.**

##### Use examples

```python
from qsnctf import *

a = quipqiup('test')
print(a.text) # that,high,area,died***
print(a.json) # {'id': 931788518, 'result': 0, 'result-message': 'success', 'time0': 1672662393.35963, 'last': 1, 'solutions': [{'logp': -1.58357763290405, 'plaintext': 'that', ***
print(a.list) # ['that', 'high',***
```

### The Base family

#### Base100

##### base100_encode

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|     base100_encode     |       string        |      base.py       |              Base100 encoding(Support Chinese)               |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|          text          |        False        |       string       |                   What needs to be encoded                   |
|        encoding        |        True         |       string       | The encoding when decoding text, the default value is UTF-8  |
|        decoding        |        True         |       string       | The encoding when exporting text, the default value is UTF-8 |

##### base100_decode

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|     base100_decode     |       string        |      base.py       |                      Base100 decodeing                       |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|          text          |        False        |       string       |                   What needs to be decoded                   |
|        encoding        |        True         |       string       | The encoding when decoding text, the default value is UTF-8  |
|        decoding        |        True         |       string       | The encoding when exporting text, the default value is UTF-8 |

##### Use examples

```python
from qsnctf import *

# 因为在__init__.py已经引用了，所以不需要再base.base100_encode('xxx'),下同
a = base100_encode('青少年CTF')
print(a) # 📠💔💉📜💧💈📜💰💫🐺👋🐽
a = base100_decode('📠💔💉📜💧💈📜💰💫🐺👋🐽')
print(a) # 青少年CTF
```

#### Base92

##### base92_encode

|   **Function name**    |   **Return type**   |    **location**    |                 **illustrate**                 |
| :--------------------: | :-----------------: | :----------------: | :--------------------------------------------: |
|     base92_encode      |       string        |      base.py       | Base92 encoding (cannot be encoded Chinese oh) |
| **The parameter name** | **Nullable or not** | **Parameter type** |                 **illustrate**                 |
|          text          |        False        |       string       |            What needs to be encoded            |

##### base92_decode

|   **Function name**    |   **Return type**   |    **location**    |      **illustrate**      |
| :--------------------: | :-----------------: | :----------------: | :----------------------: |
|     base92_decode      |       string        |      base.py       |     Base92 decoding      |
| **The parameter name** | **Nullable or not** | **Parameter type** |      **illustrate**      |
|          text          |        False        |       string       | What needs to be decoded |

##### Use examples

```python
from qsnctf import *


a = base92_encode('qsnctf123QSN')
print(a) # ItHYSr3{(eF*?n>
a = base92_decode('ItHYSr3{(eF*?n>')
print(a) # qsnctf123QSN
```

#### Base91

##### base91_encode

|   **Function name**    |   **Return type**   |    **location**    |           **illustrate**            |
| :--------------------: | :-----------------: | :----------------: | :---------------------------------: |
|     base91_encode      |       string        |      base.py       | Base91 encoding (supported Chinese) |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**            |
|          text          |        False        |       string       |      What needs to be encoded       |

##### base91_decode

|   **Function name**    |   **Return type**   |    **location**    |      **illustrate**      |
| :--------------------: | :-----------------: | :----------------: | :----------------------: |
|     base91_decode      |       string        |      base.py       |     Base91 decoding      |
| **The parameter name** | **Nullable or not** | **Parameter type** |      **illustrate**      |
|          text          |        False        |       string       | What needs to be decoded |

##### Use examples

```python
from qsnctf import *


a = base91_encode('青少年CTF')
print(a) # N_jjjief!gTFU,I
a = base91_decode('N_jjjief!gTFU,I')
print(a) # 青少年CTF
```

#### Base85

##### base85_encode

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|     base85_encode      |       string        |      base.py       |             Base85 encoding (supported Chinese)              |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|          text          |        False        |       string       |                   What needs to be encoded                   |
|        encoding        |        True         |       string       | The encoding when decoding text, the default value is UTF-8  |
|        decoding        |        True         |       string       | The encoding when exporting text, the default value is UTF-8 |

##### base85_decode

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|     base85_decode      |       string        |      base.py       |                       Base85 decoding                        |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|          text          |        False        |       string       |                   What needs to be decoded                   |
|        encoding        |        True         |       string       | The encoding when decoding text, the default value is UTF-8  |
|        decoding        |        True         |       string       | The encoding when exporting text, the default value is UTF-8 |

##### Use examples

```python
from qsnctf import *


a = base85_encode('青少年CTF')
print(a) # >7A10u#x4tv_n)z
a = base85_decode('>7A10u#x4tv_n)z')
print(a) # 青少年CTF
```

#### Base64

##### base64_encode

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|     base64_encode      |       string        |      base.py       |             Base64 encoding (supported Chinese)              |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|          text          |        False        |       string       |                   What needs to be encoded                   |
|        encoding        |        True         |       string       | The encoding when decoding text, the default value is UTF-8  |
|        decoding        |        True         |       string       | The encoding when exporting text, the default value is UTF-8 |

##### base64_decode

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|     base64_decode      |       string        |      base.py       |                       Base64 decoding                        |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|          text          |        False        |       string       |                   What needs to be decoded                   |
|        encoding        |        True         |       string       | The encoding when decoding text, the default value is UTF-8  |
|        decoding        |        True         |       string       | The encoding when exporting text, the default value is UTF-8 |

##### Use examples

```python
from qsnctf import *


a = base64_encode('青少年CTF')
print(a) # 6Z2S5bCR5bm0Q1RG
a = base64_decode('6Z2S5bCR5bm0Q1RG')
print(a) # 青少年CTF
```

#### Base62

##### base62_encode

|   **Function name**    |   **Return type**   |    **location**    |             **illustrate**             |
| :--------------------: | :-----------------: | :----------------: | :------------------------------------: |
|     base62_encode      |     **string**      |      base.py       | Base62 encoding (can only be integers) |
| **The parameter name** | **Nullable or not** | **Parameter type** |             **illustrate**             |
|          ints          |        False        |      **int**       |        What needs to be encoded        |

##### base62_decode

|   **Function name**    |   **Return type**   |    **location**    |      **illustrate**      |
| :--------------------: | :-----------------: | :----------------: | :----------------------: |
|     base62_decode      |       **int**       |      base.py       |     Base62 decoding      |
| **The parameter name** | **Nullable or not** | **Parameter type** |      **illustrate**      |
|          text          |        False        |       string       | What needs to be decoded |

##### Use examples

```python
from qsnctf import *


a = base62_encode(123456)
print(a) # W7E
a = base62_decode('W7E')
print(a) # 123456
```

#### Base58

##### base58_encode

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|     base58_encode      |       string        |      base.py       |             Base58 encoding (supported Chinese)              |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|          text          |        False        |       string       |                   What needs to be encoded                   |
|        encoding        |        True         |       string       | The encoding when decoding text, the default value is UTF-8  |
|        decoding        |        True         |       string       | The encoding when exporting text, the default value is UTF-8 |

##### base58_decode

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|     base58_decode      |       string        |      base.py       |                       Base58 decoding                        |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|          text          |        False        |       string       |                   What needs to be decoded                   |
|        encoding        |        True         |       string       | The encoding when decoding text, the default value is UTF-8  |
|        decoding        |        True         |       string       | The encoding when exporting text, the default value is UTF-8 |

##### Use examples

```python
from qsnctf import *


a = base58_encode('青少年CTF')
print(a) # 5QhHM9SSxYiJbYQMj
a = base58_decode('5QhHM9SSxYiJbYQMj')
print(a) # 青少年CTF
```

#### Base36

##### base36_encode

|   **Function name**    |   **Return type**   |    **location**    |             **illustrate**             |
| :--------------------: | :-----------------: | :----------------: | :------------------------------------: |
|     base36_encode      |     **string**      |      base.py       | Base36 encoding (can only be integers) |
| **The parameter name** | **Nullable or not** | **Parameter type** |             **illustrate**             |
|        encoded         |        False        |      **int**       |        What needs to be encoded        |

##### base36_decode

|   **Function name**    |   **Return type**   |    **location**    |      **illustrate**      |
| :--------------------: | :-----------------: | :----------------: | :----------------------: |
|     base36_decode      |       **int**       |      base.py       |     Base36 decoding      |
| **The parameter name** | **Nullable or not** | **Parameter type** |      **illustrate**      |
|          text          |        False        |       string       | What needs to be decoded |

##### Use examples

```python
from qsnctf import *


a = base36_encode(123456)
print(a) # 2n9c
a = base36_decode('2n9c')
print(a) # 123456
```

#### Base32

##### base32_encode

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|     base32_encode      |       string        |      base.py       |             Base32 encoding (supported Chinese)              |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|          text          |        False        |       string       |                   What needs to be encoded                   |
|        encoding        |        True         |       string       | The encoding when decoding text, the default value is UTF-8  |
|        decoding        |        True         |       string       | The encoding when exporting text, the default value is UTF-8 |

##### base32_decode

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|     base32_decode      |       string        |      base.py       |                       Base32 decoding                        |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|          text          |        False        |       string       |                   What needs to be decoded                   |
|        encoding        |        True         |       string       | The encoding when decoding text, the default value is UTF-8  |
|        decoding        |        True         |       string       | The encoding when exporting text, the default value is UTF-8 |

##### Use examples

```python
from qsnctf import *


a = base32_encode('青少年CTF')
print(a) # 5GOZFZNQSHS3TNCDKRDA====
a = base32_decode('5GOZFZNQSHS3TNCDKRDA====')
print(a) # 青少年CTF
```

#### Base16

##### base16_encode

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|     base16_encode      |       string        |      base.py       |             base16 encoding (supported Chinese)              |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|          text          |        False        |       string       |                   What needs to be encoded                   |
|        encoding        |        True         |       string       | The encoding when decoding text, the default value is UTF-8  |
|        decoding        |        True         |       string       | The encoding when exporting text, the default value is UTF-8 |

##### base16_decode

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|     base16_decode      |       string        |      base.py       |                       base16 decoding                        |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|          text          |        False        |       string       |                   What needs to be decoded                   |
|        encoding        |        True         |       string       | The encoding when decoding text, the default value is UTF-8  |
|        decoding        |        True         |       string       | The encoding when exporting text, the default value is UTF-8 |

##### Use examples

```python
from qsnctf import *


a = base16_encode('青少年CTF')
print(a) # E99D92E5B091E5B9B4435446
a = base16_decode('E99D92E5B091E5B9B4435446')
print(a) # 青少年CTF
```

### 各种编码

#### 核心价值观

##### Chinese_socialism_encode

|    **Function name**     |   **Return type**   |    **location**    |         **illustrate**          |
| :----------------------: | :-----------------: | :----------------: | :-----------------------------: |
| Chinese_socialism_encode |       string        |      misc.py       | Coding of socialist core values |
|  **The parameter name**  | **Nullable or not** | **Parameter type** |         **illustrate**          |
|          string          |        False        |       string       |    What needs to be encoded     |

##### Chinese_socialism_decode

|    **Function name**     |   **Return type**   |    **location**    |          **illustrate**           |
| :----------------------: | :-----------------: | :----------------: | :-------------------------------: |
| Chinese_socialism_decode |       string        |      misc.py       | Decoding of socialist core values |
|  **The parameter name**  | **Nullable or not** | **Parameter type** |          **illustrate**           |
|          string          |        False        |       string       |     What needs to be decoded      |

##### Use examples

```python
from qsnctf import *


a = Chinese_socialism_encode('青少年CTF')
print(a) # 友善爱国敬业敬业诚信和谐敬业文明友善爱国平等诚信民主富强敬业民主友善爱国平等友善平等敬业诚信民主自由自由和谐平等自由自由公正
a = Chinese_socialism_decode('友善爱国敬业敬业诚信和谐敬业文明友善爱国平等诚信民主富强敬业民主友善爱国平等友善平等敬业诚信民主自由自由和谐平等自由自由公正')
print(a) # 青少年CTF
```

#### URL编码

##### url_encode

|   **Function name**    |   **Return type**   |    **location**    |      **illustrate**      |
| :--------------------: | :-----------------: | :----------------: | :----------------------: |
|       url_encode       |       string        |      misc.py       |       URL encoding       |
| **The parameter name** | **Nullable or not** | **Parameter type** |      **illustrate**      |
|         string         |        False        |       string       | What needs to be encoded |

##### url_decode

|   **Function name**    |   **Return type**   |    **location**    |      **illustrate**      |
| :--------------------: | :-----------------: | :----------------: | :----------------------: |
|       url_decode       |       string        |      misc.py       |       URL decoding       |
| **The parameter name** | **Nullable or not** | **Parameter type** |      **illustrate**      |
|         string         |        False        |       string       | What needs to be decoded |

##### Use examples

```python
from qsnctf import *


a = url_encode('青少年CTF=中学生CTF')
print(a) # %E9%9D%92%E5%B0%91%E5%B9%B4CTF%3D%E4%B8%AD%E5%AD%A6%E7%94%9FCTF
a = url_decode('%E9%9D%92%E5%B0%91%E5%B9%B4CTF%3D%E4%B8%AD%E5%AD%A6%E7%94%9FCTF')
print(a) # 青少年CTF=中学生CTF
```

### 

### 字符串操作

#### 逆向字符串

##### string_reverse

|   **Function name**    |   **Return type**   |    **location**    |                **illustrate**                |
| :--------------------: | :-----------------: | :----------------: | :------------------------------------------: |
|     string_reverse     |       string        |      misc.py       | Reverse strings, strings reverse order, flip |
| **The parameter name** | **Nullable or not** | **Parameter type** |                **illustrate**                |
|         string         |        False        |       string       |      Content that needs to be reversed       |

##### Use examples

```python
from qsnctf import *


a = string_reverse('青少年CTF')
print(a) # FTC年少青
```

#### 列表异或

##### xor_list

|   **Function name**    |   **Return type**   |    **location**    | **illustrate** |
| :--------------------: | :-----------------: | :----------------: | :------------: |
|        xor_list        |       string        |      misc.py       |      xor       |
| **The parameter name** | **Nullable or not** | **Parameter type** | **illustrate** |
|        lt_data         |        False        |        list        |    XOR data    |
|        lt_root         |        False        |        list        |   XOROR root   |

##### Use examples

```python
from qsnctf import *

a = "abcde" # 因为string在Python中来说可以当做列表来截取，所以可以直接这样传
b = "01234"
c = xor_list(a, b)
print(c) # QSQWQ
```

### 

### 密码学

#### 凯撒密码

##### caesar_encrypt

|   **Function name**    |   **Return type**   |    **location**    |                **illustrate**                 |
| :--------------------: | :-----------------: | :----------------: | :-------------------------------------------: |
|     caesar_encrypt     |       string        |     crypto.py      |          Caesar password encryption           |
| **The parameter name** | **Nullable or not** | **Parameter type** |                **illustrate**                 |
|          text          |        False        |       string       |      Content that needs to be encrypted       |
|         shift          |        False        |   int or string    | The offset, passed in as string, converts int |

##### caesar_decrypt

|   **Function name**    |   **Return type**   |    **location**    |                **illustrate**                 |
| :--------------------: | :-----------------: | :----------------: | :-------------------------------------------: |
|     caesar_decrypt     |       string        |     crypto.py      |            Caesar code decryption             |
| **The parameter name** | **Nullable or not** | **Parameter type** |                **illustrate**                 |
|         string         |        False        |       string       |          What needs to be decrypted           |
|         shift          |        False        |   int or string    | The offset, passed in as string, converts int |

##### Use examples

```python
from qsnctf import *

a = caesar_encrypt('qsnctf', 8)
print(a) # yavkbn
b = caesar_decrypt('yavkbn', 8)
print(b) # qsnctf
```

#### 凯撒密码爆破

##### caesar_decrypt_cracking

|    **Function name**    |   **Return type**   |    **location**    |           **illustrate**           |
| :---------------------: | :-----------------: | :----------------: | :--------------------------------: |
| caesar_decrypt_cracking |        json         |     crypto.py      |    Caesar Code decryption blast    |
| **The parameter name**  | **Nullable or not** | **Parameter type** |           **illustrate**           |
|       ciphertext        |        False        |       string       | Content that needs to be encrypted |

##### caesar_encrypt_cracking

|    **Function name**    |   **Return type**   |    **location**    |           **illustrate**           |
| :---------------------: | :-----------------: | :----------------: | :--------------------------------: |
| caesar_encrypt_cracking |        json         |     crypto.py      |    Caesar Code Encryption Blast    |
| **The parameter name**  | **Nullable or not** | **Parameter type** |           **illustrate**           |
|       ciphertext        |        False        |       string       | Content that needs to be encrypted |

##### Use examples

```python
from qsnctf import *

a = caesar_encrypt_cracking('qsnctf')
print(a) # {"1": "rtodug", "2": "supevh", "3": "tvqfwi", "4": "uwrgxj", "5": "vxshyk", "6": "wytizl", "7": "xzujam", "8": "yavkbn", "9": "zbwlco", "10": "acxmdp", "11": "bdyneq", "12": "cezofr", "13": "dfapgs", "14": "egbqht", "15": "fhcriu", "16": "gidsjv", "17": "hjetkw", "18": "ikfulx", "19": "jlgvmy", "20": "kmhwnz", "21": "lnixoa", "22": "mojypb", "23": "npkzqc", "24": "oqlard", "25": "prmbse"}

b = caesar_decrypt_cracking('yavkbn')
print(b) # {"1": "xzujam", "2": "wytizl", "3": "vxshyk", "4": "uwrgxj", "5": "tvqfwi", "6": "supevh", "7": "rtodug", "8": "qsnctf", "9": "prmbse", "10": "oqlard", "11": "npkzqc", "12": "mojypb", "13": "lnixoa", "14": "kmhwnz", "15": "jlgvmy", "16": "ikfulx", "17": "hjetkw", "18": "gidsjv", "19": "fhcriu", "20": "egbqht", "21": "dfapgs", "22": "cezofr", "23": "bdyneq", "24": "acxmdp", "25": "zbwlco"}

```

**Note: The final return of encryption blasting and decryption blasting is json, the two sets are completely different, and crypto blasting is written with off-topic points in mind, so don't confuse them.**

#### Bacon password

##### bacon_encrypt

|   **Function name**    |   **Return type**   |    **location**    |           **illustrate**           |
| :--------------------: | :-----------------: | :----------------: | :--------------------------------: |
|     bacon_encrypt      |       string        |     crypto.py      |     Bacon password encryption      |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**           |
|         string         |        False        |       string       | Content that needs to be encrypted |

##### bacon_decrypt

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|     bacon_decrypt      |       string        |     crypto.py      |                  Bacon password decryption                   |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|         string         |        False        |       string       | What needs to be decrypted, if it appears lowercase must be converted to uppercase |

##### Use examples

```python
from qsnctf import *

a = bacon_encrypt('qsnctf')
print(a) # BAAAABAABAABBABAAABABAABBAABAB
b = bacon_decrypt('BAAAABAABAABBABAAABABAABBAABAB')
print(b) # QSNCTF
```

#### ROT13

##### rot13

|   **Function name**    |   **Return type**   |    **location**    |                 **illustrate**                  |
| :--------------------: | :-----------------: | :----------------: | :---------------------------------------------: |
|         rot13          |       string        |     crypto.py      |                      rot13                      |
| **The parameter name** | **Nullable or not** | **Parameter type** |                 **illustrate**                  |
|          text          |        False        |       string       | Content that needs to be encrypted or decrypted |

##### Use examples

```python
from qsnctf import *

a = rot13('qsnctf')
print(a) # dfapgs
b = rot13('dfapgs')
print(b) # qsnctf
```

#### ROT5

##### rot5

|   **Function name**    |   **Return type**   |    **location**    |                 **illustrate**                  |
| :--------------------: | :-----------------: | :----------------: | :---------------------------------------------: |
|          rot5          |       string        |     crypto.py      |                      rot5                       |
| **The parameter name** | **Nullable or not** | **Parameter type** |                 **illustrate**                  |
|          text          |        False        |       string       | Content that needs to be encrypted or decrypted |

##### Use examples

```python
from qsnctf import *

a = rot5('12345')
print(a) # 6789021
b = rot5('67890')
print(b) # 12345
```

#### ROT18

##### rot18

|   **Function name**    |   **Return type**   |    **location**    |                 **illustrate**                  |
| :--------------------: | :-----------------: | :----------------: | :---------------------------------------------: |
|         rot18          |       string        |     crypto.py      |                      rot18                      |
| **The parameter name** | **Nullable or not** | **Parameter type** |                 **illustrate**                  |
|          text          |        False        |       string       | Content that needs to be encrypted or decrypted |

##### Use examples

```python
from qsnctf import *

a = rot18('qsnctf2022')
print(a) # dfapgs7577
b = rot18('dfapgs7577')
print(b) # qsnctf2022
```

### Hash

#### MD5

##### md5

|   **Function name**    |   **Return type**   |    **location**    |           **illustrate**           |
| :--------------------: | :-----------------: | :----------------: | :--------------------------------: |
|          md5           |       string        |      hash.py       |                md5                 |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**           |
|      input_string      |        False        |       string       | Content that needs to be encrypted |

##### Use examples

```python
from qsnctf import *

a = md5('qsnctf2022')
print(a) # cede1574f851cb8a1ffb3c1b885c4965
```

#### SHA1

##### sha1

|   **Function name**    |   **Return type**   |    **location**    |           **illustrate**           |
| :--------------------: | :-----------------: | :----------------: | :--------------------------------: |
|          sha1          |       string        |      hash.py       |                sha1                |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**           |
|      input_string      |        False        |       string       | Content that needs to be encrypted |

##### Use examples

```python
from qsnctf import *

a = sha1('qsnctf2022')
print(a) # 5a66dd2590a911dc670873e12934e6f14d1da7e7
```



#### SHA224

##### sha224

|   **Function name**    |   **Return type**   |    **location**    |           **illustrate**           |
| :--------------------: | :-----------------: | :----------------: | :--------------------------------: |
|         sha224         |       string        |      hash.py       |               sha224               |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**           |
|      input_string      |        False        |       string       | Content that needs to be encrypted |

##### Use examples

```python
from qsnctf import *

a = sha224('qsnctf2022')
print(a) # 71e718c88621bfe602833420a817398aee52df7ef9c1904086c9ff8f
```



#### SHA256

##### sha256

|   **Function name**    |   **Return type**   |    **location**    |           **illustrate**           |
| :--------------------: | :-----------------: | :----------------: | :--------------------------------: |
|         sha256         |       string        |      hash.py       |               sha256               |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**           |
|      input_string      |        False        |       string       | Content that needs to be encrypted |

##### Use examples

```python
from qsnctf import *

a = sha256('qsnctf2022')
print(a) # 7404bb484d7a4a1f26bf974dc1337d778162d32be0d54f2e571f4e942673b7d1
```

#### SHA384

##### sha384

|   **Function name**    |   **Return type**   |    **location**    |           **illustrate**           |
| :--------------------: | :-----------------: | :----------------: | :--------------------------------: |
|         sha384         |       string        |      hash.py       |               sha384               |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**           |
|      input_string      |        False        |       string       | Content that needs to be encrypted |

##### Use examples

```python
from qsnctf import *

a = sha384('qsnctf2022')
print(a) # c692736bfeccbaa1e7f1fff9e351d67f042e5198ae8850401be46450b479f62d78e44f46300b13f5419eb5bf1fa0c222
```

#### SHA512

##### sha512

|   **Function name**    |   **Return type**   |    **location**    |           **illustrate**           |
| :--------------------: | :-----------------: | :----------------: | :--------------------------------: |
|         sha512         |       string        |      hash.py       |               sha512               |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**           |
|      input_string      |        False        |       string       | Content that needs to be encrypted |

##### Use examples

```python
from qsnctf import *

a = sha512('qsnctf2022')
print(a) # bfb5c9d6c5197696c251fad40932da2dfd3af627bf974b09a98c02b55301e58a8f6f0518b74b05a19f7f9f90340a0b81d76e7cc37802406392ebf0f0073c5301 
```

#### SHAKE128

##### shake128

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|       shake_128        |       string        |      hash.py       |                           shake128                           |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|      input_string      |        False        |       string       |              Content that needs to be encrypted              |
|          bits          |        False        |   int or string    | Used to specify the length of the hash value for the output. |

##### Use examples

```python
from qsnctf import *

a = shake_128('qsnctf2022',"10")
print(a) # b134959f759d7fa1942c
```

#### SHAKE256

##### shake256

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|       shake_256        |       string        |      hash.py       |                           shake256                           |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|      input_string      |        False        |       string       |              Content that needs to be encrypted              |
|          bits          |        False        |   int or string    | Used to specify the length of the hash value for the output. |

##### Use examples

```python
from qsnctf import *

a = shake_256('qsnctf2022',"10")
print(a) # 94c31528e7a32076b1f4
```

#### HMAC-SHA256

##### hmac-sha256

|   **Function name**    |   **Return type**   |    **location**    |           **illustrate**           |
| :--------------------: | :-----------------: | :----------------: | :--------------------------------: |
|    HMAC_SHA256_HEX     |       string        |      hash.py       |            hmac_sha256             |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**           |
|         secret         |        False        |       string       | Content that needs to be encrypted |
|          data          |        False        |   int or string    |         The encrypted key          |

##### Use examples

```python
from qsnctf import *

a = HMAC_SHA256_HEX('qsnctf2022',123)
print(a) # f7ce26af7e17adebd72d3cd9120fa4acd05c66aab676462026e916a53a71f564
```

#### SHA3_224

##### sha3_224

|   **Function name**    |   **Return type**   |    **location**    |           **illustrate**           |
| :--------------------: | :-----------------: | :----------------: | :--------------------------------: |
|        sha3_224        |       string        |      hash.py       |              sha3_224              |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**           |
|      input_string      |        False        |       string       | Content that needs to be encrypted |

##### Use examples

```python
from qsnctf import *

a = sha3_224('qsnctf2022')
print(a) # 2b7580cd6d4f6a8c3b96d4d08bcbf9e8ddf6d3c393cffb69dd7bc967
```

#### SHA3_256

##### sha3_256

|   **Function name**    |   **Return type**   |    **location**    |           **illustrate**           |
| :--------------------: | :-----------------: | :----------------: | :--------------------------------: |
|        sha3_256        |       string        |      hash.py       |              sha3_256              |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**           |
|      input_string      |        False        |       string       | Content that needs to be encrypted |

##### Use examples

```python
from qsnctf import *

a = sha3_256('qsnctf2022')
print(a) # ec570495a42596f49037c6f72a93c3a5803a040146a53e7f030cd7c11c0b1c79
```

#### SHA3_384

##### sha3_384

|   **Function name**    |   **Return type**   |    **location**    |           **illustrate**           |
| :--------------------: | :-----------------: | :----------------: | :--------------------------------: |
|        sha3_384        |       string        |      hash.py       |              sha3_384              |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**           |
|      input_string      |        False        |       string       | Content that needs to be encrypted |

##### Use examples

```python
from qsnctf import *

a = sha3_384('qsnctf2022')
print(a) # f3df64859a8e1b1912e1b237f1b54863fb6f11ca9bc117e019e69ceb4d7e1cacd75c8d33b1e25967428d8a7b3cee23f5
```

#### SHA3_512

##### sha3_512

|   **Function name**    |   **Return type**   |    **location**    |           **illustrate**           |
| :--------------------: | :-----------------: | :----------------: | :--------------------------------: |
|        sha3_512        |       string        |      hash.py       |              sha3_512              |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**           |
|      input_string      |        False        |       string       | Content that needs to be encrypted |

##### Use examples

```python
from qsnctf import *

a = sha3_512('qsnctf2022')
print(a) # 95e2d7d428f1b4d007be25dfd454131796f6fa2162662ec34fe8a9aa52f463f5021d5c32cfc422ea3055ed666afb1fc9edc86e65a3f57129ce2d7b2e7617e71e
```

 

## ENVIRONMENT

##### Development environment

`Windows11 + Python3.11 + PyCharm 2022.3.1 (Professional Edition)`

##### Usage environment

Support for the `Python 3.x`environment.

The documentation is continuously updated.

## ✨ Contributors

Thank everyone on the list：

<table>
  <tr>
    <td align="center"><a href="https://github.com/Moxin1044"><img src="https://avatars.githubusercontent.com/u/59173630?v=4" width="100px;" alt=""/><br /><sub><b>Moxin</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/wang256814742"><img src="https://avatars.githubusercontent.com/u/75202489?v=4" width="100px;" alt=""/><br /><sub><b>xinyi</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/yiye-yfs"><img src="https://avatars.githubusercontent.com/u/79006318?v=4" width="100px;" alt=""/><br /><sub><b>yiye-yfs</b></sub></a><br /></td>
  </tr>
</table>
