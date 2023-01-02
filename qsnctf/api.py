import requests
# 这里的操作一般都是需要联网的，如果是线下赛请确认主办方允许联网使用


class quipqiup:
    def __init__(self, ciphertext, clues=''):
        self.json = None
        self.text = None
        self.list = None
        # 上是三个返回值，用于取回不同的数据类型，均在quipqiup_return中定义
        self.ciphertext = ciphertext
        self.clues = clues
        self.url = 'https://www.quipqiup.com:443/'
        self.id = self.quipqiup_get_id()
        self.quipqiup_return()

    def quipqiup_get_id(self):
        url = f"{self.url}solve"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
                   "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                   "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
                   "Origin": "https://www.quipqiup.com", "Referer": "https://www.quipqiup.com/",
                   "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
                   "Te": "trailers", "Connection": "close"}
        json = {"ciphertext": self.ciphertext, "clues": self.clues, "mode": "auto", "was_auto": True, "was_clue": False}
        response = requests.post(url, headers=headers, json=json).json()
        return response['id']

    def quipqiup_return(self):
        url = f"{self.url}status"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
                   "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                   "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
                   "Origin": "https://www.quipqiup.com", "Referer": "https://www.quipqiup.com/",
                   "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
                   "Te": "trailers", "Connection": "close"}
        json = {"id": int(self.id)}
        response = requests.post(url, headers=headers, json=json)
        response_data = response.json()
        self.json = response_data  # json 直接返回requests的response json
        r_list = response_data['solutions']
        return_list = []
        for response_list in r_list:
            return_list.append(response_list['plaintext'])
        self.list = return_list
        self.text = ','.join(return_list)