# web操作
import requests
import os
import threading
import queue
from qsnctf.auxiliary import read_file_to_list, is_http_or_https_url, normalize_url


class DirScan:
    def __init__(self, url, threadline=100, dirlist=None, return_code=None):
        """
        :param url: Sans URL
        :param threadline: Thread line
        :param dirlist: dirs list
        :param return_code: return status_code
        """
        self.q = None
        self.url = url
        self.threadline = threadline
        self.results = []
        self.check_url = ""
        self.dirlist = dirlist
        if return_code is not None:
            self.return_code = return_code
        else:
            self.return_code = [200, 301, 302, 401, 403, 500]  # 默认不返回404，其余需返回，主要为渗透使用。
        self.run()

    def scan_dir_list(self):
        if self.dirlist:
            pass
        else:
            package_path = os.path.abspath(os.path.dirname(__file__))
            file_path = os.path.join(package_path, 'plugin', 'txt', 'dirs.txt')
            self.dirlist = read_file_to_list(file_path)
        if is_http_or_https_url(self.url):
            pass
        else:
            raise ValueError("Invalid url")

    def scan_dir(self):
        while not self.q.empty():
            # 从队列中取出一个路径
            path = self.q.get()
            response = requests.get(self.url + path)
            # 将符合条件的扫描结果添加到results列表
            if response.status_code in self.return_code:
                self.results.append(f"{self.url}{path} {response.status_code}")
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
