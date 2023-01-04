# web操作
import os
import re
import time
import queue
import threading
import requests
from bs4 import BeautifulSoup
from qsnctf.auxiliary import read_file_to_list, is_http_or_https_url, normalize_url


class DirScan:
    def __init__(self, url, threadline=10, sleep_time=0, dirlist=None, return_code=None, echo=False, wait=True):
        """
        :param url: Sans URL
        :param threadline: Thread line
        :param sleep_time: sleep time
        :param dirlist: dirs list
        :param return_code: return code
        :param echo: print scan result
        :param wait: Whether to wait for the process to end
        """
        self.q = None
        self.print_list = echo
        self.wait = wait
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
            browser = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
                "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
                "Referer": f"{self.url}{path}",
                "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
                "Te": "trailers", "Connection": "close"}
            response = requests.get(self.url + path, headers=browser, verify=False)
            time.sleep(self.sleep_time)
            # 将符合条件的扫描结果添加到results列表
            if response.status_code in self.return_code:
                self.results.append(f"{self.url}{path}")
                self.results_code.append(f"{self.url}{path} {response.status_code}")
                if self.print_list:
                    print(f"{self.url}{path} {response.status_code}")  # print response
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
        if self.wait:
            self.q.join()  # Wait for thread to finish
        # 如果不等待，也可以直接获取对象中的results、results_code属性


class UrlScan:
    # 网页存活扫描
    def __init__(self, url_list, threadline=10, sleep_time=0, return_code=None, echo=False, wait=True):
        """
        :param url_list: Sans URL
        :param threadline: Thread line
        :param sleep_time: sleep time
        :param return_code: return code
        :param echo: print scan result
        :param wait: Whether to wait for the process to end
        """
        self.q = None
        self.print_list = echo
        self.wait = wait
        self.url_list = url_list
        self.threadline = threadline
        self.sleep_time = sleep_time
        self.results = []
        self.results_code = []
        self.results_title = []
        if return_code is not None:
            self.return_code = return_code
        else:
            self.return_code = [200, 301, 302, 401, 403, 404, 500]  # 这里默认404是需要返回的，为了验证URL的状态
        self.run()

    def scan_url(self):
        while not self.q.empty():
            # 从队列中取出一个路径
            url = self.q.get()
            requests.packages.urllib3.disable_warnings()
            browser = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
                "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
                "Referer": f"{url}",
                "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
                "Te": "trailers", "Connection": "close"}
            response = requests.get(url, headers=browser, verify=False)
            time.sleep(self.sleep_time)
            # 将符合条件的扫描结果添加到results列表
            if response.status_code in self.return_code:
                self.results.append(f"{url}")
                self.results_code.append(f"{url} {response.status_code}")
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    title = soup.find("title")
                    title = re.search(r"<title>(.+?)</title>", str(title))
                    if title:
                        title = title.group(1)
                    else:
                        title = "No Title"
                    self.results_title.append(f"{url} {title}")
                if self.print_list and response.status_code == 200:
                    print(f"{url} {response.status_code} {title}")  # print response
                elif self.print_list and response.status_code != 200:
                    print(f"{url} {response.status_code}")
            # 完成之后将任务标记为完成
            self.q.task_done()

    def run(self):
        self.q = queue.Queue()  # Create Queue
        for path in self.url_list:
            self.q.put(path)
        for i in range(self.threadline):
            thread = threading.Thread(target=self.scan_url)
            thread.start()
        if self.wait:
            self.q.join()  # Wait for thread to finish
        # 如果不等待，也可以直接获取对象中的results、results_code属性


def get_url_title(url):
    browser = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"{url}",
        "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "Te": "trailers", "Connection": "close"}
    response = requests.get(url, headers=browser, verify=False)
