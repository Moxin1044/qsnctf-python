import qsnctf.plugin.python.operation
import requests
import json
import os


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


class ThreatBook:
    def __init__(self, api_key):
        self.key = api_key

    def ip_reputation(self, ip):
        api = "https://api.threatbook.cn/v3/scene/ip_reputation"
        data = {
            'apikey': self.key,
            'resource': ip,
            'lang': 'zh'
        }
        q = requests.post(url=api, data=data)
        """ 引用
        q_data = json.loads(q.text)
        if q_data['response_code'] == 0:
            data = q_data['data']
            IP_info = data[IP]
            severity = IP_info['severity']  # 威胁等级
            IP_judg = IP_info['judgments']
            if len(IP_judg) != 1:
                tags = ""
                for tag in IP_judg:
                    tags = tags+tag+","
                tags = tags[:-1]
            else:
                tags = IP_judg[0]  # IP标签
            basic = IP_info['basic']
            carrier = basic['carrier'] # 运营商
            location = basic['location']
            country = location['country']  # 国家
            province = location['province']  # 省
            city = location['city']  # 城市
            lng = location['lng']  # 经度
            lat = location['lat']  # 纬度
            scene = IP_info['scene']  # 应用场景
            confidence_level = IP_info['confidence_level']  # 可信度
            is_malicious = IP_info['is_malicious']  # 是否为恶意
            update_time = IP_info['update_time']  # 更新时间
            tags_classes = IP_info['tags_classes']
            if len(tags_classes) != 1:
                tagss = ""
                for tagsss in tags_classes:
                    tagss = tagss + tagsss + ","
                tagss = tagss[:-1]  # 团伙标签
            else:
                tagss = "空"
        """
        return q.json()

    def file_upload(self, file_path, file_name, sandbox_type='win7_sp1_enx64_office2013'):
        url = 'https://api.threatbook.cn/v3/file/upload';
        fields = {
            'apikey': self.key,
            'sandbox_type': sandbox_type,
            'run_time': 60
        }
        file_dir = file_path
        file_name = file_name
        files = {
            'file': (file_name, open(os.path.join(file_dir, file_name), 'rb'))
        }
        response = requests.post(url, data=fields, files=files)
        return response.json()

    def file_report_multiengines(self, sha256):
        """
        :param sha256: file_sha256
        :return: {'data': {'multiengines': {'threat_level': 'clean', 'total': 22,
        'is_white': False, 'total2': 22, 'positives': 0, 'scan_date': '2023-01-05 19:04:42', 'scans': {'IKARUS':
        'safe', 'vbwebshell': 'safe', 'Avast': 'safe', 'Avira': 'safe', 'Sophos': 'safe', 'K7': 'safe',
        'Rising': 'safe', 'Kaspersky': 'safe', 'Panda': 'safe', 'Baidu-China': 'safe', 'NANO': 'safe',
        'Antiy': 'safe', 'AVG': 'safe', 'Baidu': 'safe', 'DrWeb': 'safe', 'GDATA': 'safe', 'Microsoft': 'safe',
        'Qihu360': 'safe', 'ESET': 'safe', 'ClamAV': 'safe', 'JiangMin': 'safe', 'Trustlook': 'safe'}}},
        'response_code': 0, 'verbose_msg': 'OK'}
        """
        url = 'https://api.threatbook.cn/v3/file/report/multiengines'
        params = {
            'apikey': self.key,
            'sha256': sha256
        }
        response = requests.get(url, params=params)
        return response.json()

    def file_report(self, sha256, sandbox_type='win7_sp1_enx64_office2013'):
        """
        :param sha256: file_sha256
        :param sandbox_type: win7_sp1_enx64_office2013
        :return:
        """
        url = 'https://api.threatbook.cn/v3/file/report'
        params = {
            'apikey': self.key,
            'sandbox_type': sandbox_type,
            'sha256': sha256
        }
        response = requests.get(url, params=params)
        return response.json()


