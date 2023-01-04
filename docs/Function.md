# 函数库 - 我应该如何使用

由于Base、各种加密的方法较多，传参方法也花样百出。这里给大家写出这个文档方便参考，包含了供给大家使用的函数的说明、注意事项、参数和返回值等信息。

## Web.py

### DirScan

#### class-DirScan

##### DirScan

| **函数名**  | **返回类型** |   **位置**   |                           **说明**                           |
| :---------: | :----------: | :----------: | :----------------------------------------------------------: |
|   DirScan   |     list     |    web.py    |                       网站目录扫描工具                       |
| **参数名**  | **是否可空** | **传参类型** |                           **说明**                           |
|     url     |    False     |    string    | 网站地址，格式：https://bbs.qsnctf.com 如果后面存在/会自动删去 |
|  treadline  |     True     |     int      |        线程数（需要传整数）不可以太高了哦 默认10线程         |
| sleep_time  |     True     |     int      |                   每次扫描间隔时间 默认是0                   |
|   dirlist   |     True     |     list     | DirScan的列表，格式['/www.zip','/index.php'] 默认扫描库路径下的/plugin/txt/dirs.txt中的内容 |
| return_code |     True     |     list     | 返回结果的状态列表，格式[200, 301, 302, 401, 403, 500] ，格式也是默认值 |

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

dir = DirScan('https://bbs.qsnctf.com/', 10, 0.5)
print(dir.results_code) # ['https://bbs.qsnctf.com/robots.txt 200', 'https://bbs.qsnctf.com/admin.php 200', 'https://bbs.qsnctf.com/sitemap.txt 200', 'https://bbs.qsnctf.com/sitemap.xml 200']
# 下面的结果中只会存在返回的请求
print(dir.results) # ['https://bbs.qsnctf.com/robots.txt', 'https://bbs.qsnctf.com/admin.php', 'https://bbs.qsnctf.com/sitemap.txt', 'https://bbs.qsnctf.com/sitemap.xml']
```

## API.py

### quipqiup

#### class-quipqiup

##### quipqiup

| **函数名** |    **返回类型**    |   **位置**   |                  **说明**                   |
| :--------: | :----------------: | :----------: | :-----------------------------------------: |
|  quipqiup  | string、json、list |    api.py    |         quipqiup 词频分析（需联网）         |
| **参数名** |    **是否可空**    | **传参类型** |                  **说明**                   |
| ciphertext |       False        |    string    |                 分析的内容                  |
|   clues    |        True        |    string    | 分析线索，默认为空，For example G=R QVW=THE |

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

a = quipqiup('test')
print(a.text) # that,high,area,died***
print(a.json) # {'id': 931788518, 'result': 0, 'result-message': 'success', 'time0': 1672662393.35963, 'last': 1, 'solutions': [{'logp': -1.58357763290405, 'plaintext': 'that', ***
print(a.list) # ['that', 'high',***
```

### 飞书Webhook

#### class-FeishuWebhook

##### FeishuWebhook

|  **函数名**   | **返回类型** |   **位置**   |                    **说明**                     |
| :-----------: | :----------: | :----------: | :---------------------------------------------: |
| FeishuWebhook |     None     |    api.py    |                 飞书Webhook通知                 |
|  **参数名**   | **是否可空** | **传参类型** |                    **说明**                     |
|     title     |    False     |    string    |                   通知的标题                    |
|    message    |    False     |    string    |                   通知的消息                    |
|     token     |    False     |    string    |  飞书的Token，取飞书机器人/v2/hook/后面的内容   |
|   send_type   |    False     |    string    | 发送的类型：text、card 分别为文本消息和卡片消息 |

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

FeishuWebhook('青少年CTF', '你好，我是末心', 'xxxx-xxxxx-xxxx-xxxx-xxxxx','card')
```

### DingTalk

#### class-DingTalk

##### DingTalk

| **函数名** | **返回类型** |   **位置**   |    **说明**     |
| :--------: | :----------: | :----------: | :-------------: |
|  DingTalk  |     None     |    api.py    | 钉钉Webhook通知 |
| **参数名** | **是否可空** | **传参类型** |    **说明**     |
|   title    |    False     |    string    |   通知的标题    |
|  message   |    False     |    string    |   通知的消息    |
|   token    |    False     |    string    |   钉钉的Token   |

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

DingTalk('青少年CTF', '你好，我是末心', 'xxxx-xxxxx-xxxx-xxxx-xxxxx')
```

## Base.py

### Base家族

#### Base100

##### base100_encode

