# 🤔What is QSNCTF？

[青少年CTF训练平台](https://www.qsnctf.com/)是一个公益、免费、供给全国青少年学习、训练的CTF在线平台。

[（本仓库）](https://github.com/Moxin1044/qsnctf-python)qsnctf是青少年CTF训练平台进行编写的一个Python包程序，意图在Python中为大家快速使用一些CTF常用功能开发的开源包。这里有很多CTF常用功能，如Base编码、hash加密，甚至少见的社会主义核心价值观编码、quipqiup等都在其中。

当前项目将长期更新

如果您有好的想法和建议，欢迎与我取得联系：QQ：1044631097。

![Alt](https://repobeats.axiom.co/api/embed/351178f679198f07b9f9715948c6c3e011834759.svg "Repobeats analytics image")

## 安装

首先将GitHub上的项目下载下来后可以文件中有一个`setup.py`

打开终端然后输入

```bash
python setup.py install
```

或者也可以直接使用pip来进行安装**（由于本Python库仍在开发，所以pip可能不是最新版，如果您有较高的需求，可以直接clone本仓库进行安装）**

```bash
pip install qsnctf
```

也可以使用以下命令来更新此库

```bash
pip install --upgrade qsnctf
```

如果你想知道具体怎么使用可以导入这个包，然后使用`help(qsnctf)`查看库的用法

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

然后使用help(qsnctf.PACKAGE CONTENTS)来查看具体的使用方法

## 安全默认行为

从当前版本开始，网络扫描、压缩包爆破和消息/API 客户端在构造对象时不会自动执行操作，需要显式调用对应方法：

`python
scanner = DirScan("https://example.com", dirlist=["/admin"])
scanner.run()

webhook = FeishuWebhook("标题", "内容", "token")
webhook.send()
`

如需兼容原有的一行式调用，可传入 uto_run=True、uto_send=True、uto_solve=True 或 uto_validate=True。所有 HTTP 请求现在默认设置超时，Web 请求默认验证 TLS 证书。
## 演示

查看`base`的使用方法

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


# 功能列表

### BASE

|    base16    | base32 | base36 | base58 | base62  |
| :----------: | :----: | :----: | :----: | :-----: |
|    base64    | base85 | base91 | base92 | base100 |
| 自定义base64 |        |        |        |         |

### CRYPTO

| 凯撒密码 | 凯撒爆破 |  培根密码  |          ROT5          | ROT13 |
| :------: | :------: | :--------: | :--------------------: | :---: |
|  ROT18   | 八卦密码 | 埃特巴什码 | 摩斯密码（支持自定义） |       |

### MD5

|   md5    |   sha1   |  sha224  |   sha256    |  sha384  |
| :------: | :------: | :------: | :---------: | :------: |
|  sha512  | shake128 | shake256 | HMAC-SHA256 | sha3-224 |
| sha3-256 | sha3-385 | sha3-512 |             |          |



### MISC

|   核心价值观加密解密   |  文本逆向  | url加密解密 |   位异或    | 文本逆向（步长2） |
| :--------------------: | :--------: | :---------: | :---------: | :---------------: |
| 文本逆向（自定义步长） |  获取uuid  | ord转字符串 | 字符串转ord |    字符串分割     |
|        flag寻找        | 百家姓编码 | Qwerty编码  |   HTM编码   |      JSFUCK       |
|        AAencode        |  str2hex   |   hex2str   | ZIP密码爆破 | ZIP解压缩（高级） |

### API

| quipqiup词频分析 | 飞书Webhook |  钉钉Talk  | 微步在线 | FOFA |
| :--------------: | :---------: | :--------: | :------: | :--: |
|    大圣云沙箱    |  零零信安   | Go-CQ-HTTP |          |      |

### WEB

|   目录扫描   | 网站存活检测  |   取网站标题    | 子域名扫描 |   取网站描述   |
| :----------: | :-----------: | :-------------: | :--------: | :------------: |
| 取网站关键字 |   取网站ICP   | 取网站a标签地址 | 取网站注释 | 取网站响应时间 |
|  取网站ICO   | POST Webshell |  GET Webshell   | exec-shell |   eval-shell   |
| WebShell爆破 |               |                 |            |                |

# 具体使用

## 命令行使用

第一步导入`qsnctf`库

```python
from qsnctf import *
```

例如需要使用`base64`编码

```python
base64_encode("需要编码的")# 6ZyA6KaB57yW56CB55qE
```

相同如果使用`base64`解码的话就是

```python
 base64_decode("6ZyA6KaB57yW56CB55qE")# 需要编码的
```

其他的编码解码类似

------

## 编译器使用

这里还是使用base64来演示，其他的编码解码类似。

```python
from qsnctf import qsnctf

a=base64_encode("需要编码的")
print(a)
b=base64_decode("6ZyA6KaB57yW56CB55qE")
print(b)
```

`返回信息`
需要编码的
```
6ZyA6KaB57yW56CB55qE

```

**Base62的encode值应该是整数！**

```python
from qsnctf import qsnctf

a = base62_encode(34441886726)
print(a)
b = base62_decode("base62")
print(b)
```

## 传参方法

文档移动到：[Function.md](https://github.com/Moxin1044/qsnctf-python/blob/master/docs/Function.md)

## 环境

### 开发环境

`Windows11 + Python3.11`

### 使用环境

支持 `python 3.x` 环境。

文档持续更新。

## ✨ Contributors

感谢下面的所有人：

<table>
  <tr>
    <td align="center"><a href="https://github.com/Moxin1044"><img src="https://avatars.githubusercontent.com/u/59173630?v=4" width="100px;" alt=""/><br /><sub><b>Moxin</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/wang256814742"><img src="https://avatars.githubusercontent.com/u/75202489?v=4" width="100px;" alt=""/><br /><sub><b>xinyi</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/yiye-yfs"><img src="https://avatars.githubusercontent.com/u/79006318?v=4" width="100px;" alt=""/><br /><sub><b>yiye-yfs</b></sub></a><br /></td>
  </tr>
</table>
