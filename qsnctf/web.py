# web操作
import os
import re
import time
import queue
import threading
import dns.resolver
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup,Comment
from qsnctf.auxiliary import read_file_to_list, is_http_or_https_url, normalize_url


def get_url_title(url, cookies=''):
    """
    :param cookies: cookies
    :param url: get url
    :return:  url title
    """
    browser = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"{url}", "Cookie": f"{cookies}",
        "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "Te": "trailers", "Connection": "close"}
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, headers=browser, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("title")
        title = re.search(r"<title>(.+?)</title>", str(title))
        if title:
            title = title.group(1)
        else:
            title = "No Title"
    else:
        title = "Request unreachable"
    return title


def get_url_description(url, cookies=''):
    """
    :param cookies: cookie
    :param url: get url
    :return:  url description
    """
    browser = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"{url}", "Cookie": f"{cookies}",
        "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "Te": "trailers", "Connection": "close"}
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, headers=browser, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        description_tag = soup.find('meta', attrs={'name': 'description'})
        if description_tag:
            description = description_tag['content']
        else:
            description = 'No description'
    else:
        description = "Request unreachable"
    return description


def get_url_keywords(url, cookies=''):
    """
    :param cookies: cookie
    :param url: get url
    :return:  url keywords
    """
    browser = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"{url}", "Cookie": f"{cookies}",
        "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "Te": "trailers", "Connection": "close"}
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, headers=browser, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        keywords_tag = soup.find('meta', attrs={'name': 'keywords'})
        if keywords_tag:
            keywords = keywords_tag['content']
        else:
            keywords = 'No keywords'
    else:
        keywords = "Request unreachable"
    return keywords


def get_url_ICP(url, cookies=""):
    """
    :param cookies: cookie
    :param url: get url
    :return:  url ICP
    """
    browser = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"{url}", "Cookie": f"{cookies}",
        "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "Te": "trailers", "Connection": "close"}
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, headers=browser, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        icp_tag = soup.find('a', attrs={'href': 'https://beian.miit.gov.cn'})
        if icp_tag:
            icp = icp_tag.text
        else:
            icp = 'No ICP'
    else:
        icp = "Request unreachable"
    return icp.lstrip()


