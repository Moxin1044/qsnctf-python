# web操作
import requests
import os
from qsnctf.auxiliary import read_file_to_list,is_http_or_https_url,normalize_url


class DirScan:
    def __init__(self, url, threadline=10, dirlist=None):
        """
        :param url: Sans URL
        :param threadline: Thread line
        :param dirlist: dirs list
        """
        self.url = url
        self.threadline = threadline
        self.results = []
        self.dirlist = dirlist

    def scan(self):
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