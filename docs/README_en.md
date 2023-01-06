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
| Custom base64 |        |        |        |         |

### CRYPTO

| Caesar Code | Caesar blasts | Bacon password | ROT5 | ROT13 |
| :---------: | :-----------: | :------------: | :--: | :---: |
|    ROT18    |      Gossip password         |    Etbash code            |   Morse Code (customizable)   |    Qwerty password   |

### MD5

|   md5    |   sha1   |  sha224  |   sha256    |  sha384  |
| :------: | :------: | :------: | :---------: | :------: |
|  sha512  | shake128 | shake256 | HMAC-SHA256 | sha3-224 |
| sha3-256 | sha3-385 | sha3-512 |             |          |



### MISC

| Core values Encryption and decryption | Text reverses | URL encryption and decryption | Bit XOR | Text Reverse (Step 2) |
| :-----------------------------------: | :-----------: | :---------------------------: | :-----: | --------------------- |
|    Text Reverse (custom step size)    | Get the UUID  | ord to string|      String to ord   |    String splitting                   |
| Flag looking |  Hundred family name code| Qwerty coded| HTM code	 | JSFUCK |

### API

| Quipqiup word frequency analysis | Feishu Webhook | DingTalk | Microstep online | FOFA |
| :--------------: | :---------: | -------- | -------- | ---- |
|    Great Saint Cloud Sandbox    |  Zero Zero Trust   |          |          |      |

### WEB

|   Directory scanning   | Website survival detection |   Take the title of the website    | Subdomain scanning | Take the site description |
| :----------: | :----------: | :-------------: | :--------: | :--------: |
| Take the website keyword |  Take the website ICP   | Take the address of the website A label | Take the site comment |     Take the website response time       |
|  Take the website ICO   | POST Webshell |  GET Webshell   | exec-shell |   eval-shell   |
| WebShell blast |               |                 |            |                |


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


## Web.py

### Scan

#### class-DirScan

##### DirScan

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|        DirScan         |        list         |       web.py       |                   Site directory scanning                    |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|          url           |        False        |       string       | Website address, format: https://bbs.qsnctf.com If it exists/it will be automatically deleted |
|       treadline        |        True         |        int         | The number of threads (need to pass integers) should not be too high The default is 10 threads |
|       sleep_time       |        True         |        int         |           The default time between each scan is 0            |
|        dirlist         |        True         |        list        | DirScan's list in the format ['/www.zip','/index.php'] The default scan library path is in the /plugin/txt/dirs.txt |
|      return_code       |        True         |        list        | Returns a status list of results, in the format [200, 301, 302, 401, 403, 500], which is also the default format |
|          echo          |        True         |      Boolean       | Whether to output scan results directly The default value is False |
|          wait          |        True         |      Boolean       | Whether to wait for thread to end The default value is True  |

**illustrate：Please pay attention to the rules of the contest for use。**

##### Use examples

```python
from qsnctf import *

dir = DirScan('https://bbs.qsnctf.com/', 10, 0.5)
print(dir.results_code) # ['https://bbs.qsnctf.com/robots.txt 200', 'https://bbs.qsnctf.com/admin.php 200', 'https://bbs.qsnctf.com/sitemap.txt 200', 'https://bbs.qsnctf.com/sitemap.xml 200']
# 下面的结果中只会存在返回的请求
print(dir.results) # ['https://bbs.qsnctf.com/robots.txt', 'https://bbs.qsnctf.com/admin.php', 'https://bbs.qsnctf.com/sitemap.txt', 'https://bbs.qsnctf.com/sitemap.xml']

DirScan('https://bbs.qsnctf.com/', 100, 0.1, echo=True) # 将会直接进行扫描并打印结果（这样在显示上更快，但是效率同上）
"""
https://bbs.qsnctf.com/admin.php 200
https://bbs.qsnctf.com/robots.txt 200
https://bbs.qsnctf.com/sitemap.txt 200
https://bbs.qsnctf.com/home.php 200
https://bbs.qsnctf.com/sitemap.xml 200
https://bbs.qsnctf.com/index.php 200
https://bbs.qsnctf.com/install/ 403
"""
```

#### class-UrlScan

##### UrlScan

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|        UrlScan         |        list         |       web.py       |                     Site status scanning                     |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|        url_list        |        False        |       string       | Website address, format: https://bbs.qsnctf.com If it exists/it will be automatically deleted |
|       treadline        |        True         |        int         | The number of threads (need to pass integers) should not be too high The default is 10 threads |
|       sleep_time       |        True         |        int         |           The default time between each scan is 0            |
|      return_code       |        True         |        list        | Returns a status list of results, in the format [200, 301, 302, 401, 403, 500], which is also the default format |
|          echo          |        True         |      Boolean       | Whether to output scan results directly The default value is False |
|          wait          |        True         |      Boolean       | Whether to wait for thread to end The default value is True  |

**illustrate：Please pay attention to the rules of the contest for use。**

##### Use examples

```python
from qsnctf import *

list = ["https://bbs.qsnctf.com/admin.php", "https://bbs.qsnctf.com/robots.txt", "https://www.qsnctf.com/"]
dir = UrlScan(list, 10, 0.5)
print(dir.results_code) # ['https://bbs.qsnctf.com/robots.txt 200', 'https://bbs.qsnctf.com/admin.php 200', 'https://www.qsnctf.com/ 200']
# 下面的结果中只会存在返回的请求
print(dir.results) # ['https://bbs.qsnctf.com/robots.txt', 'https://bbs.qsnctf.com/admin.php', 'https://www.qsnctf.com/']
UrlScan(list, 100, 0.1, echo=True) # 将会直接进行扫描并打印结果（这样在显示上更快，但是效率同上）
"""
https://bbs.qsnctf.com/robots.txt 200 No Title
https://bbs.qsnctf.com/admin.php 200 登录管理中心
https://www.qsnctf.com/ 200 青少年CTF训练平台 | 原中学生CTF平台 | 青少年CTF
"""
```

**illustrate：`No Title` is the Title tag in the HTML page that is not found**

#### class-DomainScan

##### DomainScan

| **Function name	**  |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|       DomainScan       |        list         |       web.py       |                      Subdomain scanning                      |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|         domain         |        False        |       string       |           Website domain name, format: qsnctf.com            |
|       treadline        |        True         |        int         | The number of threads (need to pass integers) should not be too high The default is 10 threads |
|       sleep_time       |        True         |        int         |           The default time between each scan is 0            |
|       domainlist       |        True         |        list        | List of scanned subdomains, in the format ['abc', 'www'] The contents of the /plugin/txt/domain.txt under the default library path are scanned |
|      return_code       |        True         |        list        | Returns a status list of results, in the format [200, 301, 302, 401, 403, 404, 500], which is also the default format |
|          echo          |        True         |      Boolean       | Whether to output scan results directly The default value is False |
|          wait          |        True         |      Boolean       | Whether to wait for thread to end The default value is True  |