def get_url_a_href(url, cookies=""):
    """
    :param cookies: cookie
    :param url: get url
    :return:  url a_href list
    """
    browser = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"{url}", "Cookie": f"{cookies}",
        "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "Te": "trailers", "Connection": "close"}
    requests.packages.urllib3.disable_warnings()
    r_list = []
    response = requests.get(url, headers=browser, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        a_tags = soup.find_all('a')
        if a_tags:
            for a_tag in a_tags:
                # 取出 a 标签的 href 属性值
                href = a_tag.get('href')
                r_list.append(href)
            href = r_list
        else:
            href = 'No href'
    else:
        href = "Request unreachable"
    return href


def get_url_img(url, cookies=""):
    """
    :param cookies: cookie
    :param url: get url
    :return:  url img list
    """
    browser = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"{url}", "Cookie": f"{cookies}",
        "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "Te": "trailers", "Connection": "close"}
    requests.packages.urllib3.disable_warnings()
    r_list = []
    response = requests.get(url, headers=browser, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        a_tags = soup.find_all('img')
        if a_tags:
            for a_tag in a_tags:
                # 取出 a 标签的 href 属性值
                src = a_tag.get('src')
                r_list.append(src)
            src = r_list
        else:
            src = 'No src'
    else:
        src = "Request unreachable"
    return src


def get_url_comment(url, cookies=""):
    """
    :param cookies: cookie
    :param url: get url
    :return:  url comment
    """
    browser = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"{url}", "Cookie": f"{cookies}",
        "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "Te": "trailers", "Connection": "close"}
    requests.packages.urllib3.disable_warnings()
    r_list = []
    response = requests.get(url, headers=browser, verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # 查找所有的注释节点
        comments = soup.find_all(string=lambda s: isinstance(s, Comment))
        # 遍历注释节点
        if comments:
            for comment in comments:
                # 取出注释的内容
                r_list.append(comment)
            src = r_list
        else:
            src = 'No comment'
    else:
        src = "Request unreachable"
    return src


def get_url_time(url):
    """
    :param url: url
    :return: requests seconds
    """
    start_time = time.time()
    browser = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"{url}",
        "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "Te": "trailers", "Connection": "close"}
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, headers=browser, verify=False)
    end_time = time.time()
    speed = end_time - start_time
    return speed


def get_url_ico(url):
    """
    :param url: url
    :return: url ico address
    """
    start_time = time.time()
    browser = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"{url}",
        "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "Te": "trailers", "Connection": "close"}
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, headers=browser, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    link_tags = soup.find_all('link', rel='shortcut icon')
    # 遍历 link 标签
    if link_tags:
        for link_tag in link_tags:
            # 取出 ICO 图标的 URL
            ico_url = link_tag.get('href')
            if ico_url:
                return ico_url
    else:
        return False


def get_webshell_post(url, key):
    """
    :param url: url
    :param key: key
    :return: requests seconds
    """
    browser = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"{url}",
        "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "Te": "trailers", "Connection": "close"}
    requests.packages.urllib3.disable_warnings()
    shell = "print('test_a_shell');"
    post_data = f"{key}={shell}"
    response = requests.post(url, headers=browser, data=post_data, verify=False)
    if "test_a_shell" in response.text:
        return True
    return False


def get_webshell_get(url, key):
    """
    :param url: url
    :param key: key
    :return: requests seconds
    """
    browser = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"{url}",
        "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "Te": "trailers", "Connection": "close"}
    requests.packages.urllib3.disable_warnings()
    shell = "print('test_a_shell');"
    params = f"{key}={shell}"
    response = requests.get(url, headers=browser, params=params, verify=False)
    if "test_a_shell" in response.text:
        return True
    return False


def get_exec_webshell_get(url, key, shell):
    """
    :param url: url
    :param key: key
    :param shell: shell
    :return: requests seconds
    """
    browser = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"{url}",
        "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "Te": "trailers", "Connection": "close"}
    requests.packages.urllib3.disable_warnings()
    sh = f"$output = array();exec('{shell}', $output);print(implode('\n', $output));"
    params = f"{key}={sh}"
    response = requests.get(url, headers=browser, params=params, verify=False)
    return response.text


def get_exec_webshell_post(url, key, shell):
    """
    :param url: url
    :param key: key
    :param shell: shell
    :return: requests seconds
    """
    browser = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"{url}",
        "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "Te": "trailers", "Connection": "close"}
    requests.packages.urllib3.disable_warnings()
    sh = f"$output = array();exec('{shell}', $output);print(implode('\n', $output));"
    data = f"{key}={sh}"
    response = requests.post(url, headers=browser, data=data, verify=False)
    return response.text


def get_eval_webshell_get(url, key, shell):
    """
    :param url: url
    :param key: key
    :param shell: shell
    :return: requests seconds
    """
    browser = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"{url}",
        "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "Te": "trailers", "Connection": "close"}
    requests.packages.urllib3.disable_warnings()
    sh = f"{shell}"
    params = f"{key}={sh}"
    response = requests.get(url, headers=browser, params=params, verify=False)
    return response.text


def get_eval_webshell_post(url, key, shell):
    """
    :param url: url
    :param key: key
    :param shell: shell
    :return: requests seconds
    """
    browser = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"{url}",
        "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
        "Te": "trailers", "Connection": "close"}
    requests.packages.urllib3.disable_warnings()
    sh = f"{shell}"
    data = f"{key}={sh}"
    response = requests.post(url, headers=browser, data=data, verify=False)
    return response.text


class DirScan:
    def __init__(self, url, threadline=10, sleep_time=0, dirlist=None, return_code=None, echo=False, wait=True, cookies=''):
        """
        :param url: Sans URL
        :param threadline: Thread line
        :param sleep_time: sleep time
        :param dirlist: dirs list
        :param return_code: return code
        :param echo: print scan result
        :param wait: Whether to wait for the process to end
        :param cookies: cookie
        """
        self.cookies = cookies
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
                "Referer": f"{self.url}{path}", "Cookie": f"{self.cookies}",
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
    def __init__(self, url_list, threadline=10, sleep_time=0, return_code=None, echo=False, wait=True, cookies=''):
        """
        :param url_list: Sans URL
        :param threadline: Thread line
        :param sleep_time: sleep time
        :param return_code: return code
        :param echo: print scan result
        :param wait: Whether to wait for the process to end
        :param cookies: cookie
        """
        self.cookies = cookies
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
                "Referer": f"{url}", "Cookie": f"{self.cookies}",
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


class DomainScan:
    def __init__(self, domain, threadline=10, sleep_time=0, domainlist=None, return_code=None, echo=False, wait=True):
        """
        :param domain: Sans domain
        :param threadline: Thread line
        :param sleep_time: sleep time
        :param dirlist: dirs list
        :param return_code: return code
        :param echo: print scan result
        :param wait: Whether to wait for the process to end
        """
        self.results_title = []
        self.q = None
        self.print_list = echo
        self.wait = wait
        self.domain = domain
        self.threadline = threadline
        self.sleep_time = sleep_time
        self.results = []
        self.results_code = []
        self.check_url = ""
        self.domainlist = domainlist
        if return_code is not None:
            self.return_code = return_code
        else:
            self.return_code = [200, 301, 302, 401, 403, 500]  # 默认不返回404，其余需返回，主要为渗透使用。
        self.run()

    def scan_domain_list(self):
        if self.domainlist:
            pass  # 如果使用自定义的dirlist,这里不用读取
        else:
            package_path = os.path.abspath(os.path.dirname(__file__))
            file_path = os.path.join(package_path, 'plugin', 'txt', 'domain.txt')
            self.domainlist = read_file_to_list(file_path)

    def scan_domain(self):
        while not self.q.empty():
            # 从队列中取出一个路径
            domain = self.q.get()
            requests.packages.urllib3.disable_warnings()
            browser = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
                "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
                "Referer": f"http://{domain}.{self.domain}/",
                "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
                "Te": "trailers", "Connection": "close"}
            response = requests.get(f"http://{domain}.{self.domain}/", headers=browser, verify=False)
            time.sleep(self.sleep_time)
            # 将符合条件的扫描结果添加到results列表
            if response.status_code in self.return_code:
                self.results.append(f"http://{domain}.{self.domain}/")
                self.results_code.append(f"http://{domain}.{self.domain}/")
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    title = soup.find("title")
                    title = re.search(r"<title>(.+?)</title>", str(title))
                    if title:
                        title = title.group(1)
                    else:
                        title = "No Title"
                    self.results_title.append(f"http://{domain}.{self.domain}/ {title}")
                if self.print_list and response.status_code == 200:
                    print(f"http://{domain}.{self.domain}/ {response.status_code} {title}")  # print response
                elif self.print_list and response.status_code != 200:
                    print(f"http://{domain}.{self.domain}/ {response.status_code}")
                # 完成之后将任务标记为完成
            self.q.task_done()

    def run(self):
        self.scan_domain_list()
        self.q = queue.Queue()  # Create Queue
        for path in self.domainlist:
            self.q.put(path)
        for i in range(self.threadline):
            thread = threading.Thread(target=self.scan_domain)
            thread.start()
        if self.wait:
            self.q.join()  # Wait for thread to finish
        # 如果不等待，也可以直接获取对象中的results、results_code属性