class FOFA:
    def __init__(self, email, key, proxy=""):
        self.username = None
        self.email_check = None
        self.email = email
        self.key = key
        self.url = 'https://fofa.info/api/v1'
        self.proxy = proxy
        self.get_userinfo()

    def check_fofa_config(self):
        return f"Email:{self.email} Key:{self.key} Proxy:{self.proxy}"

    def get_userinfo(self):
        # Check Email and key
        url = f"{self.url}/info/my?email={self.email}&key={self.key}"
        response = qsnctf.plugin.python.operation.send_get_json(url, self.proxy)
        if response['error']:
            return response['errmsg']
        else:
            self.email_check = response['email']
            self.username = response['username']
            self.isvip = response['isvip']
            self.viplevel = response['vip_level']
            self.avatar = response['avatar']
            self.fcoin = response['fcoin']
            return self

    def userinfo(self):
        # Check Email and key
        url = f"{self.url}/info/my?email={self.email_check}&key={self.key}"
        response = qsnctf.plugin.python.operation.send_get_json(url, self.proxy)
        if response['error']:
            return response['errmsg']
        else:
            return response

    def search(self, query_text, field=None, page=1, size=100, full=False):
        if field is None:
            field = ['ip', 'host', 'port']
        fields = ','.join(field)
        query = qsnctf.plugin.python.operation.get_base64_url(query_text)
        url = f"{self.url}/search/all?email={self.email_check}&key={self.key}&qbase64={query}&fields={fields}&page={page}&size={size}&full={full}"
        response = qsnctf.plugin.python.operation.send_get_json(url, self.proxy)
        '''
            # 考虑到生产环境，所以不可以在这里直接返回errmsg，统一返回response即可。
            # 下同
            if response['error']:
                return response['errmsg']
            else:
                return response
            '''
        return response

    def search_stats(self, query_text, field=None):
        if field is None:
            field = ['title']
        fields = ','.join(field)
        query = qsnctf.plugin.python.operation.get_base64_url(query_text)
        url = f"{self.url}/search/stats?fields={fields}&qbase64={query}&email={self.email_check}&key={self.key}"
        response = qsnctf.plugin.python.operation.send_get_json(url, self.proxy)
        return response

    def search_host(self, host, detail=False):
        url = f"{self.url}/host/{host}?detail={detail}&email={self.email_check}&key={self.key}"
        response = qsnctf.plugin.python.operation.send_get_json(url, self.proxy)
        return response


class DaSheng:
    def __init__(self, id, key):
        """
        :param id: id
        :param key: key # https://sandbox.freebuf.com/cloudApi
        """
        self.id = id
        self.key = key

    def token(self):
        api = "https://sandbox.riskivy.com/openapi/oauth/token"
        data = {
            'client_id': self.id,
            'client_secret': self.key,
            'grant_type': 'client_credentials',
            'scope': 'openapi'
        }
        q = requests.post(url=api, data=data)
        data = q.json()
        access_token = data['access_token']
        return access_token

    def upload(self, file_dir, file_name):
        api = "https://sandbox.riskivy.com/openapi/mac/sample/upload"
        headers = {
            'Authorization': 'Bearer ' + self.token()
        }
        files = {
            'file': (open(os.path.join(file_dir, file_name), 'rb'))
        }
        response = requests.post(api, headers=headers, files=files)
        # q = requests.post(url=api, headers=headers)
        return response.json()

    def search(self, sha1):
        api = "https://sandbox.riskivy.com/openapi/mac/sample/report/" + sha1
        headers = {
            'Authorization': 'Bearer ' + self.token()
        }
        response = requests.get(api, headers=headers)
        return response.json()