**illustrate：Please pay attention to the rules of the contest for use.**

```python
from qsnctf import *

a = DomainScan("qsnctf.com")
print(a.results_title)
# ['http://www.qsnctf.com/ 青少年CTF训练平台 | 原中学生CTF平台 | 青少年CTF', 'http://ctf.qsnctf.com/ 克拉玛依市第一届网络安全技能大赛', 'http://test.qsnctf.com/ 克拉玛依高级中学--十三年', 'http://tools.qsnctf.com/ 青少年CTF在线工具箱 | CTF在线工具']
print(a.results) 
# ['http://www.qsnctf.com/', 'http://ctf.qsnctf.com/', 'http://test.qsnctf.com/', 'http://tools.qsnctf.com/']

```

#### Take the website information

##### get_url_title

| **Function name	**  |   **Return type**   |    **location**    |           **illustrate**            |
| :--------------------: | :-----------------: | :----------------: | :---------------------------------: |
|     get_url_title      |       string        |       web.py       |    Take the title of the website    |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**            |
|          url           |        False        |       string       |           Website address           |
|         Cookie         |        True         |       string       | Website cookies, which can be empty |

**illustrate：Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *

a = get_url_title("https://www.baidu.com/")
print(a) # 百度一下，你就知道
```

**illustrate：No Title is the Title tag in the HTML page that is not found**

##### get_url_description

| **Function name	**  |   **Return type**   |    **location**    |           **illustrate**            |
| :--------------------: | :-----------------: | :----------------: | :---------------------------------: |
|  get_url_description   |       string        |       web.py       |      Take the site description      |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**            |
|          url           |        False        |       string       |           Website address           |
|         Cookie         |        True         |       string       | Website cookies, which can be empty |

**illustrate：Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *


a = get_url_description('https://www.qsnctf.com/')
print(a)  # 青少年CTF|青少年CTF训练平台是针对青少年网络安全爱好者的训练平台，平台内有大量原创题，并收录了各大比赛的题目进行公益的学习。我们所有的题目均为免费公开，给广大学子提供更多的学习途径。
```

**illustrate：No description is the description tag in the HTML page that is not found**

##### get_url_keywords

| **Function name	**  |   **Return type**   |    **location**    |           **illustrate**            |
| :--------------------: | :-----------------: | :----------------: | :---------------------------------: |
|    get_url_keywords    |       string        |       web.py       |      Take the website keyword       |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**            |
|          url           |        False        |       string       |           Website address           |
|         Cookie         |        True         |       string       | Website cookies, which can be empty |

**illustrate：Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *


a = get_url_keywords('https://www.qsnctf.com/')
print(a)  # 青少年CTF,青少年CTF平台,青少年CTF训练平台,中学生CTF平台,中学生CTF训练平台,青少年网络安全,青少年CTF在线训练平台,CTF训练平台,CTF平台
```

**illustrate：No keywords are keywords tags that are not found in HTML pages**

##### get_url_ICP

| **Function name	**  |   **Return type**   |    **location**    |              **illustrate**               |
| :--------------------: | :-----------------: | :----------------: | :---------------------------------------: |
|      get_url_ICP       |       string        |       web.py       | Take the ICP filing number of the website |
| **The parameter name** | **Nullable or not** | **Parameter type** |              **illustrate**               |
|          url           |        False        |       string       |              Website address              |
|         Cookie         |        True         |       string       |    Website cookies, which can be empty    |

**illustrate：Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *


a = get_url_ICP('https://www.qsnctf.com/')
print(a)  # 备案号：鲁ICP备2022011740号-3
```

**illustrate：No ICP is the ICP tag in the HTML page that is not found**

##### get_url_a_href

| **Function name	**  |   **Return type**   |    **location**    |              **illustrate**               |
| :--------------------: | :-----------------: | :----------------: | :---------------------------------------: |
|     get_url_a_href     |        list         |       web.py       | Take the href of the A tag of the website |
| **The parameter name** | **Nullable or not** | **Parameter type** |              **illustrate**               |
|          url           |        False        |       string       |              Website address              |
|         Cookie         |        True         |       string       |    Website cookies, which can be empty    |

**illustrate：Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *


a = get_url_a_href('https://www.qsnctf.com/')
print(a)  # ['/', 'login', 'http://bbs.qsnctf.com/', 'javascript:;', 'https://www.sierting.com', 'https://beian.miit.gov.cn']
```

**illustrate：No href is the href tag in the HTML page that is not found**

##### get_url_img

| **Function name	**  |   **Return type**   |    **location**    |           **illustrate**            |
| :--------------------: | :-----------------: | :----------------: | :---------------------------------: |
|      get_url_img       |        list         |       web.py       |        Take the website img         |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**            |
|          url           |        False        |       string       |           Website address           |
|         Cookie         |        True         |       string       | Website cookies, which can be empty |

**illustrate：Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *


a = get_url_a_href('https://www.qsnctf.com/')
print(a)  # ['/logo.png', 'data/attachment/block/b8/b85a300493f1bd7ef7e0268dec2c3217.jpg']
```

**illustrate：No src is the src tag found in the HTML web page**

##### get_url_comment

| **Function name	**  |   **Return type**   |    **location**    |           **illustrate**            |
| :--------------------: | :-----------------: | :----------------: | :---------------------------------: |
|    get_url_comment     |        list         |       web.py       |  Take the comments in the website   |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**            |
|          url           |        False        |       string       |           Website address           |
|         Cookie         |        True         |       string       | Website cookies, which can be empty |

**illustrate：Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *


a = get_url_comment('https://www.qsnctf.com/')
print(a)  # ['baidutongji']
```

**illustrate：No comment is a comment node found in the HTML page**


#### Take the website response time

##### get_url_time

|   **Function name**    |   **Return type**   |    **location**    |         **illustrate**         |
| :--------------------: | :-----------------: | :----------------: | :----------------------------: |
|      get_url_time      |       string        |       web.py       | Take the website response time |
| **The parameter name** | **Nullable or not** | **Parameter type** |         **illustrate**         |
|          url           |        False        |       string       |        Website address         |

**illustrate：Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *


a = get_url_time('https://www.qsnctf.com/')
print(a)  # ['0.0155']
```

#### Take the ICO of the website

##### get_url_ico

|   **Function name**    |   **Return type**   |    **location**    |       **illustrate**        |
| :--------------------: | :-----------------: | :----------------: | :-------------------------: |
|      get_url_ico       |       string        |       web.py       | Take the ICO of the website |
| **The parameter name** | **Nullable or not** | **Parameter type** |       **illustrate**        |
|          url           |        False        |       string       |       Website address       |

**illustrate：Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *


a = get_url_ico('https://www.qsnctf.com/')
print(a)  # ['/ico.ico']
```

### WebShell operations

**This feature is for CTF and its own website use only and should not be used illegally.**

#### POST to test the WebShell password

##### get_webshell_post

|   **Function name**    |   **Return type**   |    **location**    | **illustrate** |
| :--------------------: | :-----------------: | :----------------: | :------------: |
|   get_webshell_post    |       string        |       web.py       | Test Webshell  |
| **The parameter name** | **Nullable or not** | **Parameter type** | **illustrate** |
|          url           |        False        |       string       | Shell address  |
|          key           |        False        |       string       |      key       |

**illustrate：Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *


a = get_webshell_post('http://localhost/shell.php', 'cmd')
print(a) # True
```

#### GET method to test WebShell password

##### get_webshell_get

|   **Function name**    |   **Return type**   |    **location**    | **illustrate** |
| :--------------------: | :-----------------: | :----------------: | :------------: |
|    get_webshell_get    |       string        |       web.py       | Test Webshell  |
| **The parameter name** | **Nullable or not** | **Parameter type** | **illustrate** |
|          url           |        False        |       string       | Shell address  |
|          key           |        False        |       string       |      key       |

**illustrate：Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *


a = get_webshell_get('http://localhost/shell.php', 'cmd')
print(a) # True
```

#### exec-webshell command execution (POST)

##### get_exec_webshell_post

|   **Function name**    |   **Return type**   |    **location**    |        **illustrate**        |
| :--------------------: | :-----------------: | :----------------: | :--------------------------: |
| get_exec_webshell_post |       string        |       web.py       | The exec command is executed |
| **The parameter name** | **Nullable or not** | **Parameter type** |        **illustrate**        |
|          url           |        False        |       string       |        Shell address         |
|          key           |        False        |       string       |             key              |
|         shell          |        Fasle        |       string       |     The command executed     |

**illustrate：Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *


a = get_exec_webshell_post('http://localhost/shell.php', 'cmd', 'whoami')
print(a) # root
```

#### exec-webshell command execution (get)

##### get_exec_webshell_get

|   **Function name**    |   **Return type**   |    **location**    |        **illustrate**        |
| :--------------------: | :-----------------: | :----------------: | :--------------------------: |
| get_exec_webshell_get  |       string        |       web.py       | The exec command is executed |
| **The parameter name** | **Nullable or not** | **Parameter type** |        **illustrate**        |
|          url           |        False        |       string       |        Shell address         |
|          key           |        False        |       string       |             key              |
|         shell          |        Fasle        |       string       |     The command executed     |

**illustrate：Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *


a = get_exec_webshell_get('http://localhost/shell.php', 'cmd', 'whoami')
print(a) # root
```

#### eval-webshell code execution (get)

##### get_eval_webshell_get

|   **Function name**    |   **Return type**   |    **location**    |   **illustrate**    |
| :--------------------: | :-----------------: | :----------------: | :-----------------: |
| get_eval_webshell_get  |       string        |       web.py       | EVAL code execution |
| **The parameter name** | **Nullable or not** | **Parameter type** |   **illustrate**    |
|          url           |        False        |       string       |    Shell address    |
|          key           |        False        |       string       |         key         |
|         shell          |        Fasle        |       string       |  The executed code  |

**illustrate：Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *


a = get_eval_webshell_get('http://localhost/shell.php', 'cmd', 'print("123");')
print(a) # 123
```

#### Eval-Webshell Code Execution (POST)

##### get_eval_webshell_post

|   **Function name**    |   **Return type**   |    **location**    |   **illustrate**    |
| :--------------------: | :-----------------: | :----------------: | :-----------------: |
| get_eval_webshell_post |       string        |       web.py       | EVAL code execution |
| **The parameter name** | **Nullable or not** | **Parameter type** |   **illustrate**    |
|          url           |        False        |       string       |    Shell address    |
|          key           |        False        |       string       |         key         |
|         shell          |        Fasle        |       string       |  The executed code  |

**illustrate：Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *


a = get_eval_webshell_post('http://localhost/shell.php', 'cmd', 'print("123");')
print(a) # 123
```

#### WebShell blast

##### WebShellCracking

|   **Function name**    |   **Return type**   |    **location**    |        **illustrate**        |
| :--------------------: | :-----------------: | :----------------: | :--------------------------: |
|    WebShellCracking    |       string        |       web.py       |  WebShell password blasting  |
| **The parameter name** | **Nullable or not** | **Parameter type** |        **illustrate**        |
|          url           |        False        |       string       |        Shell address         |
|       threadline       |        False        |        int         |    The number of threads     |
|       sleep_time       |        Fasle        |        int         |        Access latency        |
|        passlist        |        False        |        list        | A list of possible passwords |
|          mode          |        False        |       string       | Gate Auster defaults to Post |

**illustrate：Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *


a = WebShellCracking('http://localhost/shell.php', threadline=50,mode="GET")
print(a.results) # cmd
```


## API.py

### quipqiup

#### class-quipqiup

##### quipqiup

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|        quipqiup        | string、json、list  |       api.py       | quipqiup word frequency analysis (internet connection required) |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|       ciphertext       |        False        |       string       |                       What is analyzed                       |
|         clues          |        True         |       string       |  Analysis clues, empty by default, For example G=R QVW=THE   |

**illustrate：This feature requires a network connection，please pay attention to the rules of the contest for use。**

##### Use examples

```python
from qsnctf import *

a = quipqiup('test')
print(a.text) # that,high,area,died***
print(a.json) # {'id': 931788518, 'result': 0, 'result-message': 'success', 'time0': 1672662393.35963, 'last': 1, 'solutions': [{'logp': -1.58357763290405, 'plaintext': 'that', ***
print(a.list) # ['that', 'high',***
```

### Feishu Webhook

#### class-FeishuWebhook

##### FeishuWebhook

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|     FeishuWebhook      |        None         |       api.py       |                 Feishu Webhook notifications                 |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|         title          |        False        |       string       |                The title of the notification                 |
|        message         |        False        |       string       |               The message of the notification                |
|         token          |        False        |       string       | Feishu token, take the content behind Feishu robot /v2/hook/ |
|       send_type        |        False        |       string       | Types sent: text, card, text message and card message, respectively |

**illustrate：This feature requires a network connection，Please pay attention to the rules of the contest for use。**

##### Use examples

```python
from qsnctf import *

FeishuWebhook('青少年CTF', '你好，我是末心', 'xxxx-xxxxx-xxxx-xxxx-xxxxx','card')
```

### DingTalk

#### class-DingTalk

##### DingTalk

|   **Function name**    |   **Return type**   |    **location**    |         **illustrate**          |
| :--------------------: | :-----------------: | :----------------: | :-----------------------------: |
|        DingTalk        |        None         |       api.py       | DingTalk Webhook notifications  |
| **The parameter name** | **Nullable or not** | **Parameter type** |         **illustrate**          |
|         title          |        False        |       string       |  The title of the notification  |
|        message         |        False        |       string       | The message of the notification |
|         token          |        False        |       string       |        Token of DingTalk        |