|   **函数名**   | **返回类型** |   **位置**   |           **说明**            |
| :------------: | :----------: | :----------: | :---------------------------: |
| base100_encode |    string    |   base.py    |     base100编码(支持中文)     |
|   **参数名**   | **是否可空** | **传参类型** |           **说明**            |
|      text      |    False     |    string    |        需要编码的内容         |
|    encoding    |     True     |    string    | 解码文本时的编码，默认值utf-8 |
|    decoding    |     True     |    string    | 输出文本时的编码，默认值utf-8 |

##### base100_decode

|   **函数名**   | **返回类型** |   **位置**   |           **说明**            |
| :------------: | :----------: | :----------: | :---------------------------: |
| base100_decode |    string    |   base.py    |          base100解码          |
|   **参数名**   | **是否可空** | **传参类型** |           **说明**            |
|      text      |    False     |    string    |        需要解码的内容         |
|    encoding    |     True     |    string    | 解码文本时的编码，默认值utf-8 |
|    decoding    |     True     |    string    | 输出文本时的编码，默认值utf-8 |

##### 使用示例

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

|  **函数名**   | **返回类型** |   **位置**   |           **说明**           |
| :-----------: | :----------: | :----------: | :--------------------------: |
| base92_encode |    string    |   base.py    | base92编码（无法编码中文哦） |
|  **参数名**   | **是否可空** | **传参类型** |           **说明**           |
|     text      |    False     |    string    |        需要编码的内容        |

##### base92_decode

|  **函数名**   | **返回类型** |   **位置**   |    **说明**    |
| :-----------: | :----------: | :----------: | :------------: |
| base92_decode |    string    |   base.py    |   base92解码   |
|  **参数名**   | **是否可空** | **传参类型** |    **说明**    |
|     text      |    False     |    string    | 需要解码的内容 |

##### 使用示例

```python
from qsnctf import *


a = base92_encode('qsnctf123QSN')
print(a) # ItHYSr3{(eF*?n>
a = base92_decode('ItHYSr3{(eF*?n>')
print(a) # qsnctf123QSN
```

#### Base91

##### base91_encode

|  **函数名**   | **返回类型** |   **位置**   |        **说明**        |
| :-----------: | :----------: | :----------: | :--------------------: |
| base91_encode |    string    |   base.py    | base91编码（支持中文） |
|  **参数名**   | **是否可空** | **传参类型** |        **说明**        |
|     text      |    False     |    string    |     需要编码的内容     |

##### base91_decode

|  **函数名**   | **返回类型** |   **位置**   |    **说明**    |
| :-----------: | :----------: | :----------: | :------------: |
| base91_decode |    string    |   base.py    |   base91解码   |
|  **参数名**   | **是否可空** | **传参类型** |    **说明**    |
|     text      |    False     |    string    | 需要解码的内容 |

##### 使用示例

```python
from qsnctf import *


a = base91_encode('青少年CTF')
print(a) # N_jjjief!gTFU,I
a = base91_decode('N_jjjief!gTFU,I')
print(a) # 青少年CTF
```

#### Base85

##### base85_encode

|  **函数名**   | **返回类型** |   **位置**   |           **说明**            |
| :-----------: | :----------: | :----------: | :---------------------------: |
| base85_encode |    string    |   base.py    |    base85编码（支持中文）     |
|  **参数名**   | **是否可空** | **传参类型** |           **说明**            |
|     text      |    False     |    string    |        需要编码的内容         |
|   encoding    |     True     |    string    | 解码文本时的编码，默认值utf-8 |
|   decoding    |     True     |    string    | 输出文本时的编码，默认值utf-8 |

##### base85_decode

|  **函数名**   | **返回类型** |   **位置**   |           **说明**            |
| :-----------: | :----------: | :----------: | :---------------------------: |
| base85_decode |    string    |   base.py    |          base85解码           |
|  **参数名**   | **是否可空** | **传参类型** |           **说明**            |
|     text      |    False     |    string    |        需要解码的内容         |
|   encoding    |     True     |    string    | 解码文本时的编码，默认值utf-8 |
|   decoding    |     True     |    string    | 输出文本时的编码，默认值utf-8 |

##### 使用示例

```python
from qsnctf import *


a = base85_encode('青少年CTF')
print(a) # >7A10u#x4tv_n)z
a = base85_decode('>7A10u#x4tv_n)z')
print(a) # 青少年CTF
```

#### Base64

##### base64_encode

