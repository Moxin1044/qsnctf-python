import requests
# 这里的操作一般都是需要联网的，如果是线下赛请确认主办方允许联网使用


class quipqiup:
    # TODO：quipqiup 对接
    def __init__(self, ciphertext, clues=''):
        self.ciphertext = ciphertext
        self.clues = clues
        self.url = 'https://www.quipqiup.com:443/'
        self.id = self.get_quipqiup_id()

    def get_quipqiup_id(self):
        url = "https://www.quipqiup.com:443/solve"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
                   "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                   "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
                   "Origin": "https://www.quipqiup.com", "Referer": "https://www.quipqiup.com/",
                   "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
                   "Te": "trailers", "Connection": "close"}
        json = {"ciphertext": self.ciphertext, "clues": self.clues, "mode": "auto", "was_auto": True, "was_clue": False}
        response = requests.post(url, headers=headers, json=json).json()
        return response['id']
