from qsnctf import *


scan = ['https://www.baidu.com/', 'https://www.qsnctf.com/admin']
url = UrlScan(scan,echo=True)
print(url.results_code)