|  **函数名**   | **返回类型** |   **位置**   |           **说明**            |
| :-----------: | :----------: | :----------: | :---------------------------: |
| base64_encode |    string    |   base.py    |    base64编码（支持中文）     |
|  **参数名**   | **是否可空** | **传参类型** |           **说明**            |
|     text      |    False     |    string    |        需要编码的内容         |
|   encoding    |     True     |    string    | 解码文本时的编码，默认值utf-8 |
|   decoding    |     True     |    string    | 输出文本时的编码，默认值utf-8 |

##### base64_decode

|  **函数名**   | **返回类型** |   **位置**   |           **说明**            |
| :-----------: | :----------: | :----------: | :---------------------------: |
| base64_decode |    string    |   base.py    |          base64解码           |
|  **参数名**   | **是否可空** | **传参类型** |           **说明**            |
|     text      |    False     |    string    |        需要解码的内容         |
|   encoding    |     True     |    string    | 解码文本时的编码，默认值utf-8 |
|   decoding    |     True     |    string    | 输出文本时的编码，默认值utf-8 |

##### 使用示例

```python
from qsnctf import *


a = base64_encode('青少年CTF')
print(a) # 6Z2S5bCR5bm0Q1RG
a = base64_decode('6Z2S5bCR5bm0Q1RG')
print(a) # 青少年CTF
```

#### Base62

##### base62_encode

|  **函数名**   | **返回类型** |   **位置**   |          **说明**          |
| :-----------: | :----------: | :----------: | :------------------------: |
| base62_encode |  **string**  |   base.py    | base62编码（只能是整数哦） |
|  **参数名**   | **是否可空** | **传参类型** |          **说明**          |
|     ints      |    False     |   **int**    |       需要编码的内容       |

##### base62_decode

|  **函数名**   | **返回类型** |   **位置**   |    **说明**    |
| :-----------: | :----------: | :----------: | :------------: |
| base62_decode |   **int**    |   base.py    |   base62解码   |
|  **参数名**   | **是否可空** | **传参类型** |    **说明**    |
|     text      |    False     |    string    | 需要解码的内容 |

##### 使用示例

```python
from qsnctf import *


a = base62_encode(123456)
print(a) # W7E
a = base62_decode('W7E')
print(a) # 123456
```

#### Base58

##### base58_encode

|  **函数名**   | **返回类型** |   **位置**   |           **说明**            |
| :-----------: | :----------: | :----------: | :---------------------------: |
| base58_encode |    string    |   base.py    |    base58编码（支持中文）     |
|  **参数名**   | **是否可空** | **传参类型** |           **说明**            |
|     text      |    False     |    string    |        需要编码的内容         |
|   encoding    |     True     |    string    | 解码文本时的编码，默认值utf-8 |
|   decoding    |     True     |    string    | 输出文本时的编码，默认值utf-8 |

##### base58_decode

|  **函数名**   | **返回类型** |   **位置**   |           **说明**            |
| :-----------: | :----------: | :----------: | :---------------------------: |
| base58_decode |    string    |   base.py    |          base58解码           |
|  **参数名**   | **是否可空** | **传参类型** |           **说明**            |
|     text      |    False     |    string    |        需要解码的内容         |
|   encoding    |     True     |    string    | 解码文本时的编码，默认值utf-8 |
|   decoding    |     True     |    string    | 输出文本时的编码，默认值utf-8 |

##### 使用示例

```python
from qsnctf import *


a = base58_encode('青少年CTF')
print(a) # 5QhHM9SSxYiJbYQMj
a = base58_decode('5QhHM9SSxYiJbYQMj')
print(a) # 青少年CTF
```

#### Base36

##### base36_encode

|  **函数名**   | **返回类型** |   **位置**   |          **说明**          |
| :-----------: | :----------: | :----------: | :------------------------: |
| base36_encode |  **string**  |   base.py    | base36编码（只能是整数哦） |
|  **参数名**   | **是否可空** | **传参类型** |          **说明**          |
|    encoded    |    False     |   **int**    |       需要编码的内容       |

##### base36_decode

|  **函数名**   | **返回类型** |   **位置**   |    **说明**    |
| :-----------: | :----------: | :----------: | :------------: |
| base36_decode |   **int**    |   base.py    |   base36解码   |
|  **参数名**   | **是否可空** | **传参类型** |    **说明**    |
|     text      |    False     |    string    | 需要解码的内容 |

##### 使用示例

```python
from qsnctf import *


a = base36_encode(123456)
print(a) # 2n9c
a = base36_decode('2n9c')
print(a) # 123456
```

#### Base32

##### base32_encode