**illustrate：This feature requires a network connection，Please pay attention to the rules of the contest for use。**

##### Use examples

```python
from qsnctf import *

DingTalk('青少年CTF', '你好，我是末心', 'xxxx-xxxxx-xxxx-xxxx-xxxxx')
```

### Microstep online

#### class-ThreatBook

##### ThreatBook

|   **Function name**    |   **Return type**   |    **location**    |        **illustrate**        |
| :--------------------: | :-----------------: | :----------------: | :--------------------------: |
|       ThreatBook       |       object        |       api.py       |       Microstep online       |
| **The parameter name** | **Nullable or not** | **Parameter type** |        **illustrate**        |
|        api_key         |        False        |       string       | Microstepping online API Key |

API Key gets the address：https://x.threatbook.com/v5/myApi

**illustrate：This feature requires a network connection，Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *

tb = ThreatBook('***') # 主要是配合下面的调用返回的一个对象
```

#### Microstep - IP reputation

##### ip_reputation

|   **Function name**    |   **Return type**   |    **location**    |             **illustrate**              |
| :--------------------: | :-----------------: | :----------------: | :-------------------------------------: |
|     ip_reputation      |        json         |       api.py       |        Microstep - IP reputation        |
| **The parameter name** | **Nullable or not** | **Parameter type** |             **illustrate**              |
|           ip           |        False        |       string       | The IP address that needs to be queried |

**illustrate：This feature requires a network connection，Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *

tb = ThreatBook('***')
a = tb.ip_reputation('127.0.0.1')
print(a)
```

```json
{'data': {'127.0.0.1': {'severity': '无威胁', 'judgments': ['白名单', '保留地址'], 'tags_classes': [], 'basic': {'carrier': '', 'location': {'country': '', 'province': '', 'city': '', 'lng': '', 'lat': '', 'country_code': 'B1'}}, 'asn': {}, 'scene': '', 'confidence_level': '高', 'is_malicious': False, 'update_time': '2023-01-05 18:41:54'}}, 'response_code': 0, 'verbose_msg': '成功'}

```

#### File upload analysis

##### file_upload

|   **Function name**    |   **Return type**   |    **location**    |                      **illustrate**                       |
| :--------------------: | :-----------------: | :----------------: | :-------------------------------------------------------: |
|      file_upload       |        json         |       api.py       |     Microstep File Anti-Virus Engine detection report     |
| **The parameter name** | **Nullable or not** | **Parameter type** |                      **illustrate**                       |
|       file_path        |        False        |       string       |                  The path to the upload                   |
|       file_name        |        False        |       string       |          The file name that needs to be uploaded          |
|      sandbox_type      |        True         |       string       | Sandbox environment, win7_sp1_enx64_office2013 by default |

Sandbox running environment: Users can specify the sandbox running environment of the file, optional environments include:

- **Windows** 
  - win7_sp1_enx64_office2013 
  - win7_sp1_enx86_office2013 
  - win7_sp1_enx86_office2010 
  - win7_sp1_enx86_office2007 
  - win7_sp1_enx86_office2003
- **Linux** 
  - ubuntu_1704_x64 
  - centos_7_x64

**illustrate：This feature requires a network connection，Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *

tb = ThreatBook('***')
a = tb.file_upload('./','1.exe')
print(a)
# {'data': {'sha256': '***', 'permalink': 'https://s.threatbook.cn/search?query=***&type=sha256'}, 'response_code': 0, 'verbose_msg': 'OK'}
```

#### Microstep File Anti-Virus Engine detection report

##### file_report_multiengines

|    **Function name**     |   **Return type**   |    **location**    |                  **illustrate**                   |
| :----------------------: | :-----------------: | :----------------: | :-----------------------------------------------: |
| file_report_multiengines |        json         |       api.py       | Microstep File Anti-Virus Engine detection report |
|  **The parameter name**  | **Nullable or not** | **Parameter type** |                  **illustrate**                   |
|          sha256          |        False        |       string       |                    File sha256                    |

**illustrate：This feature requires a network connection，Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *

tb = ThreatBook('***')
a = tb.file_report_multiengines('******')
print(a)
# {'data': {'multiengines': {'threat_level': 'clean', 'total': 22, 'is_white': False, 'total2': 22, 'positives': 0, 'scan_date': '2023-01-05 19:04:42', 'scans': {'IKARUS': 'safe', 'vbwebshell': 'safe', 'Avast': 'safe', 'Avira': 'safe', 'Sophos': 'safe', 'K7': 'safe', 'Rising': 'safe', 'Kaspersky': 'safe', 'Panda': 'safe', 'Baidu-China': 'safe', 'NANO': 'safe', 'Antiy': 'safe', 'AVG': 'safe', 'Baidu': 'safe', 'DrWeb': 'safe', 'GDATA': 'safe', 'Microsoft': 'safe', 'Qihu360': 'safe', 'ESET': 'safe', 'ClamAV': 'safe', 'JiangMin': 'safe', 'Trustlook': 'safe'}}}, 'response_code': 0, 'verbose_msg': 'OK'}
```

#### Microstep file reports

##### file_report

|   **Function name**    |   **Return type**   |    **location**    |                      **illustrate**                       |
| :--------------------: | :-----------------: | :----------------: | :-------------------------------------------------------: |
|      file_report       |        json         |       api.py       |                  Microstep file reports                   |
| **The parameter name** | **Nullable or not** | **Parameter type** |                      **illustrate**                       |
|         sha256         |        False        |       string       |                        File sha256                        |
|      sandbox_type      |        True         |       string       | Sandbox environment, win7_sp1_enx64_office2013 by default |

 Sandbox running environment: Users can specify the sandbox running environment of the file, optional environments include:

- **Windows** 
  - win7_sp1_enx64_office2013 
  - win7_sp1_enx86_office2013 
  - win7_sp1_enx86_office2010 
  - win7_sp1_enx86_office2007 
  - win7_sp1_enx86_office2003
- **Linux** 
  - ubuntu_1704_x64 
  - centos_7_x64

**illustrate：This feature requires a network connection，Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *

tb = ThreatBook('***')
a = tb.file_report('******')
print(a)

```

### FOFA

#### class-FOFA

##### FOFA

|   **Function name**    |   **Return type**   |    **location**    |                   **illustrate**                    |
| :--------------------: | :-----------------: | :----------------: | :-------------------------------------------------: |
|          FOFA          |       object        |       api.py       | [FOFA_SDK](https://github.com/Moxin1044/pythonfofa) |
| **The parameter name** | **Nullable or not** | **Parameter type** |                   **illustrate**                    |
|         email          |        False        |       string       |                     FOFA Email                      |
|          key           |        False        |       string       |                      FOFA Key                       |

Key gets the address：https://fofa.info/

**illustrate：This feature requires a network connection，Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *

fofa = FOFA('***','xxxx') # 主要是配合下面的调用返回的一个对象
```

