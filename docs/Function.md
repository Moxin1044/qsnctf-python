# 函数库 - 我应该如何使用

由于Base、各种加密的方法较多，传参方法也花样百出。这里给大家写出这个文档方便参考，包含了供给大家使用的函数的说明、注意事项、参数和返回值等信息。

## Web.py

### Scan

#### class-DirScan

##### DirScan

| **函数名**  | **返回类型** |   **位置**   |                           **说明**                           |
| :---------: | :----------: | :----------: | :----------------------------------------------------------: |
|   DirScan   |     list     |    web.py    |                         网站目录扫描                         |
| **参数名**  | **是否可空** | **传参类型** |                           **说明**                           |
|     url     |    False     |    string    | 网站地址，格式：https://bbs.qsnctf.com 如果后面存在/会自动删去 |
|  treadline  |     True     |     int      |        线程数（需要传整数）不可以太高了哦 默认10线程         |
| sleep_time  |     True     |     int      |                   每次扫描间隔时间 默认是0                   |
|   dirlist   |     True     |     list     | DirScan的列表，格式['/www.zip','/index.php'] 默认扫描库路径下的/plugin/txt/dirs.txt中的内容 |
| return_code |     True     |     list     | 返回结果的状态列表，格式[200, 301, 302, 401, 403, 500] ，格式也是默认值 |
|    echo     |     True     |   Boolean    |              是否直接输出扫描结果 默认值为False              |
|    wait     |     True     |   Boolean    |                是否等待线程结束 默认值为True                 |
|   Cookie    |     True     |    string    |                       网站Cookie，可空                       |

**说明：请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

dir = DirScan('https://bbs.qsnctf.com/', 10, 0.5, auto_run=True)
print(dir.results_code) # ['https://bbs.qsnctf.com/robots.txt 200', 'https://bbs.qsnctf.com/admin.php 200', 'https://bbs.qsnctf.com/sitemap.txt 200', 'https://bbs.qsnctf.com/sitemap.xml 200']
# 下面的结果中只会存在返回的请求
print(dir.results) # ['https://bbs.qsnctf.com/robots.txt', 'https://bbs.qsnctf.com/admin.php', 'https://bbs.qsnctf.com/sitemap.txt', 'https://bbs.qsnctf.com/sitemap.xml']

DirScan('https://bbs.qsnctf.com/', 100, 0.1, echo=True, auto_run=True) # 将会直接进行扫描并打印结果（这样在显示上更快，但是效率同上）
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

| **函数名**  | **返回类型** |   **位置**   |                           **说明**                           |
| :---------: | :----------: | :----------: | :----------------------------------------------------------: |
|   UrlScan   |     list     |    web.py    |                         网站状态扫描                         |
| **参数名**  | **是否可空** | **传参类型** |                           **说明**                           |
|  url_list   |    False     |    string    | 网站地址，格式：https://bbs.qsnctf.com 如果后面存在/会自动删去 |
|  treadline  |     True     |     int      |        线程数（需要传整数）不可以太高了哦 默认10线程         |
| sleep_time  |     True     |     int      |                   每次扫描间隔时间 默认是0                   |
| return_code |     True     |     list     | 返回结果的状态列表，格式[200, 301, 302, 401, 403, 404, 500] ，格式也是默认值 |
|    echo     |     True     |   Boolean    |              是否直接输出扫描结果 默认值为False              |
|    wait     |     True     |   Boolean    |                是否等待线程结束 默认值为True                 |
|   Cookie    |     True     |    string    |                       网站Cookie，可空                       |

**说明：请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

list = ["https://bbs.qsnctf.com/admin.php", "https://bbs.qsnctf.com/robots.txt", "https://www.qsnctf.com/"]
dir = UrlScan(list, 10, 0.5, auto_run=True)
print(dir.results_code) # ['https://bbs.qsnctf.com/robots.txt 200', 'https://bbs.qsnctf.com/admin.php 200', 'https://www.qsnctf.com/ 200']
# 下面的结果中只会存在返回的请求
print(dir.results) # ['https://bbs.qsnctf.com/robots.txt', 'https://bbs.qsnctf.com/admin.php', 'https://www.qsnctf.com/']
UrlScan(list, 100, 0.1, echo=True, auto_run=True) # 将会直接进行扫描并打印结果（这样在显示上更快，但是效率同上）
"""
https://bbs.qsnctf.com/robots.txt 200 No Title
https://bbs.qsnctf.com/admin.php 200 登录管理中心
https://www.qsnctf.com/ 200 青少年CTF训练平台 | 原中学生CTF平台 | 青少年CTF
"""
```

**说明：No Title是没有找到HTML网页中的Title标签**

#### class-DomainScan

##### DomainScan

| **函数名**  | **返回类型** |   **位置**   |                           **说明**                           |
| :---------: | :----------: | :----------: | :----------------------------------------------------------: |
| DomainScan  |     list     |    web.py    |                          子域名扫描                          |
| **参数名**  | **是否可空** | **传参类型** |                           **说明**                           |
|   domain    |    False     |    string    |                  网站域名，格式：qsnctf.com                  |
|  treadline  |     True     |     int      |        线程数（需要传整数）不可以太高了哦 默认10线程         |
| sleep_time  |     True     |     int      |                   每次扫描间隔时间 默认是0                   |
| domainlist  |     True     |     list     | 扫描的子域名列表，格式['abc','www'] 默认扫描库路径下的/plugin/txt/domain.txt中的内容 |
| return_code |     True     |     list     | 返回结果的状态列表，格式[200, 301, 302, 401, 403, 404, 500] ，格式也是默认值 |
|    echo     |     True     |   Boolean    |              是否直接输出扫描结果 默认值为False              |
|    wait     |     True     |   Boolean    |                是否等待线程结束 默认值为True                 |

**说明：请注意比赛规则进行使用。**

```python
from qsnctf import *

a = DomainScan("qsnctf.com", auto_run=True)
print(a.results_title)
# ['http://www.qsnctf.com/ 青少年CTF训练平台 | 原中学生CTF平台 | 青少年CTF', 'http://ctf.qsnctf.com/ 克拉玛依市第一届网络安全技能大赛', 'http://test.qsnctf.com/ 克拉玛依高级中学--十三年', 'http://tools.qsnctf.com/ 青少年CTF在线工具箱 | CTF在线工具']
print(a.results) 
# ['http://www.qsnctf.com/', 'http://ctf.qsnctf.com/', 'http://test.qsnctf.com/', 'http://tools.qsnctf.com/']