|  **函数名**   | **返回类型** |   **位置**   |           **说明**            |
| :-----------: | :----------: | :----------: | :---------------------------: |
| base32_encode |    string    |   base.py    |    base32编码（支持中文）     |
|  **参数名**   | **是否可空** | **传参类型** |           **说明**            |
|     text      |    False     |    string    |        需要编码的内容         |
|   encoding    |     True     |    string    | 解码文本时的编码，默认值utf-8 |
|   decoding    |     True     |    string    | 输出文本时的编码，默认值utf-8 |

##### base32_decode

|  **函数名**   | **返回类型** |   **位置**   |           **说明**            |
| :-----------: | :----------: | :----------: | :---------------------------: |
| base32_decode |    string    |   base.py    |          base32解码           |
|  **参数名**   | **是否可空** | **传参类型** |           **说明**            |
|     text      |    False     |    string    |        需要解码的内容         |
|   encoding    |     True     |    string    | 解码文本时的编码，默认值utf-8 |
|   decoding    |     True     |    string    | 输出文本时的编码，默认值utf-8 |

##### 使用示例

```python
from qsnctf import *


a = base32_encode('青少年CTF')
print(a) # 5GOZFZNQSHS3TNCDKRDA====
a = base32_decode('5GOZFZNQSHS3TNCDKRDA====')
print(a) # 青少年CTF
```

#### Base16

##### base16_encode

|  **函数名**   | **返回类型** |   **位置**   |           **说明**            |
| :-----------: | :----------: | :----------: | :---------------------------: |
| base16_encode |    string    |   base.py    |    base16编码（支持中文）     |
|  **参数名**   | **是否可空** | **传参类型** |           **说明**            |
|     text      |    False     |    string    |        需要编码的内容         |
|   encoding    |     True     |    string    | 解码文本时的编码，默认值utf-8 |
|   decoding    |     True     |    string    | 输出文本时的编码，默认值utf-8 |

##### base16_decode

|  **函数名**   | **返回类型** |   **位置**   |           **说明**            |
| :-----------: | :----------: | :----------: | :---------------------------: |
| base16_decode |    string    |   base.py    |          base16解码           |
|  **参数名**   | **是否可空** | **传参类型** |           **说明**            |
|     text      |    False     |    string    |        需要解码的内容         |
|   encoding    |     True     |    string    | 解码文本时的编码，默认值utf-8 |
|   decoding    |     True     |    string    | 输出文本时的编码，默认值utf-8 |

##### 使用示例

```python
from qsnctf import *


a = base16_encode('青少年CTF')
print(a) # E99D92E5B091E5B9B4435446
a = base16_decode('E99D92E5B091E5B9B4435446')
print(a) # 青少年CTF
```

## Misc.py

### 各种编码

#### 核心价值观

##### Chinese_socialism_encode

|        **函数名**        | **返回类型** |   **位置**   |        **说明**        |
| :----------------------: | :----------: | :----------: | :--------------------: |
| Chinese_socialism_encode |    string    |   misc.py    | 社会主义核心价值观编码 |
|        **参数名**        | **是否可空** | **传参类型** |        **说明**        |
|          string          |    False     |    string    |     需要编码的内容     |

##### Chinese_socialism_decode

|        **函数名**        | **返回类型** |   **位置**   |        **说明**        |
| :----------------------: | :----------: | :----------: | :--------------------: |
| Chinese_socialism_decode |    string    |   misc.py    | 社会主义核心价值观解码 |
|        **参数名**        | **是否可空** | **传参类型** |        **说明**        |
|          string          |    False     |    string    |     需要解码的内容     |

##### 使用示例

```python
from qsnctf import *


a = Chinese_socialism_encode('青少年CTF')
print(a) # 友善爱国敬业敬业诚信和谐敬业文明友善爱国平等诚信民主富强敬业民主友善爱国平等友善平等敬业诚信民主自由自由和谐平等自由自由公正
a = Chinese_socialism_decode('友善爱国敬业敬业诚信和谐敬业文明友善爱国平等诚信民主富强敬业民主友善爱国平等友善平等敬业诚信民主自由自由和谐平等自由自由公正')
print(a) # 青少年CTF
```

#### URL编码

##### url_encode

| **函数名** | **返回类型** |   **位置**   |    **说明**    |
| :--------: | :----------: | :----------: | :------------: |
| url_encode |    string    |   misc.py    |    URL编码     |
| **参数名** | **是否可空** | **传参类型** |    **说明**    |
|   string   |    False     |    string    | 需要编码的内容 |

##### url_decode