#### FOFA User Information

##### userinfo

|   **Function name**    |   **Return type**   |    **location**    | **illustrate** |
| :--------------------: | :-----------------: | :----------------: | :------------: |
|        userinfo        |        json         |       api.py       | FOFA 用户信息  |
| **The parameter name** | **Nullable or not** | **Parameter type** | **illustrate** |

**illustrate：This feature requires a network connection，Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *

fofa = FOFA('***','xxxx')
print(fofa.userinfo())
```

```json
{
  "error": false,
  "email": "****@qq.com",
  "username": "***",
  "fcoin": 48,
  "isvip": true,
  "vip_level": 2,
  "is_verified": false,
  "avatar": "https://i.nosec.org/avatar/system/****",
  "message": "",
  "fofacli_ver": "4.0.3",
  "fofa_server": true
}
```



#### FOFA queries

##### search

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|         search         |        json         |       api.py       |              The FOFA query interface is called              |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|       query_text       |        False        |       string       |             Support for FOFA advanced statements             |
|         field          |        True         |       string       |                    Default host, ip, port                    |
|          page          |        True         |        int         |                            Pages                             |
|          size          |        True         |        int         |                  Number of queries per page                  |
|          full          |        True         |      Boolean       | The default search is data within one year, and if you specify true, you can search all data |

**illustrate：This feature requires a network connection，Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *

fofa = FOFA('***','xxxx')
print(fofa.search('title="bing"'))
# field =  ['ip','port','title','icp']
# fofa.search('domain="qq.com"',field=field,size=10)
```

```json
{
  "error": false,
  "size": 8683,
  "page": 1,
  "mode": "extended",
  "query": "title\u003d\"bing\"",
  "results": [
    [
      "46.101.204.107",
      "hotel-bing.hotels-rimini-it.com",
      "80"
    ],
    [
      "104.21.32.129",
      "https://peapix.com",
      "443"
    ],
    [
      "193.8.37.83",
      "https://www.thorsmindecamping.dk",
      "443"
    ]
  ]
}
```

#### FOFA statistical aggregation

