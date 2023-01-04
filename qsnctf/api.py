import requests
import json


# 这里的操作一般都是需要联网的，如果是线下赛请确认主办方允许联网使用


class quipqiup:
    def __init__(self, ciphertext, clues=''):
        self.json = None
        self.text = None
        self.list = None
        # 上是三个返回值，用于取回不同的数据类型，均在quipqiup_return中定义
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
            "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://www.quipqiup.com", "Referer": "https://www.quipqiup.com/",
            "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin",
            "Te": "trailers", "Connection": "close"}
        self.ciphertext = ciphertext
        self.clues = clues
        self.url = 'http://www.quipqiup.com/'
        self.id = self.quipqiup_get_id()
        self.quipqiup_return()

    def quipqiup_get_id(self):
        url = f"{self.url}solve"
        data = {"ciphertext": self.ciphertext, "clues": self.clues, "mode": "auto", "was_auto": True, "was_clue": False}
        response = requests.post(url, headers=self.headers, json=data).json()
        return response['id']

    def quipqiup_return(self):
        url = f"{self.url}status"
        data = {"id": int(self.id)}
        response_data = requests.post(url, headers=self.headers, json=data).json()
        self.json = response_data  # json 直接返回requests的response json
        return_list = []
        for response_list in response_data['solutions']:
            return_list.append(response_list['plaintext'])
        self.list = return_list
        self.text = ','.join(return_list)


class FeishuWebhook:
    # 遵循CamelCase命名
    def __init__(self, title, message, token, send_type='text'):
        """
        :param title: send_title
        :param message: send_message
        :param token: feishu_token Get the content after/v2/hook/of the url
        :param send_type: text or card
        """
        self.url = f"https://open.feishu.cn/open-apis/bot/v2/hook/{token}"
        self.title = title
        self.message = message
        self.headers = {
            "Content-Type": "application/json",
            "charset": "utf-8"
        }
        self.send_type = send_type
        self.send()

    def send(self):
        if self.send_type == 'text':
            data = {
                "msg_type": "text",
                "content": {
                    "text": f"{self.title}\n{self.message}"
                }
            }
        elif self.send_type == 'card':
            data = {
                "msg_type": "interactive",
                "card": {
                    "config": {
                        "wide_screen_mode": True,
                        "enable_forward": True
                    },
                    "elements": [{
                        "tag": "div",
                        "text": {
                            "content": self.message,
                            "tag": "lark_md"
                        }
                    }],
                    "header": {
                        "title": {
                            "content": self.title,
                            "tag": "plain_text"
                        }
                    }
                }
            }
        else:
            raise ValueError("Invalid send_type")
        data = json.dumps(data, ensure_ascii=True).encode("utf-8")
        requests.post(self.url, data=data, headers=self.headers)


class DingTalk:
    def __init__(self, title, message, token):
        """
        :param title: send_title
        :param message: send_message
        :param token: dingding tolken
        """
        self.url = f"https://oapi.dingtalk.com/robot/send?access_token={token}"
        self.title = title
        self.message = message
        self.headers = {
            "Content-Type": "application/json",
            "charset": "utf-8"
        }
        self.send()

    def send(self):
        data = {
            "msgtype": "text",
            "text":
                {
                    "content": f"{self.title}\n{self.message}"
                }
        }
        data = json.dumps(data, ensure_ascii=True).encode("utf-8")
        requests.post(self.url, data=data, headers=self.headers)