| **函数名** | **返回类型** |   **位置**   |    **说明**    |
| :--------: | :----------: | :----------: | :------------: |
| url_decode |    string    |   misc.py    |    URL解码     |
| **参数名** | **是否可空** | **传参类型** |    **说明**    |
|   string   |    False     |    string    | 需要解码的内容 |

##### 使用示例

```python
from qsnctf import *


a = url_encode('青少年CTF=中学生CTF')
print(a) # %E9%9D%92%E5%B0%91%E5%B9%B4CTF%3D%E4%B8%AD%E5%AD%A6%E7%94%9FCTF
a = url_decode('%E9%9D%92%E5%B0%91%E5%B9%B4CTF%3D%E4%B8%AD%E5%AD%A6%E7%94%9FCTF')
print(a) # 青少年CTF=中学生CTF
```

### 字符串操作

#### 逆向字符串

##### string_reverse

|   **函数名**   | **返回类型** |   **位置**   |           **说明**           |
| :------------: | :----------: | :----------: | :--------------------------: |
| string_reverse |    string    |   misc.py    | 逆向字符串，字符串倒序、翻转 |
|   **参数名**   | **是否可空** | **传参类型** |           **说明**           |
|     string     |    False     |    string    |        需要逆向的内容        |

##### 使用示例

```python
from qsnctf import *


a = string_reverse('青少年CTF')
print(a) # FTC年少青
```

#### 逆向字符串（包含步长）

##### string_reverse_step

|      **函数名**      | **返回类型** |   **位置**   |      **说明**       |
| :------------------: | :----------: | :----------: | :-----------------: |
| string_reverse_step2 |    string    |   misc.py    | 步长为2的字符串逆向 |
|      **参数名**      | **是否可空** | **传参类型** |      **说明**       |
|        string        |    False     |    string    |   需要逆向的内容    |
|         step         |    False     |     int      |  步长，一般是2以上  |

##### 使用示例

```python
from qsnctf import *


print(string_reverse_step('abc123', 3))  # cba321
```

##### string_reverse_step2

|      **函数名**      | **返回类型** |   **位置**   |      **说明**       |
| :------------------: | :----------: | :----------: | :-----------------: |
| string_reverse_step2 |    string    |   misc.py    | 步长为2的字符串逆向 |
|      **参数名**      | **是否可空** | **传参类型** |      **说明**       |
|        string        |    False     |    string    |   需要逆向的内容    |

##### 使用示例

```python
from qsnctf import *


a = string_reverse_step2('abc123')
print(a) # ba1c32
```

#### 列表异或

##### xor_list

| **函数名** | **返回类型** |   **位置**   | **说明** |
| :--------: | :----------: | :----------: | :------: |
|  xor_list  |    string    |   misc.py    | URL编码  |
| **参数名** | **是否可空** | **传参类型** | **说明** |
|  lt_data   |    False     |     list     | 异或数据 |
|  lt_root   |    False     |     list     |  异或根  |

##### 使用示例

```python
from qsnctf import *

a = "abcde" # 因为string在Python中来说可以当做列表来截取，所以可以直接这样传
b = "01234"
c = xor_list(a, b)
print(c) # QSQWQ
```

#### UUID

##### get_uuid()

| **函数名** | **返回类型** |   **位置**   | **说明** |
| :--------: | :----------: | :----------: | :------: |
|  get_uuid  |    string    |   misc.py    | URL编码  |
| **参数名** | **是否可空** | **传参类型** | **说明** |

##### 使用示例

```python
from qsnctf import *

c = get_uuid()
print(c) # d3a07212-a9dc-4129-937a-30fec20e604a
```

## Crypto.py

### 密码学

#### 凯撒密码

##### caesar_encrypt

|   **函数名**   | **返回类型** |   **位置**    |             **说明**              |
| :------------: | :----------: | :-----------: | :-------------------------------: |
| caesar_encrypt |    string    |   crypto.py   |           凯撒密码加密            |
|   **参数名**   | **是否可空** | **传参类型**  |             **说明**              |
|      text      |    False     |    string     |          需要加密的内容           |
|     shift      |    False     | int or string | 偏移量，传入可为string，会转换int |

##### caesar_decrypt

|   **函数名**   | **返回类型** |   **位置**    |             **说明**              |
| :------------: | :----------: | :-----------: | :-------------------------------: |
| caesar_decrypt |    string    |   crypto.py   |           凯撒密码解密            |
|   **参数名**   | **是否可空** | **传参类型**  |             **说明**              |
|     string     |    False     |    string     |          需要解密的内容           |
|     shift      |    False     | int or string | 偏移量，传入可为string，会转换int |