```

### 取网站信息

#### 取网站标题

##### get_url_title

|  **函数名**   | **返回类型** |   **位置**   |     **说明**     |
| :-----------: | :----------: | :----------: | :--------------: |
| get_url_title |    string    |    web.py    |    取网站标题    |
|  **参数名**   | **是否可空** | **传参类型** |     **说明**     |
|      url      |    False     |    string    |     网站地址     |
|    Cookie     |     True     |    string    | 网站Cookie，可空 |

**说明：请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

a = get_url_title("https://www.baidu.com/")
print(a) # 百度一下，你就知道
```

**说明：No Title是没有找到HTML网页中的Title标签**

#### 取网站描述

##### get_url_description

|     **函数名**      | **返回类型** |   **位置**   |     **说明**     |
| :-----------------: | :----------: | :----------: | :--------------: |
| get_url_description |    string    |    web.py    |    取网站描述    |
|     **参数名**      | **是否可空** | **传参类型** |     **说明**     |
|         url         |    False     |    string    |     网站地址     |
|       Cookie        |     True     |    string    | 网站Cookie，可空 |

**说明：请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *


a = get_url_description('https://www.qsnctf.com/')
print(a)  # 青少年CTF|青少年CTF训练平台是针对青少年网络安全爱好者的训练平台，平台内有大量原创题，并收录了各大比赛的题目进行公益的学习。我们所有的题目均为免费公开，给广大学子提供更多的学习途径。
```

**说明：No description是没有找到HTML网页中的description标签**

#### 取网站关键词

##### get_url_keywords

|    **函数名**    | **返回类型** |   **位置**   |     **说明**     |
| :--------------: | :----------: | :----------: | :--------------: |
| get_url_keywords |    string    |    web.py    |   取网站关键字   |
|    **参数名**    | **是否可空** | **传参类型** |     **说明**     |
|       url        |    False     |    string    |     网站地址     |
|      Cookie      |     True     |    string    | 网站Cookie，可空 |

**说明：请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *


a = get_url_keywords('https://www.qsnctf.com/')
print(a)  # 青少年CTF,青少年CTF平台,青少年CTF训练平台,中学生CTF平台,中学生CTF训练平台,青少年网络安全,青少年CTF在线训练平台,CTF训练平台,CTF平台
```

**说明：No keywords是没有找到HTML网页中的keywords标签**

#### 取网站ICP备案号

##### get_url_ICP

| **函数名**  | **返回类型** |   **位置**   |     **说明**     |
| :---------: | :----------: | :----------: | :--------------: |
| get_url_ICP |    string    |    web.py    | 取网站ICP备案号  |
| **参数名**  | **是否可空** | **传参类型** |     **说明**     |
|     url     |    False     |    string    |     网站地址     |
|   Cookie    |     True     |    string    | 网站Cookie，可空 |

**说明：请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *


a = get_url_ICP('https://www.qsnctf.com/')
print(a)  # 备案号：鲁ICP备2022011740号-3
```

**说明：No ICP是没有找到HTML网页中的ICP标签**

#### 取网站中的href地址

##### get_url_a_href

|   **函数名**   | **返回类型** |   **位置**   |     **说明**      |
| :------------: | :----------: | :----------: | :---------------: |
| get_url_a_href |     list     |    web.py    | 取网站a标签的href |
|   **参数名**   | **是否可空** | **传参类型** |     **说明**      |
|      url       |    False     |    string    |     网站地址      |
|     Cookie     |     True     |    string    | 网站Cookie，可空  |

**说明：请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *


a = get_url_a_href('https://www.qsnctf.com/')
print(a)  # ['/', 'login', 'http://bbs.qsnctf.com/', 'javascript:;', 'https://www.sierting.com', 'https://beian.miit.gov.cn']
```

**说明：No href是没有找到HTML网页中的href标签**

#### 取网站中的URL地址

##### get_url_img

| **函数名**  | **返回类型** |   **位置**   |     **说明**     |
| :---------: | :----------: | :----------: | :--------------: |
| get_url_img |     list     |    web.py    |    取网站img     |
| **参数名**  | **是否可空** | **传参类型** |     **说明**     |
|     url     |    False     |    string    |     网站地址     |
|   Cookie    |     True     |    string    | 网站Cookie，可空 |

**说明：请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *


a = get_url_a_href('https://www.qsnctf.com/')
print(a)  # ['/logo.png', 'data/attachment/block/b8/b85a300493f1bd7ef7e0268dec2c3217.jpg']
```

**说明：No src是没有找到HTML网页中的src标签**

#### 取网站的注释

##### get_url_comment

|   **函数名**    | **返回类型** |   **位置**   |     **说明**     |
| :-------------: | :----------: | :----------: | :--------------: |
| get_url_comment |     list     |    web.py    |   取网站中注释   |
|   **参数名**    | **是否可空** | **传参类型** |     **说明**     |
|       url       |    False     |    string    |     网站地址     |
|     Cookie      |     True     |    string    | 网站Cookie，可空 |

**说明：请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *


a = get_url_comment('https://www.qsnctf.com/')
print(a)  # ['baidutongji']
```

**说明：No comment是没有找到HTML网页中的注释节点**

#### 取网站响应时间

##### get_url_time

|  **函数名**  | **返回类型** |   **位置**   |    **说明**    |
| :----------: | :----------: | :----------: | :------------: |
| get_url_time |    string    |    web.py    | 取网站响应时间 |
|  **参数名**  | **是否可空** | **传参类型** |    **说明**    |
|     url      |    False     |    string    |    网站地址    |

**说明：请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *


a = get_url_time('https://www.qsnctf.com/')
print(a)  # ['0.0155']
```

#### 取网站的ICO

##### get_url_ico

| **函数名**  | **返回类型** |   **位置**   |   **说明**    |
| :---------: | :----------: | :----------: | :-----------: |
| get_url_ico |    string    |    web.py    | 取网站ico地址 |
| **参数名**  | **是否可空** | **传参类型** |   **说明**    |
|     url     |    False     |    string    |   网站地址    |

**说明：请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *


a = get_url_ico('https://www.qsnctf.com/')
print(a)  # ['/ico.ico']
```

### WebShell操作

**此功能仅限CTF和管理自己的网站使用，请勿用于非法用途。**

#### POST方式测试WebShell密码

##### get_webshell_post

|    **函数名**     | **返回类型** |   **位置**   |   **说明**   |
| :---------------: | :----------: | :----------: | :----------: |
| get_webshell_post |    string    |    web.py    | 测试Webshell |
|    **参数名**     | **是否可空** | **传参类型** |   **说明**   |
|        url        |    False     |    string    |  shell地址   |
|        key        |    False     |    string    |     key      |

