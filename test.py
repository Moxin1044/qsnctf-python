from qsnctf import *

list = ["https://bbs.qsnctf.com/admin.php", "https://bbs.qsnctf.com/robots.txt", "https://www.qsnctf.com/"]
dir = UrlScan(list, 10, 0.5)
print(dir.results_code)
# 下面的结果中只会存在返回的请求
print(dir.results)

UrlScan(list, 100, 0.1, echo=True) # 将会直接进行扫描并打印结果（这样在显示上更快，但是效率同上）