##### 使用示例

```python
from qsnctf import *

a = caesar_encrypt('qsnctf', 8)
print(a) # yavkbn
b = caesar_decrypt('yavkbn', 8)
print(b) # qsnctf
```

#### 凯撒密码爆破

##### caesar_decrypt_cracking

|       **函数名**        | **返回类型** |   **位置**   |     **说明**     |
| :---------------------: | :----------: | :----------: | :--------------: |
| caesar_decrypt_cracking |     json     |  crypto.py   | 凯撒密码解密爆破 |
|       **参数名**        | **是否可空** | **传参类型** |     **说明**     |
|       ciphertext        |    False     |    string    |    需要的内容    |

##### caesar_encrypt_cracking

|       **函数名**        | **返回类型** |   **位置**   |     **说明**     |
| :---------------------: | :----------: | :----------: | :--------------: |
| caesar_encrypt_cracking |     json     |  crypto.py   | 凯撒密码加密爆破 |
|       **参数名**        | **是否可空** | **传参类型** |     **说明**     |
|       ciphertext        |    False     |    string    |  需要加密的内容  |

##### 使用示例

```python
from qsnctf import *

a = caesar_encrypt_cracking('qsnctf')
print(a) # {"1": "rtodug", "2": "supevh", "3": "tvqfwi", "4": "uwrgxj", "5": "vxshyk", "6": "wytizl", "7": "xzujam", "8": "yavkbn", "9": "zbwlco", "10": "acxmdp", "11": "bdyneq", "12": "cezofr", "13": "dfapgs", "14": "egbqht", "15": "fhcriu", "16": "gidsjv", "17": "hjetkw", "18": "ikfulx", "19": "jlgvmy", "20": "kmhwnz", "21": "lnixoa", "22": "mojypb", "23": "npkzqc", "24": "oqlard", "25": "prmbse"}

b = caesar_decrypt_cracking('yavkbn')
print(b) # {"1": "xzujam", "2": "wytizl", "3": "vxshyk", "4": "uwrgxj", "5": "tvqfwi", "6": "supevh", "7": "rtodug", "8": "qsnctf", "9": "prmbse", "10": "oqlard", "11": "npkzqc", "12": "mojypb", "13": "lnixoa", "14": "kmhwnz", "15": "jlgvmy", "16": "ikfulx", "17": "hjetkw", "18": "gidsjv", "19": "fhcriu", "20": "egbqht", "21": "dfapgs", "22": "cezofr", "23": "bdyneq", "24": "acxmdp", "25": "zbwlco"}

```

**注意：加密爆破和解密爆破的最终返回均为json，两个集是完全不同的，加密爆破是考虑偏题题点写的，所以不要混为一谈。**

#### 培根密码

##### bacon_encrypt

|  **函数名**   | **返回类型** |   **位置**   |    **说明**    |
| :-----------: | :----------: | :----------: | :------------: |
| bacon_encrypt |    string    |  crypto.py   |  培根密码加密  |
|  **参数名**   | **是否可空** | **传参类型** |    **说明**    |
|    string     |    False     |    string    | 需要加密的内容 |

##### bacon_decrypt

|  **函数名**   | **返回类型** |   **位置**   |                  **说明**                  |
| :-----------: | :----------: | :----------: | :----------------------------------------: |
| bacon_decrypt |    string    |  crypto.py   |                培根密码解密                |
|  **参数名**   | **是否可空** | **传参类型** |                  **说明**                  |
|    string     |    False     |    string    | 需要解密的内容，如果出现小写一定要转为大写 |

##### 使用示例

```python
from qsnctf import *

a = bacon_encrypt('qsnctf')
print(a) # BAAAABAABAABBABAAABABAABBAABAB
b = bacon_decrypt('BAAAABAABAABBABAAABABAABBAABAB')
print(b) # QSNCTF
```

#### ROT13

##### rot13

| **函数名** | **返回类型** |   **位置**   |       **说明**       |
| :--------: | :----------: | :----------: | :------------------: |
|   rot13    |    string    |  crypto.py   |        rot13         |
| **参数名** | **是否可空** | **传参类型** |       **说明**       |
|    text    |    False     |    string    | 需要加密或解密的内容 |

##### 使用示例

```python
from qsnctf import *

a = rot13('qsnctf')
print(a) # dfapgs
b = rot13('dfapgs')
print(b) # qsnctf
```

#### ROT5

##### rot5