##### search_stats

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|      search_stats      |        json         |       api.py       |                 FOFA statistical aggregation                 |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|       query_text       |        False        |       string       | The statement that needs to be queried, that is, the query content entered |
|         field          |        True         |       string       | Optional fields, default title, see Details[Appendix 2](https://fofa.info/api/stats/statistical) |

**illustrate：This feature requires a network connection，Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *

fofa = FOFA('***','xxxx')
print(fofa.search_stats('ip="103.35.168.38"'))
# field =  ['ip','port','title','icp']
# fofa.search('domain="qq.com"',field=field,size=10)
```

```json
{
  "error": false,
  "distinct": {
    "ip": 1,
    "title": 1
  },
  "aggs": {
    "countries": [],
    "title": [
      {
        "count": 1,
        "name": "RouterOS router configuration page"
      }
    ]
  },
  "lastupdatetime": "2022-06-11 07:00:00"
}
```

#### FOFA HOST aggregation

##### search_host

|   **Function name**    |   **Return type**   |    **location**    |      **illustrate**       |
| :--------------------: | :-----------------: | :----------------: | :-----------------------: |
|      search_host       |        json         |       api.py       |   FOFA HOST aggregation   |
| **The parameter name** | **Nullable or not** | **Parameter type** |      **illustrate**       |
|          host          |        False        |       string       |   Host name, usually IP   |
|         detail         |        True         |      Boolean       | Displays the port details |

**illustrate：This feature requires a network connection，Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *

fofa = FOFA('***','xxxx')
print(fofa.search_host('78.48.50.249'))
```

```json
{
  "error": false,
  "host": "78.48.50.249",
  "ip": "78.48.50.249",
  "asn": 6805,
  "org": "Telefonica Germany",
  "country_name": "Germany",
  "country_code": "DE",
  "protocol": [
    "http",
    "sip",
    "https"
  ],
  "port": [
    8089,
    5060,
    7170,
    80,
    443
  ],
  "category": [
    "CMS"
  ],
  "product": [
    "Synology-WebStation"
  ],
  "update_time": "2022-12-29 05:00:00"
}
```

### Great Saint Cloud Sandbox

#### class-DaSheng

##### DaSheng

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|        DaSheng         |       object        |       api.py       | [Great Saint Cloud Sandbox](https://sandbox.freebuf.com/cloudApi) |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|           id           |        False        |       string       |                          Client ID                           |
|          key           |        False        |       string       |                        Client secret                         |

Key gets the address：https://sandbox.freebuf.com/cloudApi

**illustrate：This feature requires a network connection，Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *

ds = DaSheng('***','xxxx') # 主要是配合下面的调用返回的一个对象
```

#### Token acquisition

##### token

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|         token          |       string        |       api.py       | [Great Saint Cloud Sandbox](https://sandbox.freebuf.com/cloudApi)Token |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |

**Generally, not writing operations may not be useful**

**illustrate：This feature requires a network connection，Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *

ds = DaSheng('***','xxxx')
print(ds.token())
```

#### File upload

##### upload

|   **Function name**    |   **Return type**   |    **location**    | **illustrate** |
| :--------------------: | :-----------------: | :----------------: | :------------: |
|         upload         |       object        |       api.py       | Sample upload  |
| **The parameter name** | **Nullable or not** | **Parameter type** | **illustrate** |
|        file_dir        |        False        |       string       |      path      |
|       file_name        |        False        |       string       |    filename    |

**Generally, not writing operations may not be useful**

**illustrate：This feature requires a network connection，Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *

ds = DaSheng('***','xxxx')
print(ds.upload('路径','文件名'))
```

#### File upload

##### upload

|   **Function name**    |   **Return type**   |    **location**    | **illustrate** |
| :--------------------: | :-----------------: | :----------------: | :------------: |
|         upload         |       object        |       api.py       | Sample queries |
| **The parameter name** | **Nullable or not** | **Parameter type** | **illustrate** |
|          sha1          |        False        |       string       |   File sha1    |

**Generally, not writing operations may not be useful**

**illustrate：This feature requires a network connection，Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *

ds = DaSheng('***','xxxx')
print(ds.search('sha1'))
```

### Zero Zero Trust

#### class-ZeroZeon

##### ZeroZeon

|   **Function name**    |   **Return type**   |    **location**    |           **illustrate**           |
| :--------------------: | :-----------------: | :----------------: | :--------------------------------: |
|        ZeroZeon        |       object        |       api.py       | [Zero Zero Trust](https://0.zone/) |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**           |
|          key           |        False        |       string       |              api_key               |

Key gets the address：https://0.zone/plug-in-unit

**illustrate：This feature requires a network connection，Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *

zero = ZeroZeon('xxxx') # 主要是配合下面的调用返回的一个对象
```

#### Zero Zero Information Inquiry

##### search

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|         search         |        json         |       api.py       | [Great Saint Cloud Sandbox](https://sandbox.freebuf.com/cloudApi)Token |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|         title          |        False        |       string       |       Query statements, which support advanced search        |

**Generally, not writing operations may not be useful**

**illustrate：This feature requires a network connection，Please pay attention to the rules of the contest for use.**

##### Use examples

```python
from qsnctf import *

zero = ZeroZeon('xxxx') # 主要是配合下面的调用返回的一个对象
print(zero.search('title==零零信安'))
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

#### Custom Base64

##### base64_encode_custom

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|  base64_encode_custom  |       string        |      base.py       |             Base64 encoding (supported Chinese)              |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|          text          |        False        |       string       |                   What needs to be encoded                   |
|      custom_table      |        False        |       string       |                        Encoding table                        |
|        encoding        |        True         |       string       | The encoding when decoding text, the default value is UTF-8  |
|        decoding        |        True         |       string       | The encoding when exporting text, the default value is UTF-8 |

##### base64_decode_custom

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|  base64_decode_custom  |       string        |      base.py       |                       Base64 decoding                        |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|          text          |        False        |       string       |                   What needs to be decoded                   |
|      custom_table      |        False        |       string       |                        Encoding table                        |
|        encoding        |        True         |       string       | The encoding when decoding text, the default value is UTF-8  |
|        decoding        |        True         |       string       | The encoding when exporting text, the default value is UTF-8 |

##### Use examples

```python
from qsnctf import *

data = 'SGVsbG8sIFdvcmxkIQ=='
custom_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-'
a = base64_encode_custom(data, custom_table)
print(a)
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
# MISC.py

### Various encodings

#### Core values

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

#### URL encoding

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
 #### Hundred family name code

##### baijiaxing_encode

|   **Function name**    |   **Return type**   |    **location**    |      **illustrate**      |
| :--------------------: | :-----------------: | :----------------: | :----------------------: |
|   baijiaxing_encode    |       string        |      misc.py       | Hundred family name code |
| **The parameter name** | **Nullable or not** | **Parameter type** |      **illustrate**      |
|      source_text       |        False        |       string       | What needs to be encoded |

##### baijiaxing_decode

|   **Function name**    |   **Return type**   |    **location**    |        **illustrate**        |
| :--------------------: | :-----------------: | :----------------: | :--------------------------: |
|   baijiaxing_decode    |       string        |      misc.py       | Hundred family names decoded |
| **The parameter name** | **Nullable or not** | **Parameter type** |        **illustrate**        |
|      source_text       |        False        |       string       |   What needs to be decoded   |

##### Use examples

```python
from qsnctf import *

a = baijiaxing_encode('abcde')
print(a) # 褚卫蒋沈韩
b = baijiaxing_decode('褚卫蒋沈韩')
print(b) # abcde
```

#### Qwerty coded

##### qwerty_encode

|   **Function name**    |   **Return type**   |    **location**    |           **illustrate**           |
| :--------------------: | :-----------------: | :----------------: | :--------------------------------: |
|     qwerty_encode      |       string        |     crypto.py      |          Qwerty password           |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**           |
|      source_text       |        False        |       string       | Content that needs to be encrypted |

##### Use examples

```python
from qsnctf import *

a = qwerty_encode('abcd')
print(a) # qwer
```

##### qwerty_decode

|   **Function name**    |   **Return type**   |    **location**    |       **illustrate**       |
| :--------------------: | :-----------------: | :----------------: | :------------------------: |
|     qwerty_decode      |       string        |     crypto.py      |      Qwerty password       |
| **The parameter name** | **Nullable or not** | **Parameter type** |       **illustrate**       |
|      source_text       |        False        |       string       | What needs to be decrypted |

##### Use examples

```python
from qsnctf import *

a = qwerty_decode('qwer')
print(a) # abcd
```

#### HTML encoding

##### html_encode

|   **Function name**    |   **Return type**   |    **location**    |      **illustrate**      |
| :--------------------: | :-----------------: | :----------------: | :----------------------: |
|      html_encode       |       string        |     crypto.py      |      HTML encoding       |
| **The parameter name** | **Nullable or not** | **Parameter type** |      **illustrate**      |
|         string         |        False        |       string       | What needs to be encoded |

##### Use example

```python
from qsnctf import *

a = html_encode('<script>')
print(a)
```

##### html_decode

|   **Function name**    |   **Return type**   |    **location**    |      **illustrate**      |
| :--------------------: | :-----------------: | :----------------: | :----------------------: |
|      html_decode       |       string        |     crypto.py      |      HTML encoding       |
| **The parameter name** | **Nullable or not** | **Parameter type** |      **illustrate**      |
|         string         |        False        |       string       | What needs to be decoded |

##### Use example

```python
from qsnctf import *

b = html_decode('&lt;script&gt;')
print(b)
```

#### JSfuck

##### jsfuck_encode

|   **Function name**    |   **Return type**   |    **location**    |      **illustrate**      |
| :--------------------: | :-----------------: | :----------------: | :----------------------: |
|     jsfuck_encode      |       string        |     crypto.py      |          JSFUCK          |
| **The parameter name** | **Nullable or not** | **Parameter type** |      **illustrate**      |
|         string         |        False        |       string       | What needs to be encoded |

##### Use example

```python
from qsnctf import *

b = jsfuck_encode('abcdefg')
print(b) # [][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((![]+[])[+!+[]]+([][(!![]+[])[!+[]+!+[]+!+[]]+([][[]]+[])[+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]]()+[])[!+[]+!+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]]+[])[!+[]+!+[]+!+[]]+([][[]]+[])[!+[]+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(![]+[])[+[]]+(![]+[+[]]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]])
```

##### jsfuck_decode

|   **Function name**    |   **Return type**   |    **location**    |      **illustrate**      |
| :--------------------: | :-----------------: | :----------------: | :----------------------: |
|     jsfuck_decode      |       string        |     crypto.py      |          JSFUCK          |
| **The parameter name** | **Nullable or not** | **Parameter type** |      **illustrate**      |
|         string         |        False        |       string       | What needs to be decoded |

##### Use example

```python
from qsnctf import *

a = jsfuck_decode('(![]+[])[+!+[]]+([][(!![]+[])[!+[]+!+[]+!+[]]+([][[]]+[])[+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]]()+[])[!+[]+!+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]]+[])[!+[]+!+[]+!+[]]')
print(a)
```

#### AAencode

##### aaencode

|   **Function name**    |   **Return type**   |    **location**    |      **illustrate**      |
| :--------------------: | :-----------------: | :----------------: | :----------------------: |
|        aaencode        |       string        |     crypto.py      |          JSFUCK          |
| **The parameter name** | **Nullable or not** | **Parameter type** |      **illustrate**      |
|         string         |        False        |       string       | What needs to be encoded |

##### Use example

```python
from qsnctf import *

a = aaencode('qsnctf')
print(a)
```

##### aadecode

|   **Function name**    |   **Return type**   |    **location**    |      **illustrate**      |
| :--------------------: | :-----------------: | :----------------: | :----------------------: |
|        aadecode        |       string        |     crypto.py      |          JSFUCK          |
| **The parameter name** | **Nullable or not** | **Parameter type** |      **illustrate**      |
|         string         |        False        |       string       | What needs to be decoded |

##### Use example

```python
from qsnctf import *

b = aadecode(r"ﾟωﾟﾉ= /｀ｍ´）ﾉ ~┻━┻   //*´∇｀*/ ['_']; o=(ﾟｰﾟ)  =_=3; c=(ﾟΘﾟ) =(ﾟｰﾟ)-(ﾟｰﾟ); (ﾟДﾟ) =(ﾟΘﾟ)= (o^_^o)/ (o^_^o);(ﾟДﾟ)={ﾟΘﾟ: '_' ,ﾟωﾟﾉ : ((ﾟωﾟﾉ==3) +'_') [ﾟΘﾟ] ,ﾟｰﾟﾉ :(ﾟωﾟﾉ+ '_')[o^_^o -(ﾟΘﾟ)] ,ﾟДﾟﾉ:((ﾟｰﾟ==3) +'_')[ﾟｰﾟ] }; (ﾟДﾟ) [ﾟΘﾟ] =((ﾟωﾟﾉ==3) +'_') [c^_^o];(ﾟДﾟ) ['c'] = ((ﾟДﾟ)+'_') [ (ﾟｰﾟ)+(ﾟｰﾟ)-(ﾟΘﾟ) ];(ﾟДﾟ) ['o'] = ((ﾟДﾟ)+'_') [ﾟΘﾟ];(ﾟoﾟ)=(ﾟДﾟ) ['c']+(ﾟДﾟ) ['o']+(ﾟωﾟﾉ +'_')[ﾟΘﾟ]+ ((ﾟωﾟﾉ==3) +'_') [ﾟｰﾟ] + ((ﾟДﾟ) +'_') [(ﾟｰﾟ)+(ﾟｰﾟ)]+ ((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+((ﾟｰﾟ==3) +'_') [(ﾟｰﾟ) - (ﾟΘﾟ)]+(ﾟДﾟ) ['c']+((ﾟДﾟ)+'_') [(ﾟｰﾟ)+(ﾟｰﾟ)]+ (ﾟДﾟ) ['o']+((ﾟｰﾟ==3) +'_') [ﾟΘﾟ];(ﾟДﾟ) ['_'] =(o^_^o) [ﾟoﾟ] [ﾟoﾟ];(ﾟεﾟ)=((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+ (ﾟДﾟ) .ﾟДﾟﾉ+((ﾟДﾟ)+'_') [(ﾟｰﾟ) + (ﾟｰﾟ)]+((ﾟｰﾟ==3) +'_') [o^_^o -ﾟΘﾟ]+((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+ (ﾟωﾟﾉ +'_') [ﾟΘﾟ]; (ﾟｰﾟ)+=(ﾟΘﾟ); (ﾟДﾟ)[ﾟεﾟ]='\\'; (ﾟДﾟ).ﾟΘﾟﾉ=(ﾟДﾟ+ ﾟｰﾟ)[o^_^o -(ﾟΘﾟ)];(oﾟｰﾟo)=(ﾟωﾟﾉ +'_')[c^_^o];(ﾟДﾟ) [ﾟoﾟ]='\"';(ﾟДﾟ) ['_'] ( (ﾟДﾟ) ['_'] (ﾟεﾟ+(ﾟДﾟ)[ﾟoﾟ]+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (o^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (o^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟoﾟ]) (ﾟΘﾟ)) ('_');")
print(b)
```



### String operations

#### Inverse string

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



#### Inverse string (including step size)

##### string_reverse_step

| **Function name**    | **Return type**     | **location**       | **illustrate**                     |
| -------------------- | ------------------- | ------------------ | ---------------------------------- |
| string_reverse_step2 | string              | misc.py            | String inverse with step 2         |
| **The paramet name** | **Nullable or not** | **Parameter type** | **illustrate**                     |
| string               | False               | string             | Content that needs to be reversed  |
| step                 | False               | int                | Step length, generally more than 2 |

##### Use example

```python
from qsnctf import *


print(string_reverse_step('abc123', 3))  # cba321
```

##### string_reverse_step2

| **Function name**    | **Return type**     | **location**       | **illustrate**                    |
| -------------------- | ------------------- | ------------------ | --------------------------------- |
| string_reverse_step2 | string              | misc.py            | String inverse with step 2        |
| **The paramet name** | **Nullable or not** | **Parameter type** | **illustrate**                    |
| string               | False               | string             | Content that needs to be reversed |

##### Use example

```python
from qsnctf import *


a = string_reverse_step2('abc123')
print(a) # ba1c32
```

#### List XOR

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


#### String conversion

##### string_split

|   **Function name**    |   **Return type**   |    **location**    |             **illustrate**              |
| :--------------------: | :-----------------: | :----------------: | :-------------------------------------: |
|      string_split      |        list         |      misc.py       | Automatic segmentation based on content |
| **The parameter name** | **Nullable or not** | **Parameter type** |             **illustrate**              |
|           s            |        False        |       string       | Text that needs to be split into lists  |

##### Use example

```python
from qsnctf import *


a = string_split("abcdefg")
print(a)
a = string_split("a,b,c,d,e,f,g")
print(a)
a = string_split("a b c d e f g")
print(a)
"""
['a', 'b', 'c', 'd', 'e', 'f', 'g']
['a', 'b', 'c', 'd', 'e', 'f', 'g']
['a', 'b', 'c', 'd', 'e', 'f', 'g']
"""
```

**illustrate：Interception can be made according to different content judgments, and the final result is consistent**

##### ord_to_str

|   **Function name**    |   **Return type**   |    **location**    |              **illustrate**              |
| :--------------------: | :-----------------: | :----------------: | :--------------------------------------: |
|       ord_to_str       |       string        |      misc.py       |             ord value to str             |
| **The parameter name** | **Nullable or not** | **Parameter type** |              **illustrate**              |
|          ord           |        False        |        int         | The ord value that needs to be converted |

##### Use example

```python
from qsnctf import *


print(ord_to_str(97)) #a
```

##### ord_list_to_str_list

|   **Function name**    |   **Return type**   |    **location**    |               **illustrate**               |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------: |
|  ord_list_to_str_list  |        list         |      misc.py       |         ord to str (list support）         |
| **The parameter name** | **Nullable or not** | **Parameter type** |               **illustrate**               |
|        ord_list        |        False        |        list        | The list of ords that need to be converted |

##### Use example

```python
from qsnctf import *


a = ord_list_to_str_list(['97', '98', '99'])
print(a)  # ['a', 'b', 'c']
```

##### ord_str_to_str

|   **Function name**    |   **Return type**   |    **location**    |                     **illustrate**                      |
| :--------------------: | :-----------------: | :----------------: | :-----------------------------------------------------: |
|     ord_str_to_str     |       string        |      misc.py       |            ord value to str (string support)            |
| **The parameter name** | **Nullable or not** | **Parameter type** |                     **illustrate**                      |
|        ord_str         |        False        |        list        | ord string, which can be separated by commas and spaces |

##### Use example

```python
from qsnctf import *


a = ord_str_to_str('97,98,99')
print(a)  # abc
```

##### chr_to_ord

|   **Function name**    |   **Return type**   |    **location**    |               **illustrate**                |
| :--------------------: | :-----------------: | :----------------: | :-----------------------------------------: |
|       chr_to_ord       |       string        |      misc.py       |              char to ord value              |
| **The parameter name** | **Nullable or not** | **Parameter type** |               **illustrate**                |
|          char          |        False        |        int         | Char (characters) that need to be converted |

##### Use example

```python
from qsnctf import *


print(chr_to_ord('a')) #97
```

##### chr_list_to_ord_list

|   **Function name**    |   **Return type**   |    **location**    |               **illustrate**               |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------: |
|  chr_list_to_ord_list  |        list         |      misc.py       |            CHR list to ord list            |
| **The parameter name** | **Nullable or not** | **Parameter type** |               **illustrate**               |
|        chr_list        |        False        |        list        | The list of chr that needs to be converted |

##### Use example

```python
from qsnctf import *


a = chr_list_to_ord_list(['a', 'b', 'c'])
print(a)  # [97, 98, 99]
```

##### chr_str_to_ord_str

|   **Function name**    |   **Return type**   |    **location**    |                        **illustrate**                        |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------------------------: |
|   chr_str_to_ord_str   |       string        |      misc.py       |                      chr to ord string                       |
| **The parameter name** | **Nullable or not** | **Parameter type** |                        **illustrate**                        |
|        chr_str         |        False        |        list        | The chr string can be separated by commas, spaces, or no distinction |

##### Use example

```python
from qsnctf import *


a = ord_str_to_str('abc')
print(a)  # 97,98,99
```

##### search_flag

|   **Function name**    |   **Return type**   |    **location**    |               **illustrate**               |
| :--------------------: | :-----------------: | :----------------: | :----------------------------------------: |
|      search_flag       |       string        |      misc.py       |      Find flags through regular regex      |
| **The parameter name** | **Nullable or not** | **Parameter type** |               **illustrate**               |
|          text          |        False        |       string       | Content that is suspected to contain flags |
|      flag_prefix       |        True         |       string       |       Flag prefix, in the form flag        |

##### Use example

```python
from qsnctf import *


a = search_flag('hello, i will give you flag flag{qsnctf-12345}')
print(a) # flag{qsnctf-12345}
```


### Crypto

#### Caesar Code

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

#### Caesar Code Blast

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


#### Gossip password

##### eight_diagrams_encrypt

|   **Function name**    |   **Return type**   |    **location**    |           **illustrate**           |
| :--------------------: | :-----------------: | :----------------: | :--------------------------------: |
| eight_diagrams_encrypt |       string        |     crypto.py      |     Gossip password encryption     |
| **The parameter name** | **Nullable or not** | **Parameter type** |           **illustrate**           |
|          text          |        False        |       string       | Content that needs to be encrypted |

##### eight_diagrams_decrypt

|   **Function name**    |   **Return type**   |    **location**    |       **illustrate**       |
| :--------------------: | :-----------------: | :----------------: | :------------------------: |
| eight_diagrams_decrypt |       string        |     crypto.py      | Gossip password decryption |
| **The parameter name** | **Nullable or not** | **Parameter type** |       **illustrate**       |
|          text          |        False        |       string       | What needs to be decrypted |

##### Use examples

```python
from qsnctf import *

a = eight_diagrams_encrypt('qsnctf')
print(a)  # 正巽震~正巽兑~正离巽~正艮兑~正巽艮~正艮巽~
a = eight_diagrams_decrypt('正巽震~正巽兑~正离巽~正艮兑~正巽艮~正艮巽~')
print(a)  # qsnctf
```

#### Etbash code

##### atbash_cipher

|   **Function name**    |   **Return type**   |    **location**    |                 **illustrate**                  |
| :--------------------: | :-----------------: | :----------------: | :---------------------------------------------: |
|     atbash_cipher      |       string        |     crypto.py      |                   Etbash code                   |
| **The parameter name** | **Nullable or not** | **Parameter type** |                 **illustrate**                  |
|          text          |        False        |       string       | Content that needs to be encrypted or decrypted |

##### Use examples

```python
from qsnctf import *


a = atbash_cipher('qsnctf.com')
print(a) # jhmxgu.xln
a = atbash_cipher('jhmxgu.xln')
print(a) # qsnctf.com

```

#### Morse cipher encryption

##### morse_encrypt

|   **Function name**    |   **Return type**   |    **location**    |                      **illustrate**                      |
| :--------------------: | :-----------------: | :----------------: | :------------------------------------------------------: |
|     morse_encrypt      |       string        |     crypto.py      |                 Morse cipher encryption                  |
| **The parameter name** | **Nullable or not** | **Parameter type** |                      **illustrate**                      |
|        message         |        False        |       string       |            Content that needs to be encrypted            |
|         split          |        True         |       string       | The delimiter (the default is a space) can be set to "/" |
|         point          |        True         |       string       |        Click the "" used to replace Morse code."         |
|          bar           |        True         |       string       |  horizontal "-" used as a replacement for Morse cipher   |

##### Use examples

```python
from qsnctf import *

a = morse_encrypt('QSNCTF','/')
print(a) # --.-/.../-./-.-./-/..-.
```

#### Morse code decryption

##### morse_decrypt

|   **Function name**    |   **Return type**   |    **location**    |                      **illustrate**                      |
| :--------------------: | :-----------------: | :----------------: | :------------------------------------------------------: |
|     morse_decrypt      |       string        |     crypto.py      |                  Morse code decryption                   |
| **The parameter name** | **Nullable or not** | **Parameter type** |                      **illustrate**                      |
|         cipher         |        False        |       string       |                What needs to be decrypted                |
|         split          |        True         |       string       | The delimiter (the default is a space) can be set to "/" |
|         point          |        True         |       string       |        Click the "" used to replace Morse code."         |
|          bar           |        True         |       string       |  horizontal "-" used as a replacement for Morse cipher   |

##### Use examples

```python
from qsnctf import *

b = morse_decrypt('..-./---/.-/.-.-/./--.-','/', '-', '.')
print(b) # QSNCTF
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
