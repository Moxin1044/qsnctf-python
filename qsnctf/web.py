# web操作
import os
import time
import queue
import threading
import requests
from qsnctf.auxiliary import read_file_to_list, is_http_or_https_url, normalize_url


# 模块内公有函数
def url_get(url):
    headers = {}
    return requests.get(url, header=headers)

class DirScan:
    def __init__(self, url, threadline=100, sleep_time=0, dirlist=None, return_code=None):
        """
        :param url: Sans URL
        :param threadline: Thread line
        :param sleep_time: sleep time
        :param dirlist: dirs list
        :param return_code: return code
        """
        self.q = None
        self.url = url
        self.threadline = threadline
        self.sleep_time = sleep_time
        self.results = []
        self.results_code = []
        self.check_url = ""
        self.dirlist = dirlist
        if return_code is not None:
            self.return_code = return_code
        else:
            self.return_code = [200, 301, 302, 401, 403, 500]  # 默认不返回404，其余需返回，主要为渗透使用。
        self.run()

    def scan_dir_list(self):
        if self.dirlist:
            pass  # 如果使用自定义的dirlist,这里不用读取
        else:
            package_path = os.path.abspath(os.path.dirname(__file__))
            file_path = os.path.join(package_path, 'plugin', 'txt', 'dirs.txt')
            self.dirlist = read_file_to_list(file_path)
        if is_http_or_https_url(self.url):
            self.url = normalize_url(self.url)
        else:
            raise ValueError("Invalid url")

    def scan_dir(self):
        while not self.q.empty():
            # 从队列中取出一个路径
            path = self.q.get()
            requests.packages.urllib3.disable_warnings()
            response = requests.get(self.url + path, verify=False)
            time.sleep(self.sleep_time)
            # 将符合条件的扫描结果添加到results列表
            if response.status_code in self.return_code:
                self.results.append(f"{self.url}{path}")
                self.results_code.append(f"{self.url}{path} {response.status_code}")
            # 完成之后将任务标记为完成
            self.q.task_done()

    def run(self):
        self.scan_dir_list()
        self.q = queue.Queue()  # Create Queue
        for path in self.dirlist:
            self.q.put(path)
        for i in range(self.threadline):
            thread = threading.Thread(target=self.scan_dir)
            thread.start()
        self.q.join()  # Wait for thread to finish