| **函数名** | **返回类型** |   **位置**   |       **说明**       |
| :--------: | :----------: | :----------: | :------------------: |
|    rot5    |    string    |  crypto.py   |         rot5         |
| **参数名** | **是否可空** | **传参类型** |       **说明**       |
|    text    |    False     |    string    | 需要加密或解密的内容 |

##### 使用示例

```python
from qsnctf import *

a = rot5('12345')
print(a) # 6789021
b = rot5('67890')
print(b) # 12345
```

#### ROT18

##### rot18

| **函数名** | **返回类型** |   **位置**   |       **说明**       |
| :--------: | :----------: | :----------: | :------------------: |
|   rot18    |    string    |  crypto.py   |        rot18         |
| **参数名** | **是否可空** | **传参类型** |       **说明**       |
|    text    |    False     |    string    | 需要加密或解密的内容 |

##### 使用示例

```python
from qsnctf import *

a = rot18('qsnctf2022')
print(a) # dfapgs7577
b = rot18('dfapgs7577')
print(b) # qsnctf2022
```

## Hash.py

### Hash

#### MD5

##### md5

|  **函数名**  | **返回类型** |   **位置**   |    **说明**    |
| :----------: | :----------: | :----------: | :------------: |
|     md5      |    string    |   hash.py    |      md5       |
|  **参数名**  | **是否可空** | **传参类型** |    **说明**    |
| input_string |    False     |    string    | 需要加密的内容 |

##### 使用示例

```python
from qsnctf import *

a = md5('qsnctf2022')
print(a) # cede1574f851cb8a1ffb3c1b885c4965
```

#### SHA1

##### sha1

|  **函数名**  | **返回类型** |   **位置**   |    **说明**    |
| :----------: | :----------: | :----------: | :------------: |
|     sha1     |    string    |   hash.py    |      sha1      |
|  **参数名**  | **是否可空** | **传参类型** |    **说明**    |
| input_string |    False     |    string    | 需要加密的内容 |

##### 使用示例

```python
from qsnctf import *

a = sha1('qsnctf2022')
print(a) # 5a66dd2590a911dc670873e12934e6f14d1da7e7
```



#### SHA224

##### sha224

|  **函数名**  | **返回类型** |   **位置**   |    **说明**    |
| :----------: | :----------: | :----------: | :------------: |
|    sha224    |    string    |   hash.py    |     sha224     |
|  **参数名**  | **是否可空** | **传参类型** |    **说明**    |
| input_string |    False     |    string    | 需要加密的内容 |

##### 使用示例

```python
from qsnctf import *

a = sha224('qsnctf2022')
print(a) # 71e718c88621bfe602833420a817398aee52df7ef9c1904086c9ff8f
```



#### SHA256

##### sha256

|  **函数名**  | **返回类型** |   **位置**   |    **说明**    |
| :----------: | :----------: | :----------: | :------------: |
|    sha256    |    string    |   hash.py    |     sha256     |
|  **参数名**  | **是否可空** | **传参类型** |    **说明**    |
| input_string |    False     |    string    | 需要加密的内容 |

##### 使用示例

```python
from qsnctf import *

a = sha256('qsnctf2022')
print(a) # 7404bb484d7a4a1f26bf974dc1337d778162d32be0d54f2e571f4e942673b7d1
```

#### SHA384

##### sha384

|  **函数名**  | **返回类型** |   **位置**   |    **说明**    |
| :----------: | :----------: | :----------: | :------------: |
|    sha384    |    string    |   hash.py    |     sha384     |
|  **参数名**  | **是否可空** | **传参类型** |    **说明**    |
| input_string |    False     |    string    | 需要加密的内容 |

##### 使用示例

```python
from qsnctf import *

a = sha384('qsnctf2022')
print(a) # c692736bfeccbaa1e7f1fff9e351d67f042e5198ae8850401be46450b479f62d78e44f46300b13f5419eb5bf1fa0c222
```

#### SHA512

##### sha512

|  **函数名**  | **返回类型** |   **位置**   |    **说明**    |
| :----------: | :----------: | :----------: | :------------: |
|    sha512    |    string    |   hash.py    |     sha512     |
|  **参数名**  | **是否可空** | **传参类型** |    **说明**    |
| input_string |    False     |    string    | 需要加密的内容 |

##### 使用示例

```python
from qsnctf import *

a = sha512('qsnctf2022')
print(a) # bfb5c9d6c5197696c251fad40932da2dfd3af627bf974b09a98c02b55301e58a8f6f0518b74b05a19f7f9f90340a0b81d76e7cc37802406392ebf0f0073c5301 
```

#### SHAKE128

##### shake128