class WebShellCracking:
    def __init__(self, url, threadline=10, sleep_time=0, passlist=None, mode="POST"):
        """
        :param url: Shell URL
        :param threadline: thread line
        :param sleep_time: sleep_time in seconds
        :param passlist:  list of passwords
        :param mode: GET or POST
        """
        self.results_title = []
        self.mode = mode
        self.q = None
        self.url = url
        self.threadline = threadline
        self.sleep_time = sleep_time
        self.results = ''
        self.passlist = passlist
        self.return_code = [200, 301, 302, 401, 403, 500]  # 默认不返回404，其余需返回，主要为渗透使用。
        self.run()

    def scan_pass_list(self):
        if self.passlist:
            pass  # 如果使用自定义的dirlist,这里不用读取
        else:
            package_path = os.path.abspath(os.path.dirname(__file__))
            file_path = os.path.join(package_path, 'plugin', 'txt', 'shell_weak_password.txt')
            self.passlist = read_file_to_list(file_path)

    def Cracking_webshell_POST(self):
        while not self.q.empty():
            # 从队列中取出密码
            key = self.q.get()
            if get_webshell_post(self.url, key):
                self.results = key
            self.q.task_done()

    def Cracking_webshell_GET(self):
        while not self.q.empty():
            # 从队列中取出密码
            key = self.q.get()
            if get_webshell_get(self.url, key):
                self.results = key
            self.q.task_done()

    def run(self):
        self.scan_pass_list()
        self.q = queue.Queue()  # Create Queue
        for password in self.passlist:
            self.q.put(password)
        for i in range(self.threadline):
            if self.mode == "GET":
                thread = threading.Thread(target=self.Cracking_webshell_GET)
                thread.start()
            else:
                thread = threading.Thread(target=self.Cracking_webshell_POST)
                thread.start()
        self.q.join()  # Wait for thread to finish
        # 如果不等待，也可以直接获取对象中的results、results_code属性


