# web操作
import requests


class dirscan:
    def __init__(self, url, threadline=10, dirlist=None):
        self.url = url
        self.threadline = threadline
        if dirlist:
            print("true")
        else:
            print("false")