|  **函数名**  | **返回类型** |   **位置**    |           **说明**           |
| :----------: | :----------: | :-----------: | :--------------------------: |
|  shake_128   |    string    |    hash.py    |           shake128           |
|  **参数名**  | **是否可空** | **传参类型**  |           **说明**           |
| input_string |    False     |    string     |        需要加密的内容        |
|     bits     |    False     | int or string | 用于指定输出的散列值的长度。 |

##### 使用示例

```python
from qsnctf import *

a = shake_128('qsnctf2022',"10")
print(a) # b134959f759d7fa1942c
```

#### SHAKE256

##### shake256

|  **函数名**  | **返回类型** |   **位置**    |           **说明**           |
| :----------: | :----------: | :-----------: | :--------------------------: |
|  shake_256   |    string    |    hash.py    |           shake256           |
|  **参数名**  | **是否可空** | **传参类型**  |           **说明**           |
| input_string |    False     |    string     |        需要加密的内容        |
|     bits     |    False     | int or string | 用于指定输出的散列值的长度。 |

##### 使用示例

```python
from qsnctf import *

a = shake_256('qsnctf2022',"10")
print(a) # 94c31528e7a32076b1f4
```

#### HMAC-SHA256

##### hmac-sha256

|   **函数名**    | **返回类型** |   **位置**    |    **说明**    |
| :-------------: | :----------: | :-----------: | :------------: |
| HMAC_SHA256_HEX |    string    |    hash.py    |  hmac_sha256   |
|   **参数名**    | **是否可空** | **传参类型**  |    **说明**    |
|     secret      |    False     |    string     | 需要加密的内容 |
|      data       |    False     | int or string |   加密的密钥   |

##### 使用示例

```python
from qsnctf import *

a = HMAC_SHA256_HEX('qsnctf2022',123)
print(a) # f7ce26af7e17adebd72d3cd9120fa4acd05c66aab676462026e916a53a71f564
```

#### SHA3_224

##### sha3_224

|  **函数名**  | **返回类型** |   **位置**   |    **说明**    |
| :----------: | :----------: | :----------: | :------------: |
|   sha3_224   |    string    |   hash.py    |    sha3_224    |
|  **参数名**  | **是否可空** | **传参类型** |    **说明**    |
| input_string |    False     |    string    | 需要加密的内容 |

##### 使用示例

```python
from qsnctf import *

a = sha3_224('qsnctf2022')
print(a) # 2b7580cd6d4f6a8c3b96d4d08bcbf9e8ddf6d3c393cffb69dd7bc967
```

#### SHA3_256

##### sha3_256

|  **函数名**  | **返回类型** |   **位置**   |    **说明**    |
| :----------: | :----------: | :----------: | :------------: |
|   sha3_256   |    string    |   hash.py    |    sha3_256    |
|  **参数名**  | **是否可空** | **传参类型** |    **说明**    |
| input_string |    False     |    string    | 需要加密的内容 |

##### 使用示例

```python
from qsnctf import *

a = sha3_256('qsnctf2022')
print(a) # ec570495a42596f49037c6f72a93c3a5803a040146a53e7f030cd7c11c0b1c79
```

#### SHA3_384

##### sha3_384

|  **函数名**  | **返回类型** |   **位置**   |    **说明**    |
| :----------: | :----------: | :----------: | :------------: |
|   sha3_384   |    string    |   hash.py    |    sha3_384    |
|  **参数名**  | **是否可空** | **传参类型** |    **说明**    |
| input_string |    False     |    string    | 需要加密的内容 |

##### 使用示例

```python
from qsnctf import *

a = sha3_384('qsnctf2022')
print(a) # f3df64859a8e1b1912e1b237f1b54863fb6f11ca9bc117e019e69ceb4d7e1cacd75c8d33b1e25967428d8a7b3cee23f5
```

#### SHA3_512

##### sha3_512

|  **函数名**  | **返回类型** |   **位置**   |    **说明**    |
| :----------: | :----------: | :----------: | :------------: |
|   sha3_512   |    string    |   hash.py    |    sha3_512    |
|  **参数名**  | **是否可空** | **传参类型** |    **说明**    |
| input_string |    False     |    string    | 需要加密的内容 |

##### 使用示例

```python
from qsnctf import *

a = sha3_512('qsnctf2022')
print(a) # 95e2d7d428f1b4d007be25dfd454131796f6fa2162662ec34fe8a9aa52f463f5021d5c32cfc422ea3055ed666afb1fc9edc86e65a3f57129ce2d7b2e7617e71e
```

 