**说明：请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *


a = get_webshell_post('http://localhost/shell.php', 'cmd')
print(a) # True
```

#### GET方式测试WebShell密码

##### get_webshell_get

|    **函数名**    | **返回类型** |   **位置**   |   **说明**   |
| :--------------: | :----------: | :----------: | :----------: |
| get_webshell_get |    string    |    web.py    | 测试Webshell |
|    **参数名**    | **是否可空** | **传参类型** |   **说明**   |
|       url        |    False     |    string    |  shell地址   |
|       key        |    False     |    string    |     key      |

**说明：请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *


a = get_webshell_get('http://localhost/shell.php', 'cmd')
print(a) # True
```

#### exec-webshell命令执行（POST）

##### get_exec_webshell_post

|       **函数名**       | **返回类型** |   **位置**   |   **说明**   |
| :--------------------: | :----------: | :----------: | :----------: |
| get_exec_webshell_post |    string    |    web.py    | exec命令执行 |
|       **参数名**       | **是否可空** | **传参类型** |   **说明**   |
|          url           |    False     |    string    |  shell地址   |
|          key           |    False     |    string    |     key      |
|         shell          |    Fasle     |    string    |  执行的命令  |

**说明：请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *


a = get_exec_webshell_post('http://localhost/shell.php', 'cmd', 'whoami')
print(a) # root
```

#### exec-webshell命令执行（get）

##### get_exec_webshell_get

|      **函数名**       | **返回类型** |   **位置**   |   **说明**   |
| :-------------------: | :----------: | :----------: | :----------: |
| get_exec_webshell_get |    string    |    web.py    | exec命令执行 |
|      **参数名**       | **是否可空** | **传参类型** |   **说明**   |
|          url          |    False     |    string    |  shell地址   |
|          key          |    False     |    string    |     key      |
|         shell         |    Fasle     |    string    |  执行的命令  |

**说明：请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *


a = get_exec_webshell_get('http://localhost/shell.php', 'cmd', 'whoami')
print(a) # root
```

#### eval-webshell代码执行（get）

##### get_eval_webshell_get

|      **函数名**       | **返回类型** |   **位置**   |   **说明**   |
| :-------------------: | :----------: | :----------: | :----------: |
| get_eval_webshell_get |    string    |    web.py    | eval代码执行 |
|      **参数名**       | **是否可空** | **传参类型** |   **说明**   |
|          url          |    False     |    string    |  shell地址   |
|          key          |    False     |    string    |     key      |
|         shell         |    Fasle     |    string    |  执行的代码  |

**说明：请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *


a = get_eval_webshell_get('http://localhost/shell.php', 'cmd', 'print("123");')
print(a) # 123
```

#### eval-webshell代码执行（post）

##### get_eval_webshell_post

|       **函数名**       | **返回类型** |   **位置**   |   **说明**   |
| :--------------------: | :----------: | :----------: | :----------: |
| get_eval_webshell_post |    string    |    web.py    | eval代码执行 |
|       **参数名**       | **是否可空** | **传参类型** |   **说明**   |
|          url           |    False     |    string    |  shell地址   |
|          key           |    False     |    string    |     key      |
|         shell          |    Fasle     |    string    |  执行的代码  |

**说明：请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *


a = get_eval_webshell_post('http://localhost/shell.php', 'cmd', 'print("123");')
print(a) # 123
```

#### WebShell爆破

##### WebShellCracking

|    **函数名**    | **返回类型** |   **位置**   |       **说明**        |
| :--------------: | :----------: | :----------: | :-------------------: |
| WebShellCracking |    string    |    web.py    |   WebShell密码爆破    |
|    **参数名**    | **是否可空** | **传参类型** |       **说明**        |
|       url        |    False     |    string    |       shell地址       |
|    threadline    |    False     |     int      |        线程数         |
|    sleep_time    |    Fasle     |     int      |       访问延时        |
|     passlist     |    False     |     list     |    可能的密码列表     |
|       mode       |    False     |    string    | GET or POST 默认 POST |

**说明：请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *


a = WebShellCracking('http://localhost/shell.php', threadline=50, mode="GET", auto_run=True)
print(a.results) # cmd
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

a = quipqiup('test', auto_solve=True)
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

FeishuWebhook('青少年CTF', '你好，我是末心', 'xxxx-xxxxx-xxxx-xxxx-xxxxx', 'card', auto_send=True)
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

DingTalk('青少年CTF', '你好，我是末心', 'xxxx-xxxxx-xxxx-xxxx-xxxxx', auto_send=True)
```

### 微步在线

#### class-ThreatBook

##### ThreatBook

| **函数名** | **返回类型** |   **位置**   |    **说明**     |
| :--------: | :----------: | :----------: | :-------------: |
| ThreatBook |    object    |    api.py    |    微步在线     |
| **参数名** | **是否可空** | **传参类型** |    **说明**     |
|  api_key   |    False     |    string    | 微步在线API Key |

API Key 获取地址：https://x.threatbook.com/v5/myApi

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

tb = ThreatBook('***') # 主要是配合下面的调用返回的一个对象
```

#### 微步-IP信誉

##### ip_reputation

|  **函数名**   | **返回类型** |   **位置**   |     **说明**     |
| :-----------: | :----------: | :----------: | :--------------: |
| ip_reputation |     json     |    api.py    |  微步在线IP信誉  |
|  **参数名**   | **是否可空** | **传参类型** |     **说明**     |
|      ip       |    False     |    string    | 需要查询的IP地址 |

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

tb = ThreatBook('***')
a = tb.ip_reputation('127.0.0.1')
print(a)
```

```json
{'data': {'127.0.0.1': {'severity': '无威胁', 'judgments': ['白名单', '保留地址'], 'tags_classes': [], 'basic': {'carrier': '', 'location': {'country': '', 'province': '', 'city': '', 'lng': '', 'lat': '', 'country_code': 'B1'}}, 'asn': {}, 'scene': '', 'confidence_level': '高', 'is_malicious': False, 'update_time': '2023-01-05 18:41:54'}}, 'response_code': 0, 'verbose_msg': '成功'}