class ZeroZeon:
    def __init__(self, key):
        self.key = key

    def search(self, title):
        url = "https://0.zone/api/data/"
        payload = json.dumps({
            "title": title,
            "title_type": "site",
            "page": 1,
            "pagesize": 10,
            "zone_key_id": self.key
        })
        headers = {
            'User-Agent': 'qsnCTF/1.0.0 (https://www.qsnctf.com)',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Host': '0.zone',
            'Connection': 'keep-alive'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()


class GoCQHttp:
    def __init__(self, go_cq_ip, auth="", proxy=""):
        self.ip = go_cq_ip
        self.auth = auth
        self.proxy = proxy

    def send_private_msg(self, user_id, text):
        body = {
            "Authorization": self.auth
        }
        data = {
            "user_id": user_id,
            "message": text
        }
        return requests.post("http://" + self.ip + "/send_private_msg", data=data, headers=body, proxies=self.proxy)

    def send_group_msg(self, qq_group_id, text):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": qq_group_id,
            "message": text
        }
        return requests.post("http://" + self.ip + "/send_group_msg", data=data, headers=body, proxies=self.proxy)

    def send_msg(self, message_type, user_id, group_id, message, auto_escape):
        body = {
            "Authorization": self.auth
        }
        if message_type == "private":
            data = {
                "message_type": message_type,
                "user_id": user_id,
                "message": message,
                "auto_escape": auto_escape
            }
        else:
            data = {
                "message_type": message_type,
                "group_id": group_id,
                "message": message,
                "auto_escape": auto_escape
            }
        return requests.post("http://" + self.ip + "/send_group_msg", data=data, headers=body, proxies=self.proxy)

    def delete_msg(self, message_id):
        body = {
            "Authorization": self.auth
        }
        data = {
            "message_id": message_id
        }
        return requests.post("http://" + self.ip + "/delete_msg", data=data, headers=body, proxies=self.proxy)

    def set_group_kick(self, group_id, user_id, reject_add_request):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "user_id": user_id,
            "reject_add_request": reject_add_request
        }
        return requests.post("http://" + self.ip + "/set_group_kick", data=data, headers=body, proxies=self.proxy)

    def set_group_ban(self, group_id, user_id, duration):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "user_id": user_id,
            "duration": duration
        }
        return requests.post("http://" + self.ip + "/set_group_ban", data=data, headers=body, proxies=self.proxy)

    def set_group_whole_ban(self, group_id, enable):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "enable": enable
        }
        return requests.post("http://" + self.ip + "/set_group_whole_ban", data=data, headers=body, proxies=self.proxy)

    def set_group_card(self, group_id, user_id, card):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "user_id": user_id,
            "card": card
        }
        return requests.post("http://" + self.ip + "/set_group_card", data=data, headers=body, proxies=self.proxy)

    def set_group_leave(self, group_id, is_dismiss):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "is_dismiss": is_dismiss
        }
        return requests.post("http://" + self.ip + "/set_group_leave", data=data, headers=body, proxies=self.proxy)

    def send_group_sign(self, group_id):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
        }
        return requests.post("http://" + self.ip + "/send_group_sign", data=data, headers=body, proxies=self.proxy)

    def set_friend_add_request(self, flag, approve, remark):
        body = {
            "Authorization": self.auth
        }
        data = {
            "flag": flag,
            "sub_type": approve,
            "remark": remark
        }
        return requests.post("http://" + self.ip + "/set_friend_add_request", data=data, headers=body,
                             proxies=self.proxy)

    def set_group_add_request(self, flag, sub_type, approve, reason):
        body = {
            "Authorization": self.auth
        }
        data = {
            "flag": flag,
            "sub_type": sub_type,
            "approve": approve,
            "reason": reason
        }
        return requests.post("http://" + self.ip + "/set_group_add_request", data=data, headers=body,
                             proxies=self.proxy)

    def get_login_info(self):
        body = {
            "Authorization": self.auth
        }
        return requests.post("http://" + self.ip + "/get_login_info", headers=body, proxies=self.proxy)

    def get_stranger_info(self, user_id):
        body = {
            "Authorization": self.auth
        }
        data = {
            "user_id": user_id,
            "no_cache": True
        }
        return requests.post("http://" + self.ip + "/get_stranger_info", data=data, headers=body, proxies=self.proxy)

    def set_group_special_title(self, group_id, user_id, special_title, duration):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "user_id": user_id,
            "special_title": special_title,
            "duration": duration
        }
        return requests.post("http://" + self.ip + "/set_group_special_title", data=data, headers=body,
                             proxies=self.proxy)

    def set_qq_profile(self, nickname, company, email, college, personal_note):
        body = {
            "Authorization": self.auth
        }
        data = {
            "nickname": nickname,
            "company": company,
            "email": email,
            "college": college,
            "personal_note": personal_note
        }
        return requests.post("http://" + self.ip + "/set_qq_profile", data=data, headers=body, proxies=self.proxy)

    def get_friend_list(self):
        body = {
            "Authorization": self.auth
        }
        return requests.post("http://" + self.ip + "/get_friend_list", headers=body, proxies=self.proxy)

    def get_unidirectional_friend_list(self):
        body = {
            "Authorization": self.auth
        }
        return requests.post("http://" + self.ip + "/get_unidirectional_friend_list", headers=body, proxies=self.proxy)

    def delete_friend(self, user_id):
        body = {
            "Authorization": self.auth
        }
        data = {
            "user_id": user_id
        }
        return requests.post("http://" + self.ip + "/delete_friend", data=data, headers=body, proxies=self.proxy)

    def get_group_info(self, group_id):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "no_cache": True
        }
        return requests.post("http://" + self.ip + "/get_group_info", data=data, headers=body, proxies=self.proxy)

    def get_group_list(self):
        body = {
            "Authorization": self.auth
        }
        data = {
            "no_cache": True
        }
        return requests.post("http://" + self.ip + "/get_group_list", data=data, headers=body, proxies=self.proxy)

    def get_group_member_info(self, group_id, user_id):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "user_id": user_id,
            "no_cache": True
        }
        return requests.post("http://" + self.ip + "/get_group_member_info", data=data, headers=body,
                             proxies=self.proxy)

    def get_group_member_list(self, group_id):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "no_cache": True
        }
        return requests.post("http://" + self.ip + "/get_group_member_list", data=data, headers=body,
                             proxies=self.proxy)

    def get_group_honor_info(self, group_id, types):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "type": types
        }
        return requests.post("http://" + self.ip + "/get_group_honor_info", data=data, headers=body, proxies=self.proxy)

    def set_group_portrait(self, group_id, file):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "file": file,
            "cache": 0
        }
        return requests.post("http://" + self.ip + "/get_group_honor_info", data=data, headers=body, proxies=self.proxy)

    def upload_private_file(self, user_id, file, name):
        body = {
            "Authorization": self.auth
        }
        data = {
            "user_id": user_id,
            "file": file,
            "name": name
        }
        return requests.post("http://" + self.ip + "/upload_private_file", data=data, headers=body, proxies=self.proxy)

    def upload_group_file(self, group_id, file, name, folder=""):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "file": file,
            "name": name,
            "folder": folder
        }
        return requests.post("http://" + self.ip + "/upload_group_file", data=data, headers=body, proxies=self.proxy)

    def get_group_file_system_info(self, group_id):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id
        }
        return requests.post("http://" + self.ip + "/get_group_file_system_info", data=data, headers=body,
                             proxies=self.proxy)

    def get_group_root_files(self, group_id):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id
        }
        return requests.post("http://" + self.ip + "/get_group_root_files", data=data, headers=body, proxies=self.proxy)

    def get_group_files_by_folder(self, group_id, folder_id):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "folder_id": folder_id
        }
        return requests.post("http://" + self.ip + "/get_group_files_by_folder", data=data, headers=body,
                             proxies=self.proxy)

    def create_group_file_folder(self, group_id, name, parent_id="/"):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "name": name,
            "parent_id": parent_id
        }
        return requests.post("http://" + self.ip + "/create_group_file_folder", data=data, headers=body,
                             proxies=self.proxy)

    def delete_group_folder(self, group_id, folder_id):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "folder_id": folder_id
        }
        return requests.post("http://" + self.ip + "/delete_group_folder", data=data, headers=body, proxies=self.proxy)

    def delete_group_file(self, group_id, file_id, busid):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "file_id": file_id,
            "busid": busid
        }
        return requests.post("http://" + self.ip + "/delete_group_file", data=data, headers=body, proxies=self.proxy)

    def get_group_file_url(self, group_id, file_id, busid):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "file_id": file_id,
            "busid": busid
        }
        return requests.post("http://" + self.ip + "/get_group_file_url", data=data, headers=body, proxies=self.proxy)

    def _send_group_notice(self, group_id, content, image=""):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "content": content,
            "image": image
        }
        return requests.post("http://" + self.ip + "/_send_group_notice", data=data, headers=body, proxies=self.proxy)

    def _get_group_notice(self, group_id):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id
        }
        return requests.post("http://" + self.ip + "/_get_group_notice", data=data, headers=body, proxies=self.proxy)

    def set_essence_msg(self, message_id):
        body = {
            "Authorization": self.auth
        }
        data = {
            "message_id": message_id
        }
        return requests.post("http://" + self.ip + "/set_essence_msg", data=data, headers=body, proxies=self.proxy)

    def delete_essence_msg(self, message_id):
        body = {
            "Authorization": self.auth
        }
        data = {
            "message_id": message_id
        }
        return requests.post("http://" + self.ip + "/delete_essence_msg", data=data, headers=body, proxies=self.proxy)

    def get_essence_msg_list(self, group_id):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id
        }
        return requests.post("http://" + self.ip + "/get_essence_msg_list", data=data, headers=body, proxies=self.proxy)

    def set_group_name(self, group_id, group_name):
        body = {
            "Authorization": self.auth
        }
        data = {
            "group_id": group_id,
            "group_name": group_name
        }
        return requests.post("http://" + self.ip + "/get_essence_msg_list", data=data, headers=body, proxies=self.proxy)

    def send_reply(self, message, message_id, user_id, group_id):
        self.send_group_msg(group_id, f"[CQ:reply,id={message_id}][CQ:at,qq={user_id}] {message}")


class Shodan:
    def __init__(self, key):
        self.api_url = "https://api.shodan.io"
        self.key = key

    def api_info(self):
        url = self.api_url + "/api-info" + f"?key={self.key}"
        response = requests.get(url).json()
        return response


    def host(self, ip):
        """
        :param ip: search ip
        :return: request json
        """
        url = self.api_url + f"/shodan/host/{ip}?key={self.key}"
        response = requests.get(url).json()
        return response