```

#### 文件上传分析

##### file_upload

|  **函数名**  | **返回类型** |   **位置**   |                **说明**                 |
| :----------: | :----------: | :----------: | :-------------------------------------: |
| file_upload  |     json     |    api.py    |       微步文件反病毒引擎检测报告        |
|  **参数名**  | **是否可空** | **传参类型** |                **说明**                 |
|  file_path   |    False     |    string    |               上传的路径                |
|  file_name   |    False     |    string    |            需要上传的文件名             |
| sandbox_type |     True     |    string    | 沙箱环境，默认win7_sp1_enx64_office2013 |

 沙箱运行环境，用户可以指定文件的沙箱运行环境，可选环境包括：

- **Windows** 
  - win7_sp1_enx64_office2013 
  - win7_sp1_enx86_office2013 
  - win7_sp1_enx86_office2010 
  - win7_sp1_enx86_office2007 
  - win7_sp1_enx86_office2003
- **Linux** 
  - ubuntu_1704_x64 
  - centos_7_x64

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

tb = ThreatBook('***')
a = tb.file_upload('./','1.exe')
print(a)
# {'data': {'sha256': '***', 'permalink': 'https://s.threatbook.cn/search?query=***&type=sha256'}, 'response_code': 0, 'verbose_msg': 'OK'}
```

#### 微步文件反病毒引擎检测报告

##### file_report_multiengines

|        **函数名**        | **返回类型** |   **位置**   |          **说明**          |
| :----------------------: | :----------: | :----------: | :------------------------: |
| file_report_multiengines |     json     |    api.py    | 微步文件反病毒引擎检测报告 |
|        **参数名**        | **是否可空** | **传参类型** |          **说明**          |
|          sha256          |    False     |    string    |        文件的sha256        |

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

tb = ThreatBook('***')
a = tb.file_report_multiengines('******')
print(a)
# {'data': {'multiengines': {'threat_level': 'clean', 'total': 22, 'is_white': False, 'total2': 22, 'positives': 0, 'scan_date': '2023-01-05 19:04:42', 'scans': {'IKARUS': 'safe', 'vbwebshell': 'safe', 'Avast': 'safe', 'Avira': 'safe', 'Sophos': 'safe', 'K7': 'safe', 'Rising': 'safe', 'Kaspersky': 'safe', 'Panda': 'safe', 'Baidu-China': 'safe', 'NANO': 'safe', 'Antiy': 'safe', 'AVG': 'safe', 'Baidu': 'safe', 'DrWeb': 'safe', 'GDATA': 'safe', 'Microsoft': 'safe', 'Qihu360': 'safe', 'ESET': 'safe', 'ClamAV': 'safe', 'JiangMin': 'safe', 'Trustlook': 'safe'}}}, 'response_code': 0, 'verbose_msg': 'OK'}
```

#### 微步文件报告

##### file_report

|  **函数名**  | **返回类型** |   **位置**   |                **说明**                 |
| :----------: | :----------: | :----------: | :-------------------------------------: |
| file_report  |     json     |    api.py    |              微步文件报告               |
|  **参数名**  | **是否可空** | **传参类型** |                **说明**                 |
|    sha256    |    False     |    string    |              文件的sha256               |
| sandbox_type |     True     |    string    | 沙箱环境，默认win7_sp1_enx64_office2013 |

 沙箱运行环境，用户可以指定文件的沙箱运行环境，可选环境包括：

- **Windows** 
  - win7_sp1_enx64_office2013 
  - win7_sp1_enx86_office2013 
  - win7_sp1_enx86_office2010 
  - win7_sp1_enx86_office2007 
  - win7_sp1_enx86_office2003
- **Linux** 
  - ubuntu_1704_x64 
  - centos_7_x64

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

tb = ThreatBook('***')
a = tb.file_report('******')
print(a)

```

### GO-CQ-HTTP

#### class-GoCQHttp

##### GoCQHttp

|  **函数名**   | **返回类型** |   **位置**   |                  **说明**                   |
| :-----------: | :----------: | :----------: | :-----------------------------------------: |
|   GoCQHttp    |    object    |    api.py    |   [GoCQHttp](https://docs.go-cqhttp.org/)   |
|  **参数名**   | **是否可空** | **传参类型** |                  **说明**                   |
|      url      |    False     |    string    | Go-CQ-HTTP URL 如 http://www.baidu.com:1700 |
|     auth      |     True     |   Boolean    |           是否启用了authorization           |
| authorization |     True     |    string    |               authorization值               |

Key 获取地址：https://fofa.info/

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

cq = GoCQHttp('http://www.baidu.com:1700', True, "check me") # 主要是配合下面的调用返回的一个对象
```

#### 发送私聊消息

##### send_private_msg

|    **函数名**    | **返回类型** |   **位置**   |                      **说明**                       |
| :--------------: | :----------: | :----------: | :-------------------------------------------------: |
| send_private_msg |    object    |    api.py    | [GoCQHttp](https://docs.go-cqhttp.org/)发送私聊消息 |
|    **参数名**    | **是否可空** | **传参类型** |                      **说明**                       |
|      userid      |    False     |     int      |                   接收消息的QQ号                    |
|     message      |    False     |    string    |                     发送的内容                      |

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

cq = GoCQHttp('http://www.baidu.com:1700', True, "check me") # 主要是配合下面的调用返回的一个对象
cq.send_private_msg(1044631097, '早上该起床啦！')
```

#### 发送群消息

##### send_group_msg

|   **函数名**   | **返回类型** |   **位置**   |                      **说明**                       |
| :------------: | :----------: | :----------: | :-------------------------------------------------: |
| send_group_msg |    object    |    api.py    | [GoCQHttp](https://docs.go-cqhttp.org/)发送群聊消息 |
|   **参数名**   | **是否可空** | **传参类型** |                      **说明**                       |
|    group_id    |    False     |     int      |                   接收消息的群号                    |
|    message     |    False     |    string    |                     发送的内容                      |

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

cq = GoCQHttp('http://www.baidu.com:1700', True, "check me") # 主要是配合下面的调用返回的一个对象
cq.send_group_msg(797842833, '大家好哦！')
```

### FOFA

#### class-FOFA

##### FOFA

| **函数名** | **返回类型** |   **位置**   |                      **说明**                       |
| :--------: | :----------: | :----------: | :-------------------------------------------------: |
|    FOFA    |    object    |    api.py    | [FOFA_SDK](https://github.com/Moxin1044/pythonfofa) |
| **参数名** | **是否可空** | **传参类型** |                      **说明**                       |
|   email    |    False     |    string    |                     FOFA Email                      |
|    key     |    False     |    string    |                      FOFA Key                       |

Key 获取地址：https://fofa.info/

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

fofa = FOFA('***', 'xxxx', auto_validate=True) # 主要是配合下面的调用返回的一个对象
```

#### FOFA用户信息

##### userinfo

| **函数名** | **返回类型** |   **位置**   |   **说明**    |
| :--------: | :----------: | :----------: | :-----------: |
|  userinfo  |     json     |    api.py    | FOFA 用户信息 |
| **参数名** | **是否可空** | **传参类型** |   **说明**    |

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

fofa = FOFA('***', 'xxxx', auto_validate=True)
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



#### FOFA查询

##### search

| **函数名** | **返回类型** |   **位置**   |                     **说明**                     |
| :--------: | :----------: | :----------: | :----------------------------------------------: |
|   search   |     json     |    api.py    |                FOFA 查询接口调用                 |
| **参数名** | **是否可空** | **传参类型** |                     **说明**                     |
| query_text |    False     |    string    |                 支持FOFA高级语句                 |
|   field    |     True     |    string    |                默认 host,ip,port                 |
|    page    |     True     |     int      |                       页数                       |
|    size    |     True     |     int      |                   每页查询数量                   |
|    full    |     True     |   Boolean    | 默认搜索一年内的数据，指定为true即可搜索全部数据 |

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

fofa = FOFA('***', 'xxxx', auto_validate=True)
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

#### FOFA统计聚合

##### search_stats

|  **函数名**  | **返回类型** |   **位置**   |                           **说明**                           |
| :----------: | :----------: | :----------: | :----------------------------------------------------------: |
| search_stats |     json     |    api.py    |                      FOFA 统计聚合查询                       |
|  **参数名**  | **是否可空** | **传参类型** |                           **说明**                           |
|  query_text  |    False     |    string    |             需要进行查询的语句,即输入的查询内容              |
|    field     |     True     |    string    | 可选字段，默认title，详见[附录2](https://fofa.info/api/stats/statistical) |

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

fofa = FOFA('***', 'xxxx', auto_validate=True)
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

#### FOFA HOST 聚合

##### search_host

| **函数名**  | **返回类型** |   **位置**   |     **说明**      |
| :---------: | :----------: | :----------: | :---------------: |
| search_host |     json     |    api.py    | FOFA HOST聚合查询 |
| **参数名**  | **是否可空** | **传参类型** |     **说明**      |
|    host     |    False     |    string    | host名，通常是ip  |
|   detail    |     True     |   Boolean    |   显示端口详情    |

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

fofa = FOFA('***', 'xxxx', auto_validate=True)
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

### 大圣云沙箱

#### class-DaSheng

##### DaSheng

| **函数名** | **返回类型** |   **位置**   |                      **说明**                      |
| :--------: | :----------: | :----------: | :------------------------------------------------: |
|  DaSheng   |    object    |    api.py    | [大圣云沙箱](https://sandbox.freebuf.com/cloudApi) |
| **参数名** | **是否可空** | **传参类型** |                      **说明**                      |
|     id     |    False     |    string    |                      客户端ID                      |
|    key     |    False     |    string    |                     客户端密钥                     |

Key 获取地址：https://sandbox.freebuf.com/cloudApi

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

ds = DaSheng('***','xxxx') # 主要是配合下面的调用返回的一个对象
```

#### Token获取

##### token

| **函数名** | **返回类型** |   **位置**   |                        **说明**                         |
| :--------: | :----------: | :----------: | :-----------------------------------------------------: |
|   token    |    string    |    api.py    | [大圣云沙箱](https://sandbox.freebuf.com/cloudApi)Token |
| **参数名** | **是否可空** | **传参类型** |                        **说明**                         |

**一般不写操作可能没啥用**

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

ds = DaSheng('***','xxxx')
print(ds.token())
```

#### 文件上传

##### upload

| **函数名** | **返回类型** |   **位置**   | **说明** |
| :--------: | :----------: | :----------: | :------: |
|   upload   |    object    |    api.py    | 样本上传 |
| **参数名** | **是否可空** | **传参类型** | **说明** |
|  file_dir  |    False     |    string    |   路径   |
| file_name  |    False     |    string    |  文件名  |

**一般不写操作可能没啥用**

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

ds = DaSheng('***','xxxx')
print(ds.upload('路径','文件名'))
```

#### 文件上传

##### upload

| **函数名** | **返回类型** |   **位置**   | **说明** |
| :--------: | :----------: | :----------: | :------: |
|   upload   |    object    |    api.py    | 样本查询 |
| **参数名** | **是否可空** | **传参类型** | **说明** |
|    sha1    |    False     |    string    | 文件sha1 |

**一般不写操作可能没啥用**

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

ds = DaSheng('***','xxxx')
print(ds.search('sha1'))
```

### 零零信安

#### class-ZeroZeon

##### ZeroZeon

| **函数名** | **返回类型** |   **位置**   |          **说明**           |
| :--------: | :----------: | :----------: | :-------------------------: |
|  ZeroZeon  |    object    |    api.py    | [零零信安](https://0.zone/) |
| **参数名** | **是否可空** | **传参类型** |          **说明**           |
|    key     |    False     |    string    |           api_key           |

Key 获取地址：https://0.zone/plug-in-unit

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

zero = ZeroZeon('xxxx') # 主要是配合下面的调用返回的一个对象
```

#### 零零信安查询

##### search

| **函数名** | **返回类型** |   **位置**   |                        **说明**                         |
| :--------: | :----------: | :----------: | :-----------------------------------------------------: |
|   search   |     json     |    api.py    | [大圣云沙箱](https://sandbox.freebuf.com/cloudApi)Token |
| **参数名** | **是否可空** | **传参类型** |                        **说明**                         |
|   title    |    False     |    string    |                 查询语句，支持高级搜索                  |

**一般不写操作可能没啥用**

**说明：此功能需要连接网络，请注意比赛规则进行使用。**

##### 使用示例

```python
from qsnctf import *

zero = ZeroZeon('xxxx') # 主要是配合下面的调用返回的一个对象
print(zero.search('title==零零信安'))
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

#### 自定义Base64

##### base64_encode_custom

|      **函数名**      | **返回类型** |   **位置**   |           **说明**            |
| :------------------: | :----------: | :----------: | :---------------------------: |
| base64_encode_custom |    string    |   base.py    |    base64编码（支持中文）     |
|      **参数名**      | **是否可空** | **传参类型** |           **说明**            |
|         text         |    False     |    string    |        需要编码的内容         |
|     custom_table     |    False     |    string    |            编码表             |
|       encoding       |     True     |    string    | 解码文本时的编码，默认值utf-8 |
|       decoding       |     True     |    string    | 输出文本时的编码，默认值utf-8 |

##### base64_decode_custom

|      **函数名**      | **返回类型** |   **位置**   |           **说明**            |
| :------------------: | :----------: | :----------: | :---------------------------: |
| base64_decode_custom |    string    |   base.py    |          base64解码           |
|      **参数名**      | **是否可空** | **传参类型** |           **说明**            |
|         text         |    False     |    string    |        需要解码的内容         |
|     custom_table     |    False     |    string    |            编码表             |
|       encoding       |     True     |    string    | 解码文本时的编码，默认值utf-8 |
|       decoding       |     True     |    string    | 输出文本时的编码，默认值utf-8 |

##### 使用示例

```python
from qsnctf import *

data = 'SGVsbG8sIFdvcmxkIQ=='
custom_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-'
a = base64_encode_custom(data, custom_table)
print(a)
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

#### 百家姓编码

##### baijiaxing_encode

|    **函数名**     | **返回类型** |   **位置**   |    **说明**    |
| :---------------: | :----------: | :----------: | :------------: |
| baijiaxing_encode |    string    |   misc.py    |   百家姓编码   |
|    **参数名**     | **是否可空** | **传参类型** |    **说明**    |
|    source_text    |    False     |    string    | 需要编码的内容 |

##### baijiaxing_decode

|    **函数名**     | **返回类型** |   **位置**   |    **说明**    |
| :---------------: | :----------: | :----------: | :------------: |
| baijiaxing_decode |    string    |   misc.py    |   百家姓解码   |
|    **参数名**     | **是否可空** | **传参类型** |    **说明**    |
|    source_text    |    False     |    string    | 需要解码的内容 |

##### 使用示例

```python
from qsnctf import *

a = baijiaxing_encode('abcde')
print(a) # 褚卫蒋沈韩
b = baijiaxing_decode('褚卫蒋沈韩')
print(b) # abcde
```

#### Qwerty编码

##### qwerty_encode

|  **函数名**   | **返回类型** |   **位置**   |    **说明**    |
| :-----------: | :----------: | :----------: | :------------: |
| qwerty_encode |    string    |  crypto.py   |   qwerty密码   |
|  **参数名**   | **是否可空** | **传参类型** |    **说明**    |
|  source_text  |    False     |    string    | 需要加密的内容 |

##### 使用示例

```python
from qsnctf import *

a = qwerty_encode('abcd')
print(a) # qwer
```

##### qwerty_decode

|  **函数名**   | **返回类型** |   **位置**   |    **说明**    |
| :-----------: | :----------: | :----------: | :------------: |
| qwerty_decode |    string    |  crypto.py   |   qwerty密码   |
|  **参数名**   | **是否可空** | **传参类型** |    **说明**    |
|  source_text  |    False     |    string    | 需要解密的内容 |

##### 使用示例

```python
from qsnctf import *

a = qwerty_decode('qwer')
print(a) # abcd
```

#### HTML编码

##### html_encode

| **函数名**  | **返回类型** |   **位置**   |    **说明**    |
| :---------: | :----------: | :----------: | :------------: |
| html_encode |    string    |  crypto.py   |    HTML编码    |
| **参数名**  | **是否可空** | **传参类型** |    **说明**    |
|   string    |    False     |    string    | 需要编码的内容 |

##### 使用示例

```python
from qsnctf import *

a = html_encode('<script>')
print(a)
```

##### html_decode

| **函数名**  | **返回类型** |   **位置**   |    **说明**    |
| :---------: | :----------: | :----------: | :------------: |
| html_decode |    string    |  crypto.py   |    HTML编码    |
| **参数名**  | **是否可空** | **传参类型** |    **说明**    |
|   string    |    False     |    string    | 需要解码的内容 |

##### 使用示例

```python
from qsnctf import *

b = html_decode('&lt;script&gt;')
print(b)
```

#### JSfuck

##### jsfuck_encode

|  **函数名**   | **返回类型** |   **位置**   |    **说明**    |
| :-----------: | :----------: | :----------: | :------------: |
| jsfuck_encode |    string    |  crypto.py   |     JSFUCK     |
|  **参数名**   | **是否可空** | **传参类型** |    **说明**    |
|    string     |    False     |    string    | 需要编码的内容 |

##### 使用示例

```python
from qsnctf import *

b = jsfuck_encode('abcdefg')
print(b) # [][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]][([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]]((![]+[])[+!+[]]+([][(!![]+[])[!+[]+!+[]+!+[]]+([][[]]+[])[+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]]()+[])[!+[]+!+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]]+[])[!+[]+!+[]+!+[]]+([][[]]+[])[!+[]+!+[]]+(!![]+[])[!+[]+!+[]+!+[]]+(![]+[])[+[]]+(![]+[+[]]+([]+[])[([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]])[+!+[]+[+[]]]+([][[]]+[])[+!+[]]+(![]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([][[]]+[])[+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]]+[])[!+[]+!+[]+!+[]]+(!![]+[])[+[]]+(!![]+[][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]])[+!+[]+[+[]]]+(!![]+[])[+!+[]]])[!+[]+!+[]+[+[]]])
```

##### jsfuck_decode

|  **函数名**   | **返回类型** |   **位置**   |    **说明**    |
| :-----------: | :----------: | :----------: | :------------: |
| jsfuck_decode |    string    |  crypto.py   |     JSFUCK     |
|  **参数名**   | **是否可空** | **传参类型** |    **说明**    |
|    string     |    False     |    string    | 需要解码的内容 |

##### 使用示例

```python
from qsnctf import *

a = jsfuck_decode('(![]+[])[+!+[]]+([][(!![]+[])[!+[]+!+[]+!+[]]+([][[]]+[])[+!+[]]+(!![]+[])[+[]]+(!![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(!![]+[])[!+[]+!+[]+!+[]]+(![]+[])[!+[]+!+[]+!+[]]]()+[])[!+[]+!+[]]+([][(![]+[])[+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]]+(![]+[])[!+[]+!+[]]]+[])[!+[]+!+[]+!+[]]')
print(a)
```

#### AAencode

##### aaencode

| **函数名** | **返回类型** |   **位置**   |    **说明**    |
| :--------: | :----------: | :----------: | :------------: |
|  aaencode  |    string    |  crypto.py   |     JSFUCK     |
| **参数名** | **是否可空** | **传参类型** |    **说明**    |
|   string   |    False     |    string    | 需要编码的内容 |

##### 使用示例

```python
from qsnctf import *

a = aaencode('qsnctf')
print(a)
```

##### aadecode

| **函数名** | **返回类型** |   **位置**   |    **说明**    |
| :--------: | :----------: | :----------: | :------------: |
|  aadecode  |    string    |  crypto.py   |     JSFUCK     |
| **参数名** | **是否可空** | **传参类型** |    **说明**    |
|   string   |    False     |    string    | 需要解码的内容 |

##### 使用示例

```python
from qsnctf import *

b = aadecode(r"ﾟωﾟﾉ= /｀ｍ´）ﾉ ~┻━┻   //*´∇｀*/ ['_']; o=(ﾟｰﾟ)  =_=3; c=(ﾟΘﾟ) =(ﾟｰﾟ)-(ﾟｰﾟ); (ﾟДﾟ) =(ﾟΘﾟ)= (o^_^o)/ (o^_^o);(ﾟДﾟ)={ﾟΘﾟ: '_' ,ﾟωﾟﾉ : ((ﾟωﾟﾉ==3) +'_') [ﾟΘﾟ] ,ﾟｰﾟﾉ :(ﾟωﾟﾉ+ '_')[o^_^o -(ﾟΘﾟ)] ,ﾟДﾟﾉ:((ﾟｰﾟ==3) +'_')[ﾟｰﾟ] }; (ﾟДﾟ) [ﾟΘﾟ] =((ﾟωﾟﾉ==3) +'_') [c^_^o];(ﾟДﾟ) ['c'] = ((ﾟДﾟ)+'_') [ (ﾟｰﾟ)+(ﾟｰﾟ)-(ﾟΘﾟ) ];(ﾟДﾟ) ['o'] = ((ﾟДﾟ)+'_') [ﾟΘﾟ];(ﾟoﾟ)=(ﾟДﾟ) ['c']+(ﾟДﾟ) ['o']+(ﾟωﾟﾉ +'_')[ﾟΘﾟ]+ ((ﾟωﾟﾉ==3) +'_') [ﾟｰﾟ] + ((ﾟДﾟ) +'_') [(ﾟｰﾟ)+(ﾟｰﾟ)]+ ((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+((ﾟｰﾟ==3) +'_') [(ﾟｰﾟ) - (ﾟΘﾟ)]+(ﾟДﾟ) ['c']+((ﾟДﾟ)+'_') [(ﾟｰﾟ)+(ﾟｰﾟ)]+ (ﾟДﾟ) ['o']+((ﾟｰﾟ==3) +'_') [ﾟΘﾟ];(ﾟДﾟ) ['_'] =(o^_^o) [ﾟoﾟ] [ﾟoﾟ];(ﾟεﾟ)=((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+ (ﾟДﾟ) .ﾟДﾟﾉ+((ﾟДﾟ)+'_') [(ﾟｰﾟ) + (ﾟｰﾟ)]+((ﾟｰﾟ==3) +'_') [o^_^o -ﾟΘﾟ]+((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+ (ﾟωﾟﾉ +'_') [ﾟΘﾟ]; (ﾟｰﾟ)+=(ﾟΘﾟ); (ﾟДﾟ)[ﾟεﾟ]='\\'; (ﾟДﾟ).ﾟΘﾟﾉ=(ﾟДﾟ+ ﾟｰﾟ)[o^_^o -(ﾟΘﾟ)];(oﾟｰﾟo)=(ﾟωﾟﾉ +'_')[c^_^o];(ﾟДﾟ) [ﾟoﾟ]='\"';(ﾟДﾟ) ['_'] ( (ﾟДﾟ) ['_'] (ﾟεﾟ+(ﾟДﾟ)[ﾟoﾟ]+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (o^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (o^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟoﾟ]) (ﾟΘﾟ)) ('_');")
print(b)
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

##### get_uuid

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

#### 字符串转换

##### string_split

|  **函数名**  | **返回类型** |   **位置**   |       **说明**       |
| :----------: | :----------: | :----------: | :------------------: |
| string_split |     list     |   misc.py    |   根据内容自动分割   |
|  **参数名**  | **是否可空** | **传参类型** |       **说明**       |
|      s       |    False     |    string    | 需要分割成列表的文本 |

##### 使用示例

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

**说明：可以根据不同的内容判断进行截取，最终结果是一致的**

##### ord_to_str

| **函数名** | **返回类型** |   **位置**   |    **说明**     |
| :--------: | :----------: | :----------: | :-------------: |
| ord_to_str |    string    |   misc.py    |   ord值转str    |
| **参数名** | **是否可空** | **传参类型** |    **说明**     |
|    ord     |    False     |     int      | 需要转换的ord值 |

##### 使用示例

```python
from qsnctf import *


print(ord_to_str(97)) #a
```

##### ord_list_to_str_list

|      **函数名**      | **返回类型** |   **位置**   |        **说明**        |
| :------------------: | :----------: | :----------: | :--------------------: |
| ord_list_to_str_list |     list     |   misc.py    | ord值转str（列表支持） |
|      **参数名**      | **是否可空** | **传参类型** |        **说明**        |
|       ord_list       |    False     |     list     |   需要转换的ord列表    |

##### 使用示例

```python
from qsnctf import *


a = ord_list_to_str_list(['97', '98', '99'])
print(a)  # ['a', 'b', 'c']
```

##### ord_str_to_str

|   **函数名**   | **返回类型** |   **位置**   |            **说明**             |
| :------------: | :----------: | :----------: | :-----------------------------: |
| ord_str_to_str |    string    |   misc.py    |    ord值转str（字符串支持）     |
|   **参数名**   | **是否可空** | **传参类型** |            **说明**             |
|    ord_str     |    False     |     list     | ord字符串，可以用逗号和空格分开 |

##### 使用示例

```python
from qsnctf import *


a = ord_str_to_str('97,98,99')
print(a)  # abc
```

##### chr_to_ord

| **函数名** | **返回类型** |   **位置**   |       **说明**       |
| :--------: | :----------: | :----------: | :------------------: |
| chr_to_ord |    string    |   misc.py    |     char转ord值      |
| **参数名** | **是否可空** | **传参类型** |       **说明**       |
|    char    |    False     |     int      | 需要转换的char(字符) |

##### 使用示例

```python
from qsnctf import *


print(chr_to_ord('a')) #97
```

##### chr_list_to_ord_list

|      **函数名**      | **返回类型** |   **位置**   |     **说明**      |
| :------------------: | :----------: | :----------: | :---------------: |
| chr_list_to_ord_list |     list     |   misc.py    | chr列表转ord列表  |
|      **参数名**      | **是否可空** | **传参类型** |     **说明**      |
|       chr_list       |    False     |     list     | 需要转换的chr列表 |

##### 使用示例

```python
from qsnctf import *


a = chr_list_to_ord_list(['a', 'b', 'c'])
print(a)  # [97, 98, 99]
```

##### chr_str_to_ord_str

|     **函数名**     | **返回类型** |   **位置**   |                  **说明**                   |
| :----------------: | :----------: | :----------: | :-----------------------------------------: |
| chr_str_to_ord_str |    string    |   misc.py    |               chr转ord字符串                |
|     **参数名**     | **是否可空** | **传参类型** |                  **说明**                   |
|      chr_str       |    False     |     list     | chr字符串，可以用逗号、空格分开，也可以不分 |

##### 使用示例

```python
from qsnctf import *


a = ord_str_to_str('abc')
print(a)  # 97,98,99
```

##### search_flag

| **函数名**  | **返回类型** |   **位置**   |            **说明**             |
| :---------: | :----------: | :----------: | :-----------------------------: |
| search_flag |    string    |   misc.py    |        通过正则查找flag         |
| **参数名**  | **是否可空** | **传参类型** |            **说明**             |
|    text     |    False     |    string    |       疑似包含flag的内容        |
| flag_prefix |     True     |    string    | Flag前缀，格式flag\|qsnctf\|ctf |

##### 使用示例

```python
from qsnctf import *


a = search_flag('hello, i will give you flag flag{qsnctf-12345}')
print(a) # flag{qsnctf-12345}
```

#### 压缩包操作

##### class-ZipPasswordCracking

|     **函数名**      | **返回类型** |   **位置**   |            **说明**            |
| :-----------------: | :----------: | :----------: | :----------------------------: |
| ZipPasswordCracking |    string    |   misc.py    |       ZIP压缩包密码爆破        |
|     **参数名**      | **是否可空** | **传参类型** |            **说明**            |
|      filename       |    False     |    string    |         zip的文件位置          |
|     threadline      |     True     |     int      |             线程数             |
|     sleep_time      |     True     |     int      | 等待时间（非网络操作一般不用） |
|      pass_list      |     True     |     list     |         自定义密码列表         |
|        path         |     True     |    string    |          解压缩的目录          |

**说明：这里支持伪加密压缩包了哦！**

##### 使用示例

```python
from qsnctf import *

zip = ZipPasswordCracking("pass.zip", auto_run=True)

print(zip.results)

plist = ['1234','test','123123']
zip = ZipPasswordCracking("pass.zip", threadline=100, pass_list=plist, path="file", auto_run=True)

print(zip.results) # 123123
```

##### zip_unzip

| **函数名** | **返回类型** |   **位置**   |              **说明**              |
| :--------: | :----------: | :----------: | :--------------------------------: |
| zip_unzip  |   Boolean    |   misc.py    |             ZIP解压缩              |
| **参数名** | **是否可空** | **传参类型** |              **说明**              |
|  filename  |    False     |    string    |           zip的文件位置            |
|  password  |     True     |    string    | 这里是string类型，如果没有密码留空 |
|  members   |     True     |     list     |           需要解压的文件           |
|    path    |     True     |    string    |            解压缩的目录            |

##### 使用示例

```python
from qsnctf import *

zip_unzip("pass.zip")
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

#### 八卦密码

##### eight_diagrams_encrypt

|       **函数名**       | **返回类型** |   **位置**   |    **说明**    |
| :--------------------: | :----------: | :----------: | :------------: |
| eight_diagrams_encrypt |    string    |  crypto.py   |  八卦密码加密  |
|       **参数名**       | **是否可空** | **传参类型** |    **说明**    |
|          text          |    False     |    string    | 需要加密的内容 |

##### eight_diagrams_decrypt

|       **函数名**       | **返回类型** |   **位置**   |    **说明**    |
| :--------------------: | :----------: | :----------: | :------------: |
| eight_diagrams_decrypt |    string    |  crypto.py   |  八卦密码解密  |
|       **参数名**       | **是否可空** | **传参类型** |    **说明**    |
|          text          |    False     |    string    | 需要解密的内容 |

##### 使用示例

```python
from qsnctf import *

a = eight_diagrams_encrypt('qsnctf')
print(a)  # 正巽震~正巽兑~正离巽~正艮兑~正巽艮~正艮巽~
a = eight_diagrams_decrypt('正巽震~正巽兑~正离巽~正艮兑~正巽艮~正艮巽~')
print(a)  # qsnctf
```

#### 埃特巴什码

##### atbash_cipher

|  **函数名**   | **返回类型** |   **位置**   |       **说明**       |
| :-----------: | :----------: | :----------: | :------------------: |
| atbash_cipher |    string    |  crypto.py   |      埃特巴什码      |
|  **参数名**   | **是否可空** | **传参类型** |       **说明**       |
|     text      |    False     |    string    | 需要加密或解密的内容 |

##### 使用示例

```python
from qsnctf import *


a = atbash_cipher('qsnctf.com')
print(a) # jhmxgu.xln
a = atbash_cipher('jhmxgu.xln')
print(a) # qsnctf.com

```

#### 摩斯密码加密

##### morse_encrypt

|  **函数名**   | **返回类型** |   **位置**   |             **说明**              |
| :-----------: | :----------: | :----------: | :-------------------------------: |
| morse_encrypt |    string    |  crypto.py   |           摩斯密码加密            |
|  **参数名**   | **是否可空** | **传参类型** |             **说明**              |
|    message    |    False     |    string    |          需要加密的内容           |
|     split     |     True     |    string    | 分隔符（默认为空格）可以设置为"/" |
|     point     |     True     |    string    |     点 用做替换摩斯密码的“.”      |
|      bar      |     True     |    string    |     横 用作替换摩斯密码的“-”      |

##### 使用示例

```python
from qsnctf import *

a = morse_encrypt('QSNCTF','/')
print(a) # --.-/.../-./-.-./-/..-.
```

#### 摩斯密码解密

##### morse_decrypt

|  **函数名**   | **返回类型** |   **位置**   |             **说明**              |
| :-----------: | :----------: | :----------: | :-------------------------------: |
| morse_decrypt |    string    |  crypto.py   |           摩斯密码解密            |
|  **参数名**   | **是否可空** | **传参类型** |             **说明**              |
|    cipher     |    False     |    string    |          需要解密的内容           |
|     split     |     True     |    string    | 分隔符（默认为空格）可以设置为"/" |
|     point     |     True     |    string    |     点 用做替换摩斯密码的“.”      |
|      bar      |     True     |    string    |     横 用作替换摩斯密码的“-”      |

##### 使用示例

```python
from qsnctf import *

b = morse_decrypt('..-./---/.-/.-.-/./--.-','/', '-', '.')
print(b) # QSNCTF
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

 
